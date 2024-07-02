from TextData.models import Language
from TextData.services.text import get_text_by_language_and_key


def get_text(key: str, lang: Language) -> str:
    return get_text_by_language_and_key(key=key, lang=lang)
