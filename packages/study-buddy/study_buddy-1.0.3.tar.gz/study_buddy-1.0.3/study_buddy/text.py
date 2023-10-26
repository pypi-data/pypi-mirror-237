from gtts import gTTS

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def text_to_speech(text: str, output_file: str = 'text.mp3'):
    """
    Convert text to speech
    :param text: The text to convert
    :param output_file: The path to the output MP3 file
    :return: None
    """
    logger.info('Starting text to speech conversion')
    my_obj = gTTS(text=text, lang='en', slow=False)
    my_obj.save(output_file)
