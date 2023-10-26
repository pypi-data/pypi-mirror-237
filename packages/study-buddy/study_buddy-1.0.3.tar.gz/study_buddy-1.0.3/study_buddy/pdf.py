from tempfile import TemporaryDirectory
from pathlib import Path

from pdf2image import convert_from_path

import image
import text

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pdf_to_speech(pdf_path: str, output_file: str = 'pdf.mp3'):
    """
    Read a PDF file and converts it to an MP3 file
    :param pdf_path: The path to the PDF file
    :param output_file: The path to the output MP3 file
    :return: None
    """
    logger.info('Starting PDF to speech conversion')
    pdf_text = pdf_to_text(pdf_path)
    text.text_to_speech(pdf_text, output_file)


def pdf_to_text(pdf_path: str, output_path: str = None) -> str:
    """
    Read a PDF file and output the text to a file
    :param pdf_path: The path to the PDF file
    :param output_path: The path to the output file
    :return: None
    """
    logger.info('Starting PDF to text conversion')
    pdf_file = Path(pdf_path)

    with TemporaryDirectory() as temp_dir:
        # Store all the pages of the PDF in a variable
        image_file_list = pdf_to_image(pdf_file, temp_dir)
        pdf_text = ""
        if output_path:
            text_file = Path("~").expanduser() / Path(output_path)
            with open(text_file, "a") as output_file:
                for image_file in image_file_list:
                    image_text = image.image_to_text(image_file)
                    output_file.write(image_text)
                    pdf_text += image_text
        else:
            for image_file in image_file_list:
                image_text = image.image_to_text(image_file)
                pdf_text += image_text
    return pdf_text


def pdf_to_image(pdf_file: Path, temp_dir: str) -> list:
    """
    Convert a PDF file to a list of images
    :param pdf_file: The path to the PDF file
    :param temp_dir: The path to the temporary directory the files will be saved in
    :return: A list of image files
    """
    logger.info('Starting PDF to image conversion')
    pdf_pages = convert_from_path(pdf_file, 500)
    image_file_list = []

    for page_enumeration, page in enumerate(pdf_pages, start=1):
        filename = f"{temp_dir}/page_{page_enumeration:03}.jpg"
        page.save(filename, "JPEG")
        image_file_list.append(filename)

    return image_file_list


if __name__ == "__main__":
    pdf_to_speech("test.pdf")
