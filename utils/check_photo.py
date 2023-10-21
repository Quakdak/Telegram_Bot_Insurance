import cv2
import numpy as np
from PIL import Image
from requests import get
from io import BytesIO


def is_blurry(image, threshold=100):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    return fm < threshold


def has_noise(image, threshold=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    diff = cv2.absdiff(gray, blurred)
    stddev = diff.std()
    return stddev > threshold


async def check_photo(photo_url: str):
    response = get(photo_url)
    pil_image = Image.open(BytesIO(response.content))

    exif_data = pil_image.getexif()

    if not exif_data or 36867 not in exif_data or 36868 not in exif_data or 34853 not in exif_data:
        return 'В фото отсутствуют дата, время или геолокация'

    width, height = pil_image.size

    # Проверяем разрешение
    if width >= 1600 and height >= 1200:
        pass
    else:
        return "Фотография не соответствует разрешению"

    image = np.array(bytearray(response.content), dtype=np.uint8)

    img = cv2.imdecode(image, cv2.IMREAD_COLOR)

    blurry = is_blurry(img)
    noisy = has_noise(img)
    if blurry or noisy:
        return 'Фотография размыта или содержит шумы'

    return True
# check_photo("https://api.telegram.org/file/bot6664800041:AAH-YTC9r44vRbrQkLZzNk90rQWqRIpLCIo/photos/file_0.jpg")
# check_photo("https://www.imgonline.com.ua/result_img/imgonline-com-ua-Blur-mglUmgw7PCsuiNM.jpg")
