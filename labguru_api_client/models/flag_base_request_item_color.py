from enum import Enum


class FlagBaseRequestItemColor(str, Enum):
    BLUE = "blue"
    BLUE_DARK = "blue-dark"
    BLUE_LIGHT = "blue-light"
    GREEN = "green"
    GREEN_DARK = "green-dark"
    GREEN_LIGHT = "green-light"
    GREY = "grey"
    GREY_DARK = "grey-dark"
    GREY_LIGHT = "grey-light"
    ORANGE = "orange"
    ORANGE_DARK = "orange-dark"
    ORANGE_LIGHT = "orange-light"
    RED = "red"
    RED_DARK = "red-dark"
    RED_LIGHT = "red-light"

    def __str__(self) -> str:
        return str(self.value)
