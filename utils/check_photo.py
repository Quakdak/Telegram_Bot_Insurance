import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError
from requests import get
from io import BytesIO
from pillow_heif import register_heif_opener


def get_exif(image):
    return image.getexif().get_ifd(0x8825)


def is_blurry(image, threshold=100):
    fm = cv2.Laplacian(image, cv2.CV_64F).var()
    return fm < threshold


def has_noise(image, threshold=10):
    denoised_image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21)
    diff = cv2.absdiff(image, denoised_image)
    mean_diff = diff.mean()
    return mean_diff > threshold


async def check_photo(photo_url: str):
    response = get(photo_url)
    try:
        pil_image = Image.open(BytesIO(response.content))
    except UnidentifiedImageError:
        register_heif_opener()
        pil_image = Image.open(BytesIO(response.content))

    exif = get_exif(pil_image)
    print(exif)
    if not exif or 1 not in exif or 2 not in exif or 3 not in exif or 4 not in exif or 29 not in exif:
        return 'В фото отсутствуют дата, время или геолокация. Возможно у вас выключены геометки/дата/время в настройках камеры/галереи'

    width, height = pil_image.size

    if width < 1600 or height < 1200:
        return "Фотография не соответствует разрешению"

    '''image_array = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)'''

    return True
# check_photo("https://api.telegram.org/file/bot6664800041:AAH-YTC9r44vRbrQkLZzNk90rQWqRIpLCIo/photos/file_0.jpg")
# check_photo("https://www.imgonline.com.ua/result_img/imgonline-com-ua-Blur-mglUmgw7PCsuiNM.jpg")
