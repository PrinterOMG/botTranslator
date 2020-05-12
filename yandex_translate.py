# подключение библиотек
import config
import requests


# функция отправки запроса для получения списка языков
def get_langs():

    # параметры запроса
    params = {

        "key": config.KEY,
        "ui": "ru"

    }

    # отправка запроса и поулчение ответа
    response = requests.get(config.URL_GET_LANGS, params=params)

    # перевод ответа в json
    func_json = response.json()

    # возвращение списка языков
    return func_json["langs"]


# функция отправки запроса для определения языка на котором написан текст
def what_lang_text(text):

    # параметры запроса
    params = {

        "key": config.KEY,
        "text": text

    }

    # отправка запроса и поулчение ответа
    response = requests.get(config.URL_WHAT, params=params)

    # перевод ответа в json
    func_json = response.json()

    # возвращение списка языков
    return func_json["lang"]


# функция отправки запроса для получния перевода текста
def translate_text(text, lang):

    # параметры запроса
    params = {

        "key": config.KEY,
        "text": text,
        "lang": lang

    }

    # отправка запроса и поулчение ответа
    response = requests.get(config.URL_TRANS, params=params)

    # перевод ответа в json
    func_json = response.json()

    # возвращение списка языков
    return ''.join(func_json["text"])
