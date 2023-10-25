from psycopg2cffi import compat

compat.register()
import aiopg  # after compat.register()
import re
import time
import ujson
from options import dsn

sql_durations_times = {}


def convert_value_to_hstore(value):
    if isinstance(value, (dict, list)):
        return f"'{ujson.dumps(value)}'"

    elif isinstance(value, bool):
        return str(value).lower()

    elif isinstance(value, (int, float)):
        return value

    elif isinstance(value, str):
        return f"'{value}'"

    return value


class Tablo:
    def __init__(self, table_name):
        self.table_name = table_name
        self.insert_values = {}
        self.set_values = {}
        self.like_conditions = {}
        self.likenot_conditions = {}
        self.likesw_conditions = {}
        self.likeew_conditions = {}
        self.likenotew_conditions = {}
        self.likenotsw_conditions = {}
        self.where_conditions = {}
        self.wherenot_conditions = {}
        self.selected_fields = "*"
        self.order_by = None

    def order(self, field):
        self.order_by = field
        return self

    def asc(self):
        if self.order_by:
            self.order_by = f"{self.order_by} ASC"
        return self

    def desc(self):
        if self.order_by:
            self.order_by = f"{self.order_by} DESC"
        return self

    def update(self, **kwargs):
        self.set_values.update(kwargs)
        return self

    def insert(self, **kwargs):
        self.insert_values = kwargs
        return self

    def where(self, **kwargs):
        self.where_conditions.update(kwargs)
        return self

    def wherenot(self, **kwargs):
        self.wherenot_conditions.update(kwargs)
        return self

    def like(self, **kwargs):
        self.like_conditions.update(kwargs)
        return self

    def likenot(self, **kwargs):
        self.likenot_conditions.update(kwargs)
        return self

    def likesw(self, **kwargs):
        self.likesw_conditions.update(kwargs)
        return self

    def likenotsw(self, **kwargs):
        self.likenotsw_conditions.update(kwargs)
        return self

    def likeew(self, **kwargs):
        self.likeew_conditions.update(kwargs)
        return self

    def likenotew(self, **kwargs):
        self.likenotew_conditions.update(kwargs)
        return self

    def select(self, *fields, fetchall=None):
        if fields:
            self.selected_fields = fields
        else:
            self.selected_fields = ["*"]

        self.fetchall = fetchall
        return self

    async def execute(self):

        # SQL sorgusunu oluştururken her bir koşul ekleniyor
        sql = f"SELECT {', '.join(self.selected_fields)} FROM {self.table_name}"

        if self.likenot_conditions:
            where_params = [f"{key} not like '%%{value}%%'" for key, value in self.likenot_conditions.items()]
            sql += " WHERE " + " AND ".join(where_params)

        if self.like_conditions:
            where_params = [f"{key} like '%%{value}%%'" for key, value in self.like_conditions.items()]
            sql += " WHERE " + " AND ".join(where_params)

        if self.likesw_conditions:
            where_params = [f"{key} like '{value}%%'" for key, value in self.likesw_conditions.items()]
            sql += " WHERE " + " AND ".join(where_params)

        if self.likenotsw_conditions:
            where_params = [f"{key} not like '{value}%%'" for key, value in self.likenotsw_conditions.items()]
            sql += " WHERE " + " AND ".join(where_params)

        if self.likeew_conditions:
            where_params = [f"{key} like '%%{value}'" for key, value in self.likeew_conditions.items()]
            sql += " WHERE " + " AND ".join(where_params)

        if self.likenotew_conditions:
            where_params = [f"{key} not like '%%{value}'" for key, value in self.likenotew_conditions.items()]
            sql += " WHERE " + " AND ".join(where_params)

        if self.where_conditions:
            where_params = [f"{key} = %s" for key in self.where_conditions]
            for key, value in self.where_conditions.items():
                if isinstance(value, list):
                    where_params = [f"{key} in {tuple(value)}" for key in self.where_conditions]
            sql += " WHERE " + " AND ".join(where_params)

        if self.wherenot_conditions:
            where_params = [f"{key} != %s" for key in self.wherenot_conditions]
            for key, value in self.wherenot_conditions.items():
                if isinstance(value, list):
                    where_params = [f"{key} not in {tuple(value)}" for key in self.wherenot_conditions]
            sql += " WHERE " + " AND ".join(where_params)

        if self.order_by:
            sql += f" ORDER BY {self.order_by};"

        params = (
                tuple(self.set_values.values())
                  + tuple(self.insert_values.values())
                  + tuple(self.where_conditions.values())
                  + tuple(self.wherenot_conditions.values())
                  + tuple(self.like_conditions.values())
                  + tuple(self.likenot_conditions.values())
                  + tuple(self.likesw_conditions.values())
                  + tuple(self.likeew_conditions.values())
                  + tuple(self.likenotsw_conditions.values())
                  + tuple(self.likenotew_conditions.values())
                  )

        async with aiopg.create_pool(dsn) as pool, pool.acquire() as conn, conn.cursor() as cur:
            if self.set_values:
                await cur.execute(f"{sql} RETURNING id;", params)
                returning_id = await cur.fetchone()
                self.reset_conditions()  # Sorgu bitiminde koşulları sıfırla
                return {'status': True, 'message': 'updated', 'id': returning_id[0]} if returning_id else {'status': False, 'message': 'not_returning_id', 'id': None}
            elif self.insert_values:
                await cur.execute(sql, tuple(self.insert_values.values()))
                returning_id = await cur.fetchone()
                self.reset_conditions()  # Sorgu bitiminde koşulları sıfırla
                return {'status': True, 'message': 'added', 'id': returning_id[0]} if returning_id else {'status': False, 'message': 'not_returning_id', 'id': None}
            else:
                # full_sql = cur.mogrify(sql, params)
                # print("SQL Query:", full_sql)
                await cur.execute(sql, params) if params else await cur.execute(sql)
                self.reset_conditions()  # Sorgu bitiminde koşulları sıfırla
                if self.fetchall:
                    result = await cur.fetchall()
                    if result:
                        result_list = []
                        for row in result:
                            row_dict = {cur.description[i].name: value for i, value in enumerate(row)}
                            result_list.append(row_dict)
                        return result_list
                    else:
                        return []
                else:
                    result = await cur.fetchone()
                    if result:
                        return {cur.description[i].name: value for i, value in enumerate(result)}
                    else:
                        return {'status': False, 'message': 'not_found'}

    async def delete(self):
        sql = f"DELETE FROM {self.table_name}"
        if self.where_conditions:
            where_params = [f"{key} = %s" for key in self.where_conditions]
            sql += " WHERE " + " AND ".join(where_params)
        try:
            async with aiopg.create_pool(dsn) as pool, pool.acquire() as conn, conn.cursor() as cur:
                await cur.execute(sql, tuple(self.where_conditions.values()))
                if cur.rowcount > 0:
                    return {'status': True, 'message': 'deleted', 'id': self.where_conditions.get('id')}
                else:
                    return {'status': False, 'message': 'not_deleted', 'id': None}
        except Exception as e:
            return {'status': False, 'message': str(e).split('\n')[0]}

    def reset_conditions(self):
        # Sorgu bitiminde koşulları sıfırla
        self.insert_values = {}
        self.set_values = {}
        self.like_conditions = {}
        self.likenot_conditions = {}
        self.likesw_conditions = {}
        self.likenotsw_conditions = {}
        self.likeew_conditions = {}
        self.likenotew_conditions = {}
        self.where_conditions = {}
        self.wherenot_conditions = {}


