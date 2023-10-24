import translators as ts


def get_translation(text: str):
    """
    Insert an English text or word to get the translation into Portuguese.
    :param text: Text/word to be translated
    :return: The translation
    """
    return ts.translate_text(text, from_language='en', to_language='pt', translator='google')
