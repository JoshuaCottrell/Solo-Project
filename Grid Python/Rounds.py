from enum import Enum

class Rounds(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    NO_TRUMP = 8
    BLIND = 9

    def __str__(self):
        if self.value <= 7:
            return f"{self.name.title()}"
        elif self.value == 8:
            return "No Trump"
        else:
            return "Blind"