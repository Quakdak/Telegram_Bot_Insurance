import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError
from requests import get
from io import BytesIO
from pillow_heif import register_heif_opener


def get_exif(image):
    return image.getexif().get_ifd(0x8825)


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
    try:
        pil_image = Image.open(BytesIO(response.content))
    except UnidentifiedImageError:
        register_heif_opener()
        pil_image = Image.open(BytesIO(response.content))

    exif = get_exif(pil_image)
    if not exif or 1 not in exif or 2 not in exif or 3 not in exif or 4 not in exif or 31 not in exif:
        return 'В фото отсутствуют дата, время или геолокация'''

    width, height = pil_image.size

    # Проверяем разрешение
    if width >= 1600 and height >= 1200:
        pass
    else:
        return "Фотография не соответствует разрешению"

    return True
""" image = np.array(bytearray(response.content), dtype=np.uint8)

 img = cv2.imdecode(image, cv2.IMREAD_COLOR)

 blurry = is_blurry(img)
 noisy = has_noise(img)
 if blurry or noisy:
     return 'Фотография размыта или содержит шумы'"""


# check_photo("https://api.telegram.org/file/bot6664800041:AAH-YTC9r44vRbrQkLZzNk90rQWqRIpLCIo/photos/file_0.jpg")
# check_photo("https://www.imgonline.com.ua/result_img/imgonline-com-ua-Blur-mglUmgw7PCsuiNM.jpg")