async def db_delete(sql, params=None):
    try:
        async with aiopg.create_pool(dsn) as pool, pool.acquire() as conn, conn.cursor() as cur:
            params = (params,) if not isinstance(params, tuple) else params
            await cur.execute(f"{sql} RETURNING id;", params)
            returning_id = await cur.fetchone()
            return {'status': True, 'message': returning_id[0]} if returning_id else {'status': False, 'message': 'not_returning_id'}
    except Exception as e:
        return {'status': False, 'message': str(e).split('\n')[0]}


async def db_update(sql, params=None):
    try:
        async with aiopg.create_pool(dsn) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    params = (params,) if not isinstance(params, tuple) else params
                    await cur.execute(f"{sql} RETURNING id;", params)
                    returning_id = await cur.fetchone()
                    return {'status': True, 'message': returning_id[0]} if returning_id else {'status': False, 'message': 'not_returning_id'}
    except Exception as e:
        return {'status': False, 'message': str(e).split('\n')[0]}


async def db_insert(sql, params=None):
    try:
        async with aiopg.create_pool(dsn) as pool, pool.acquire() as conn, conn.cursor() as cur:
            params = (params,) if not isinstance(params, tuple) else params
            await cur.execute(f"{sql} RETURNING id;", params)
            returning_id = await cur.fetchone()
            return {'status': True, 'message': returning_id[0]} if returning_id else {'status': False, 'message': 'not_returning_id'}
    except Exception as e:
        return {'status': False, 'message': str(e).split('\n')[0]}


async def db_query(sql, params=None, fetchall=False, servertiming_number=None, servertiming_desc=None):
    servertiming_desc = re.sub(r'[^a-zA-Z0-9]', '', servertiming_desc)[0:15]

    try:
        async with aiopg.create_pool(dsn) as pool, pool.acquire() as conn, conn.cursor() as cur:
            params = (params,) if not isinstance(params, tuple) else params

            start_time = time.time()
            ############################################################################
            await cur.execute(sql, params) if params else await cur.execute(sql)
            if fetchall:
                response_data = await cur.fetchall()
                # Dönen sonuçları düzeltmek için, iç içe listeleri birleştir
                response_data = [item for sublist in response_data for item in sublist]
            else:
                response_data = await cur.fetchone()
            ############################################################################
            end_time = time.time()

            if servertiming_number:
                sql_durations_times[f"{servertiming_number}_{servertiming_desc}"] = int((end_time - start_time) * 1000)

            if response_data:
                if not fetchall and len(response_data) == 1:
                    return response_data[0]  # Tek bir sonuç ise tek bir JSON olarak döndür
                return response_data  # Birden fazla sonuç ise liste içinde JSON olarak döndür
            else:
                return {'status': False, 'message': 'record_not_found'}
    except Exception as e:
        return {'status': False, 'message': str(e).split('\n')[0]}
