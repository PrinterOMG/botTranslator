!pip install opencv-python
!apt update && apt install -y libsm6 libxext6


# подключение библиотек
from PIL import Image
import pytesseract
import cv2
import os
import requests


def image_to_text(url):

    url = url

    # получение расширения изображения в ссылке
    ext = url[url.rfind("."):]

    # скачивание изображения
    p = requests.get(url)
    out = open(r"images\img" + ext, "wb")
    out.write(p.content)
    out.close()

    image = r'images\img' + ext

    preprocess = "thresh"

    # загрузка образа и преобразование его в оттенки серого
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # проверка, следует ли применять пороговое значение для предварительной обработки изображения
    if preprocess == "thresh":

        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # если нужно медианное размытие, чтобы удалить шум
    elif preprocess == "blur":

        gray = cv2.medianBlur(gray, 3)

    # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # загрузка изображения в виде объекта image Pillow, применение OCR
    text = pytesseract.image_to_string(Image.open(filename))

    # удаление файлов
    os.remove(filename)
    os.remove(r"images\img" + ext)

    if text:

        return str(text)

    else:

        return False
