from typing import List, Optional

from modifiers.model import schema, database
from modifiers.model.schema import WoundLevel, ArmorType

WOUND_MODIFIERS = {
    WoundLevel.SCRATCH: 0,
    WoundLevel.LIGHT: -1,
    WoundLevel.SEVERE: -2,
    WoundLevel.INCAPACITATED: None,
    WoundLevel.NEAR_DEATH: None
}

WOUND_LEVELS_ORDERED = list(WOUND_MODIFIERS.keys())

ARMOR_MODIFIERS = {
    ArmorType.LIGHT: 0,
    ArmorType.MEDIUM: -1,
    ArmorType.HEAVY: -2
}


async def __get_wound_almost_cured(wound_level: WoundLevel) -> Optional[int]:
    index = WOUND_LEVELS_ORDERED.index(wound_level) - 1

    if index < 0 or index > len(WOUND_LEVELS_ORDERED):
        return 0

    return WOUND_MODIFIERS.get(WOUND_LEVELS_ORDERED[index], 0)


async def __get_wound_modifiers(wounds: List[schema.Wound]) -> Optional[int]:
    final_modifier = 0

    for wound in wounds:
        modifier = await __get_wound_almost_cured(wound.type) \
            if wound.almost_cured \
            else WOUND_MODIFIERS.get(wound.type, 0)

        if modifier is None:
            return None

        if modifier < final_modifier:
            final_modifier = modifier

    return final_modifier


async def get_roll_modifiers(username: str) -> schema.ModifiersSummary:
    character = await database.get_character(username)

    summary = schema.ModifiersSummary()

    if not character:
        return summary

    if character.wounds:
        summary.wounds = await __get_wound_modifiers(character.wounds)

    summary.armor = ARMOR_MODIFIERS.get(character.armor, 0)

    return summary
