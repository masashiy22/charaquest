from .player import *
from .boss import *

__all__ = [
    "character_init"
]


def character_init():
    characters = {
        "player": Player(),
        "boss": Boss()
    }

    return characters
