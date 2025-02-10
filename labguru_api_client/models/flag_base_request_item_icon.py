from enum import Enum


class FlagBaseRequestItemIcon(str, Enum):
    BELL = "bell"
    BELL_SLASH = "bell-slash"
    BOLT = "bolt"
    EXCLAMATION = "exclamation"
    FIRE = "fire"
    QUESTION = "question"
    STAR = "star"
    SUN = "sun"
    THUMBS_DOWN = "thumbs-down"
    THUMBS_UP = "thumbs-up"

    def __str__(self) -> str:
        return str(self.value)
