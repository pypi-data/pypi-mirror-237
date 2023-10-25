from basemodels import PostInvoicesData
from func_builtin_class import DataContainer, DotDict
from func_builtin_def import def_hersey_haric_fiyat_more
from func_dbs import db_query
from func_handlers import get, check_params, post, put
from func_ratelimit import rate_limit




@put("/putet")
async def putet(request):
    print(request.json)



@get(r"/fiyat-hesapla", auth=False, redis_cache_params={"expire_time": 30, "key": "ip,useragent"})
# @get(r"/fiyat-hesapla")
@check_params(["fiyat"])
async def get_cache(request):
    # print(request.headers["staffs_id"])
    # print(request.headers["token_expiration"])
    # print(request.headers["token"])

    status, response_data = await db_query("SELECT pg_sleep(0.1);", id, False, 1, "1sn")
    fiyat = float(request.params("fiyat"))

    vergi_orani = 20  # %20 KDV oranı
    otv_orani = 2  # %2 ÖTV oranı
    islem_ucreti = 10  # 10 TL işlem ücreti
    komisyon_orani = 5  # %5 Komisyon oranı

    tutarlar = DotDict(def_hersey_haric_fiyat_more(fiyat, vergi_orani, otv_orani, islem_ucreti, komisyon_orani, yuvarlama=1))
    return tutarlar

@get(r"/pi", auth=False, redis_cache_params={"expire_time": 30, "key": "ip,cookie:username"})
@check_params(["id"])
async def get_pi(request):
    # await tornado.gen.sleep(1)  # Örnek olarak 1 saniyelik bekle
    id = request.params("id")  # id değerini al
    param2 = request.params("param2")

    status, response_data = await db_query("SELECT pg_sleep(0.1);", id, False, 1, "pg_sleep1")

    # if not status:
    #     return {"status": status, "detail": response_data}

    status, response_data = await db_query("SELECT * FROM accounting__customer_proforma_invoices where id=%s;", id, False, 2, "proformainvoices")

    return response_data


@post(r"/post", auth=True, redis_cache_params={"expire_time": 10, "key": "ip,useragent,cookie:username"})
@rate_limit(limit=5, period=5, period_max=10, block_time=10)
async def post_handler(request, data):
    # print(request.headers["staffs_id"])
    # print(request.headers["token_expiration"])
    print(request.headers["token"])

    update_data = PostInvoicesData(**data)

    invoices_id = update_data.invoices_id
    afloat = update_data.afloat
    astr = update_data.astr
    # print(afloat)

    content = DataContainer(update_data.content)
    quantity = content.quantity
    currency = content.currency
    aadate = content.project_date

    # print(aadate)

    status, response_data = await db_query("SELECT * FROM accounting__customer_proforma_invoices where id=%s;", invoices_id, False, 1, "postsample")
    if not status:
        return {"status": status, "detail": response_data}

    return response_data
