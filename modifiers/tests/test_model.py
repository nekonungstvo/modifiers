import pytest

from modifiers.model import model
from modifiers.model import schema
from modifiers.model.schema import WoundLevel


@pytest.mark.asyncio
async def test_wound_almost_cured():
    assert await model.__get_almost_cured_modifier(WoundLevel.SCRATCH) == 0
    assert await model.__get_almost_cured_modifier(WoundLevel.LIGHT) == 0
    assert await model.__get_almost_cured_modifier(WoundLevel.SEVERE) == -1
    assert await model.__get_almost_cured_modifier(WoundLevel.INCAPACITATED) == -2
    assert await model.__get_almost_cured_modifier(WoundLevel.NEAR_DEATH) is None


@pytest.mark.asyncio
async def test_wounds():
    assert await model.__get_wound_modifier([
        schema.Wound(
            id="id1",
            username="somebody",
            type=WoundLevel.SEVERE
        ),
        schema.Wound(
            id="id2",
            username="somebody",
            type=WoundLevel.LIGHT
        ),
    ]) == -2

    assert await model.__get_wound_modifier([
        schema.Wound(
            id="id1",
            username="somebody",
            type=WoundLevel.SEVERE,
            almost_cured=True
        ),
        schema.Wound(
            id="id2",
            username="somebody",
            type=WoundLevel.LIGHT
        ),
    ]) == -1

    assert await model.__get_wound_modifier([
        schema.Wound(
            id="id1",
            username="somebody",
            type=WoundLevel.NEAR_DEATH,
            almost_cured=True
        )
    ]) is None
