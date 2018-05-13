import datetime
import enum
from typing import Optional

from pydantic import BaseModel, validator


class WoundLevel(enum.Enum):
    SCRATCH = 0
    LIGHT = 1
    SEVERE = 2
    INCAPACITATED = 3
    NEAR_DEATH = 4


class ArmorType(enum.Enum):
    LIGHT = 0
    MEDIUM = 1
    HEAVY = 2


class Wound(BaseModel):
    id: Optional[str] = None
    username: str

    type: WoundLevel

    description: str = ""
    almost_cured: bool = False

    created_at: datetime.date
    expire_at: Optional[datetime.date] = None

    @validator("created_at", pre=True, always=True)
    def set_created_at_today(cls, created_at):
        return created_at or datetime.date.today()


class Armor(BaseModel):
    username: str
    type: Optional[ArmorType] = None


class CharacterSummary(BaseModel):
    wounds: int = 0
    armor: int = 0
