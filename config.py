# префикс бота
BOT_PREFIX = "!"
# статус бота
BOT_STATUS = "!help (!h)"

# команды бота
COMMANDS = ["!translate ( !tr ) - перевод", "!set_lang ( !sl ) - смена режима перевода",
            "!what_lang ( !wl ) - какой язык", "!auto_translate ( !atr ) - автоперевод",
            "!current_mode ( !cm ) - какой режим", "!image_translate ( !itr ) - автоперевод с картинки",
            "!lang_list ( !ll ) - список поддерживаемых языков"]
# команды бота
COMMANDS_CHECK = ["!translate", "!tr", "!set_lang", "!sl", "!what_lang", "!wl", "!auto_translate", "!atr",
                  "!current_mode", "!cm", "!image_translate", "!itr", "!lang_list", "!ll"]
# помощь к командам бота
COMMANDS_HELP = {
    "!translate": {"title": "!translate ( !tr )",
                   "value": "Команда для перевода текста в соответствии с установленным режимом перевода (Лучше "
                            "переводить словосочетания - перевод будет точнее)",
                   "footer": "Пример: !tr Привет", "usage": "!translate ( !tr ) {текст-который-нужно-перевести}"},
    "!tr": {"title": "!translate ( !tr )",
            "value": "Команда для перевода текста в соответствии с установленным режимом перевода",
            "footer": "Пример: !tr Привет", "usage": "!translate ( !tr ) {текст-который-нужно-перевести}"},
    "!set_lang": {"title": "!set_lang ( !sl )", "value": "Команда для смены Вашего режима перевода",
                  "footer": "Пример: !sl русский английский", "usage": "!set_lang ( !sl ) {первый-яызк} {второй-язык}"},
    "!sl": {"title": "!set_lang ( !sl )", "value": "Команда для смены Вашего режима перевода",
            "footer": "Пример: !sl русский английский", "usage": "!set_lang ( !sl ) {первый-яызк} {второй-язык}"},
    "!what_lang": {"title": "!what_lang ( !wl )", "value": "Команда для определения языка, на котором написан текст",
                   "footer": "Пример: !wl Hello", "usage": "!what_lang ( !sl ) {текст-язык-которого-нужно-определить}"},
    "!wl": {"title": "!what_lang ( !wl )", "value": "Команда для определения языка, на котором написан текст",
            "footer": "Пример: !wl Hello", "usage": "!what_lang ( !sl ) {текст-язык-которого-нужно-определить}"},
    "!auto_translate": {"title": "!auto_translate ( !atr )",
                        "value": "Команда для перевода текста с автоопредлением языка, на котором написан текст",
                        "footer": "Пример: !atr русский Das ist richtig",
                        "usage": "!auto_translate ( !atr ) {язык-на-который-нужно-перевести} {"
                                 "текст_который_нужно_перевести}"},
    "!atr": {"title": "!auto_translate ( !atr )",
             "value": "Команда для перевода текста с автоопредлением языка, на котором написан текст",
             "footer": "Пример: !atr русский Das ist richtig",
             "usage": "!auto_translate ( !atr ) {язык-на-который-нужно-перевести} {текст_который_нужно_перевести}"},
    "!current_mode": {"title": " !current_mode ( !cm ) ",
                      "value": "Команда для получения Вашего текущего режима перевода", "footer": "Пример: !cm",
                      "usage": "!current_mode ( !cm )"},
    "!cm": {"title": " !current_mode ( !cm ) ", "value": "Команда для получения Вашего текущего режима перевода",
            "footer": "Пример: !cm", "usage": "!current_mode ( !cm )"},
    "!image_translate": {"title": "!image_translate ( !itr )",
                         "value": "Команда для перевода текста с картинки (язык текста на картинке определяется "
                                  "автоматически) ВНИМАНИЕ! Команда находится в Beta-тесировании, возможны ошибки",
                         "footer": "Изображения с перевёрнутым текстом не читаются!",
                         "usage": "{прикрлеплённое-иозбражение} !itr {язык-на-который-нужно-перевести}"},
    "!itr": {"title": "!image_translate ( !itr )",
             "value": "Команда для перевода текста с картинки (язык текста на картинке определяется автоматически) "
                      "ВНИМАНИЕ! Команда находится в Beta-тесировании, возможны ошибки",
             "footer": "Изображения с перевёрнутым текстом не читаются!",
             "usage": "{прикрлеплённое-иозбражение} !itr {язык-на-который-нужно-перевести}"},
    "!lang_list": {"title": " !lang_list ( !ll ) ",
                   "value": "Команда для получения списка поддерживаемых языков", "footer": "Пример: !ll",
                   "usage": "!lang_list ( !ll )"},
    "!ll": {"title": " !lang_list ( !ll ) ",
            "value": "Команда для получения списка поддерживаемых языков", "footer": "Пример: !ll",
            "usage": "!lang_list ( !ll )"},
}

# токен
TOKEN = "NzA5MzE2MzQyMTUwNDYzNTE5.XrkJlw._Su8MLKaA1780Sp0KnHMEXl25Ec"

# ссылка на переводчик
URL_TRANS = "https://translate.yandex.net/api/v1.5/tr.json/translate"

# ссылка на определение языка
URL_WHAT = "https://translate.yandex.net/api/v1.5/tr.json/detect"

# ссылка на получение языков
URL_GET_LANGS = "https://translate.yandex.net/api/v1.5/tr.json/getLangs"

# ключ
KEY = "trnsl.1.1.20200511T113948Z.01f4b5f90f5999ef.7f71ac10d5d647c5d2b4affa1f6f06e48edbd31e"

# ключ
IAM = "CggVAgAAABoBMxKABGXdYSVGQOAitWEoUHcpWJyZoamD5lg_ktpCOBVanirUDDypw-IcW" \
      "--L7xWQ5EeFhja9wH531aN1xmwSIzCG2bpOAjbZ85B8peOJ0Moo_jzXL3Wg3W4REBB_npFpq67y9n7KKSYySrB_JTJIXXETBdWV1SVSooxdNxc" \
      "-TUsLbUSPxHnPNaUIALOhGpvh8CYXIyGxtVJ9UFukCWA1UKMqLknThWfP-HxOaaw5KnIfNQ3xvThh97a-0yydh-B4AW5lC" \
      "-TRqDV1k7ZL0j8crP3c1zNRPvnQGHpXC2dMvFiA2-J2GwEHpQEOfWPTMh--z0MK-5oupdnUT5BoN_1KXExdNNBofPBw5j6OE" \
      "-fzaE_WOHiKxQvDF0h0xNf8eLjV8IPt6XUbG7Mn3SPQnyUS" \
      "-nj1NHxI0ytbM85UndaiHKefOODcRV_cJNdqsru8BpM799LgVKrZ1gtqET65Vkg8txuyKX4cPs5BuzrNPtaFv3R1dfU4AsdkQbRPi9CzAQd4Bd9XQ69HDBwSe8EnXLHkOTrj47JqGTCOx6qQlrv6Hbps-KtKPIwjEqxqvqM1dhi1Zqq7quTtHRDAb2NNVSeZQFjN2AbddibAzgqPlwI8RpZ2kcHOdzXO1KP6SlMgumEUE17Sf9hNE8Ps7xVeNxUGE_35tQqtpdawaKcKQgsC8wZk-c3YGiQQ2_bk9QUYm8jn9QUiFgoUYWplY25uOHNlcWhhNXZ1czJrcWo= "
