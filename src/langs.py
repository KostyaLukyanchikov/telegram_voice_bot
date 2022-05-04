RU = 'ru'
EN = 'en'
SUPPORTED_LANGS = (RU, EN)
DEFAULT = EN


def lang_map(lang: str):
    return lang if lang in SUPPORTED_LANGS else DEFAULT
