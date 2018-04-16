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


async def __get_almost_cured_modifier(wound_level: WoundLevel) -> Optional[int]:
    """
    Get modifier for almost cured wound.
    :param wound_level: Wound level.
    :return: Modifier or nothing if can do nothing.
    """
    index = WOUND_LEVELS_ORDERED.index(wound_level) - 1

    if index < 0 or index > len(WOUND_LEVELS_ORDERED):
        return 0

    return WOUND_MODIFIERS.get(WOUND_LEVELS_ORDERED[index], 0)


async def __get_wound_modifier(wounds: List[schema.Wound]) -> Optional[int]:
    """
    Get modifier for wounds.
    :param wounds: List of wounds.
    :return: Modifier or nothing if can do nothing.
    """
    final_modifier = 0

    for wound in wounds:
        modifier = await __get_almost_cured_modifier(wound.type) \
            if wound.almost_cured \
            else WOUND_MODIFIERS.get(wound.type, 0)

        if modifier is None:
            return None

        if modifier < final_modifier:
            final_modifier = modifier

    return final_modifier


async def get_roll_modifiers(username: str) -> schema.ModifiersSummary:
    """
    Fetch wounds and armor and return appropriate roll modifiers.
    :param username: Username.
    :return: Roll modifiers.
    """
    character = await database.get_character(username)

    summary = schema.ModifiersSummary()

    if not character:
        return summary

    if character.wounds:
        summary.wounds = await __get_wound_modifier(character.wounds)

    summary.armor = ARMOR_MODIFIERS.get(character.armor, 0)

    return summary
