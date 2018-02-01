from typing import Optional

from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient

from modifiers.model import schema

__collection = None


async def get_db() -> AgnosticCollection:
    global __collection
    if not __collection:
        client = AsyncIOMotorClient()
        __collection = client.modifiers.collection
        __collection.create_index("username")
    return __collection


async def get_character(username: str) -> Optional[schema.Character]:
    collection = await get_db()
    data = await collection.find_one({"username": username})
    return schema.Character(**data) if data else None


async def save_character(character: schema.Character):
    collection = await get_db()
    await collection.update_one(
        {"username": character.username},
        {"$set": character.dict()},
        upsert=True
    )
