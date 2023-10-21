from PIL import Image
from PIL.ExifTags import TAGS
from requests import get
from io import BytesIO


async def check_photo(photo_url: str):
    checked_image = 0
    response = get(photo_url)
    image = Image.open(BytesIO(response.content))

    exif_data = image.getexif()

    if exif_data is not None:
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if tag_name == 'DateTimeOriginal' or tag_name == 'GPSInfo':
                checked_image += 1

    size = image.size
    print(size)
