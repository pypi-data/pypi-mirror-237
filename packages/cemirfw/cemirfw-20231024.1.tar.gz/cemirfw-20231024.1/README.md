# cemirfw

# Install

```shell
sudo bash install.sh
```
```shell
cemirfw start
cemirfw stop
cemirfw restart
cemirfw disable
cemirfw status
```


## Sample endpoints
```python
@cemir_sget(r"/get", auth=False, redis_cache_params={"expire_time": 30, "key": "ip,useragent"})
# @cemir_sget(r"/get", auth=True)
@rate_limit(limit=3, period=1, period_max=5, block_time=10)
@check_params(["fiyat"])
async def get_get(request):

    status, response_data = await db_query("SELECT pg_sleep(1);", id, False, 1, "1sn")
    fiyat = float(request.params("fiyat"))

    vergi_orani = 20  # %20 KDV oranı
    otv_orani = 0  # %2 ÖTV oranı
    islem_ucreti = 0  # 10 TL işlem ücreti
    komisyon_orani = 0  # %5 Komisyon oranı

    tutarlar = DotDict(def_hersey_haric_fiyat_more(fiyat, vergi_orani, otv_orani, islem_ucreti, komisyon_orani, yuvarlama=2))
    return tutarlar
```