import enum
from typing import List, Optional

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
    type: WoundLevel
    description: str = ""

    almost_cured: bool = False


class Character(BaseModel):
    username: str
    armor: Optional[ArmorType] = None
    wounds: List[Wound] = []


class ModifiersSummary(BaseModel):
    wounds: int = 0
    armor: int = 0
