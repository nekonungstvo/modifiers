import pytest

from modifiers.model import model
from modifiers.model import schema
from modifiers.model.schema import WoundLevel


@pytest.mark.asyncio
async def test_wound_almost_cured():
    assert await model.__get_wound_almost_cured(WoundLevel.SCRATCH) == 0
    assert await model.__get_wound_almost_cured(WoundLevel.LIGHT) == 0
    assert await model.__get_wound_almost_cured(WoundLevel.SEVERE) == -1
    assert await model.__get_wound_almost_cured(WoundLevel.INCAPACITATED) == -2
    assert await model.__get_wound_almost_cured(WoundLevel.NEAR_DEATH) is None


@pytest.mark.asyncio
async def test_wounds():
    assert await model.__get_wound_modifiers([
        schema.Wound(
            type=WoundLevel.SEVERE
        ),
        schema.Wound(
            type=WoundLevel.LIGHT
        ),
    ]) == -2

    assert await model.__get_wound_modifiers([
        schema.Wound(
            type=WoundLevel.SEVERE,
            almost_cured=True
        ),
        schema.Wound(
            type=WoundLevel.LIGHT
        ),
    ]) == -1

    assert await model.__get_wound_modifiers([
        schema.Wound(
            type=WoundLevel.NEAR_DEATH,
            almost_cured=True
        )
    ]) is None
