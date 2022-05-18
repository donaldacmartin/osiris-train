from typing import List

from cleantext import clean
from nltk import corpus, download, word_tokenize


PUNCTUATION = list(":',-’()/\\.“”#?!")
LANGUAGE_MAP = {"eng": "english", "fra": "french"}


def init_libraries() -> None:
    download('punkt')
    download('stopwords')


def preprocess_text(text: str, language: str) -> List[str]:
    clean_text = clean(text, no_emoji=True, no_punct=True, no_urls=True, no_line_breaks=True)
    words = word_tokenize(clean_text, language=LANGUAGE_MAP[language])
    language_stopwords = corpus.stopwords.words(LANGUAGE_MAP[language])
    no_stopwords = [word for word in words if word not in language_stopwords]
    return [word for word in no_stopwords if word not in PUNCTUATION]

