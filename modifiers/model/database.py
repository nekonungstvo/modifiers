from typing import Optional

from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient

from modifiers.model import schema

client = AsyncIOMotorClient()
collection: AgnosticCollection = client.modifiers.collection
collection.create_index("username")


async def get_character(username: str) -> Optional[schema.Character]:
    data = await collection.find_one({"username": username})
    return schema.Character(**data) if data else None


async def save_character(character: schema.Character):
    await collection.update_one(
        {"username": character.username},
        {"$set": character.dict()},
        upsert=True
    )
