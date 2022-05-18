from keras import Input
from keras.layers import Embedding


def run() -> None:
    title_input = Input(shape=(None,), name="title")
    description_input = Input(shape=(None,), name="description")
    channel_input = Input(shape=(None,), name="channel")
    tags_input = Input(shape=(None,), name="tags")
    category_input = Input(shape=(None,), name="category")
    language_input = Input(shape=(None,), name="language")
    age_input = Input(shape=(1,), name="age")
    duration_input = Input(shape=(1,), name="duration")
