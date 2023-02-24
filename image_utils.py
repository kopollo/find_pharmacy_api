from io import BytesIO

from PIL import Image


def show_image(content: bytes) -> None:
    Image.open(BytesIO(content)).show()
