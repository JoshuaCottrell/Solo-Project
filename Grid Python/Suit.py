from enum import Enum

class Suit(Enum):
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3
    HEARTS = 4

    def __str__(self):
        return f"{self.name.title()}"