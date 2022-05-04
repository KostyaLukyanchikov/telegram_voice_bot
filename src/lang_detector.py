import spacy
from spacy import Language
from spacy_langdetect import LanguageDetector

import langs
from langs import lang_map


def get_lang_detector(nlp, name):
    return LanguageDetector()


nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)


def detect_lang(text):
    try:
        return lang_map(nlp(text)._.language['language'])
    except:
        return langs.DEFAULT
