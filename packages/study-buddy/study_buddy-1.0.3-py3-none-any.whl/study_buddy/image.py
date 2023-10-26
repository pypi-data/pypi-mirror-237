from PIL import Image
from pytesseract import pytesseract

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def image_to_text(image_file: str) -> str:
    """
    Read an image file and return the text using Tesseract
    :param image_file: The path to the image file
    :return: The text from the image
    """
    logger.info('Starting image to text conversion')
    text = str((pytesseract.image_to_string(Image.open(image_file))))
    text = text.replace("-\n", "")
    text = text.replace("\n", " ")

    return text
