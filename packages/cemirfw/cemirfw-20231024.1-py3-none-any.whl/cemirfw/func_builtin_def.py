def def_vergi_dahil_fiyat(vergi_dahil_fiyat, vergi_orani, yuvarlama=2):
    vergi_haric_fiyat = round(vergi_dahil_fiyat / (1 + (vergi_orani / 100)), yuvarlama)
    vergi_miktari = round(vergi_dahil_fiyat - vergi_haric_fiyat, yuvarlama)
    toplam_fiyat = round(vergi_haric_fiyat + vergi_miktari, yuvarlama)
    return {'vergi_haric_fiyat': vergi_haric_fiyat, 'vergi_miktari': vergi_miktari, 'toplam_fiyat': toplam_fiyat}


def def_vergi_haric_fiyat(vergi_haric_fiyat, vergi_orani, yuvarlama=2):
    vergi_miktari = round(vergi_haric_fiyat * (vergi_orani / 100), yuvarlama)
    toplam_fiyat = round(vergi_haric_fiyat + vergi_miktari, yuvarlama)
    return {'vergi_haric_fiyat': vergi_haric_fiyat, 'vergi_miktari': vergi_miktari, 'toplam_fiyat': toplam_fiyat}


def def_hersey_dahil_fiyat_more(vergi_dahil_fiyat, vergi_orani, otv_orani, islem_ucreti, komisyon_orani, yuvarlama=2):
    vergi_haric_fiyat = round(vergi_dahil_fiyat / (1 + (vergi_orani / 100)), yuvarlama)
    vergi_miktari = round(vergi_dahil_fiyat - vergi_haric_fiyat, yuvarlama)

    # ÖTV tutarı hesaplanır
    otv_miktari = round(vergi_dahil_fiyat * (otv_orani / 100), yuvarlama)

    # Komisyon hesaplanır
    komisyon_miktari = round(vergi_dahil_fiyat * (komisyon_orani / 100), yuvarlama)

    # İşlem ücreti hesaplanır
    islem_ucreti_miktari = round(islem_ucreti, yuvarlama)

    toplam_fiyat = vergi_dahil_fiyat - vergi_miktari - otv_miktari - islem_ucreti_miktari - komisyon_miktari

    return {'toplam_fiyat': toplam_fiyat, 'vergi_miktari': vergi_miktari, 'otv_miktari': otv_miktari, 'islem_ucreti_miktari': islem_ucreti_miktari, 'komisyon_miktari': komisyon_miktari}


def def_hersey_haric_fiyat_more(vergi_haric_fiyat, vergi_orani, otv_orani, islem_ucreti, komisyon_orani, yuvarlama=2):
    # Vergi miktarı hesaplanır
    vergi_miktari = round(vergi_haric_fiyat * (vergi_orani / 100), yuvarlama)

    # İşlem ücreti hesaplanır
    islem_ucreti_miktari = round(islem_ucreti, yuvarlama)

    # Komisyon hesaplanır
    komisyon_miktari = round(vergi_haric_fiyat * (komisyon_orani / 100), yuvarlama)

    # ÖTV hesaplanır
    otv_miktari = round(vergi_haric_fiyat * (otv_orani / 100), yuvarlama)

    # Vergi dahil fiyat hesaplanır
    toplam_fiyat = round(vergi_haric_fiyat + vergi_miktari + otv_miktari + islem_ucreti_miktari + komisyon_miktari, yuvarlama)

    return {'toplam_fiyat': toplam_fiyat, 'vergi_miktari': vergi_miktari, 'otv_miktari': otv_miktari, 'islem_ucreti_miktari': islem_ucreti_miktari, 'komisyon_miktari': komisyon_miktari}


def mmslugify(input_string):
    # Küçük harf yap
    text = input_string.lower()

    # Boşlukları tire ile değiştir
    text = text.replace(' ', '-')

    # Özel karakterleri temizle
    text = ''.join(char for char in text if char.isalnum() or char == '-')

    return text


def parse_cookies(cookie_string):
    cookies = {}
    if cookie_string:
        cookie_parts = cookie_string.split(';')
        for part in cookie_parts:
            key_value = part.strip().split('=')
            if len(key_value) == 2:
                key, value = key_value
                cookies[key] = value
    return cookies


def extract_cookie_info(cookie_data, key):
    cookies = parse_cookies(cookie_data)
    if key in cookies:
        return cookies[key]
    else:
        return None
