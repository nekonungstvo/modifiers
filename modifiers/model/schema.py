import enum
from typing import Optional

from pydantic import BaseModel


class WoundLevel(enum.IntEnum):
    SCRATCH = 0
    LIGHT = 1
    SEVERE = 2
    INCAPACITATED = 3
    NEAR_DEATH = 4


class ArmorType(enum.IntEnum):
    LIGHT = 0
    MEDIUM = 1
    HEAVY = 2


class Wound(BaseModel):
    id: Optional[str] = None
    username: str

    type: WoundLevel

    description: str = ""
    almost_cured: bool = False


class Armor(BaseModel):
    username: str
    type: Optional[ArmorType] = None


class CharacterSummary(BaseModel):
    wounds: int = 0
    armor: int = 0
