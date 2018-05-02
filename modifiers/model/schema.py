import datetime
import enum
from typing import Optional

from pydantic import BaseModel


class WoundLevel(enum.Enum):
    SCRATCH = "scratch"
    LIGHT = "light"
    SEVERE = "severe"
    INCAPACITATED = "incapacitated"
    NEAR_DEATH = "near_death"


class ArmorType(enum.Enum):
    LIGHT = "light"
    MEDIUM = "medium"
    HEAVY = "heavy"


class Wound(BaseModel):
    id: Optional[str] = None
    username: str

    type: WoundLevel

    description: str = ""
    almost_cured: bool = False

    received: datetime.date
    valid_through: Optional[datetime.date] = None


class Armor(BaseModel):
    username: str
    type: Optional[ArmorType] = None


class CharacterSummary(BaseModel):
    wounds: int = 0
    armor: int = 0
