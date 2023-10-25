from func_dbs import db_query, Tablo
from func_handlers import put, get, check_params


@put(r"/fiyat-guncelle", auth=False, redis_cache_params={"expire_time": 30, "key": "ip,useragent"})
async def putete(request, data):
    table = Tablo("test1")

    # ins_result = await table.insert(name="asd", blocked=True, content=data).execute()
    # upd_result = await table.update(blocked=True, name="asdasdasdasdasdasd").where(id=7).execute()

    # del_result = await table.where(id=15).delete()

    # sel_result = await table.select("*", fetchall=True).wherenot(name=["asd", "John", "Johdddddddddddddddddn"]).order('id').asc().execute()
    # sel_result = await table.select("*", fetchall=True).wherenot(id=3).order('id').asc().execute()
    # sel_result = await table.select("*", fetchall=True).wherenot(name="Johdddddddddddddddddn").order('id').asc().execute()
    # sel_result = await table.select("*", fetchall=True).likenot(name="John").order('id').asc().execute()
    # sel_result = await table.select("*", fetchall=True).likeew(name="hn").order('id').asc().execute()
    # sel_result = await table.select("*", fetchall=True).likenotew(name="asd").order('id').asc().execute()
    # sel_result = await table.select("*", fetchall=True).likesw(name="Jo").order('id').asc().execute()
    sel_result = await table.select("*", fetchall=True).likenotsw(name="asd").order('id').asc().execute()
    # sel_result = await table.select("*").where(id=7).execute()
    return sel_result


@get(r"/pi", redis_cache_params={"expire_time": 3, "key": "ip,useragent"})
@check_params(["id"])
async def get_pi(request):
    id = request.params("id")
    # return await db_query("SELECT content FROM accounting__customer_proforma_invoices where id=%s;", id, False, 2, "proformainvoices")
    return await db_query("SELECT content FROM test1 where id in (1,2,3,4);", id, True, 2, "proformainvoices")
