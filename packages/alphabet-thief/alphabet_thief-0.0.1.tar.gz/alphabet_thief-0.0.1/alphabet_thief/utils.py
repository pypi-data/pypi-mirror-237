import re
import unicodedata

from .diacritics import DIACRITICS_UTF8

WORD_REGEX = re.compile(r'\w')
DIACRITICS_UTF8_REGEX = re.compile(b'(' + b'|'.join(DIACRITICS_UTF8) + b')+')


def replace(text: str, replacement: str) -> str:
    new_chars = []
    for char in text:
        if WORD_REGEX.search(char) is None:
            new_chars.append(char)
        else:
            byte_string = unicodedata.normalize('NFD', char).encode()
            matched = DIACRITICS_UTF8_REGEX.search(byte_string)
            diacritics = b'' if matched is None else matched.group()
            new_char = (replacement.encode() + diacritics).decode()
            new_char = unicodedata.normalize('NFC', new_char)
            new_chars.append(new_char)
    return ''.join(new_chars)


def steal(text: str) -> str:
    return replace(text=text, replacement=' ')
