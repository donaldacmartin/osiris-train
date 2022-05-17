"""osiris_train.repo

Abstractions for interacting with Firestore. Requires that the KEY_PATH
environment variable be set to access Firestore credentials.

Functions:
    get_docs() -> List[Tuple[str, dict]]
"""

from os import getenv
from typing import List, Tuple

from firebase_admin import initialize_app
from firebase_admin.credentials import Certificate
from firebase_admin.firestore import client


TRAINING_COLLECTION = "training"
ENV_KEY_PATH = "KEY_PATH"


def get_docs() -> List[Tuple[str, dict]]:
    """Return a list of tuples of (userId, chosenVideos by date)"""
    database_client = _get_client()
    docs = database_client.collection(TRAINING_COLLECTION).stream()
    return [(doc.id, doc.to_dict()) for doc in docs]


def _get_client() -> any:
    cred = Certificate(getenv(ENV_KEY_PATH))
    initialize_app(cred)
    return client()
