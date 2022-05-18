"""osiris_train.__main__

The main application.
"""

from .preprocess import preprocess_text
from .repo import get_docs


if __name__ == "__main__":
    user_data = get_docs()
    sample = user_data[0][1]["2022-05-16"][0]
    print(preprocess_text(sample["description"], sample["language"]))
