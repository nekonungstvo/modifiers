import os
from typing import Optional, List

import pymongo
from bson import ObjectId
from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient

from modifiers.model import schema

__collection = None

MONGO_HOST = "modifiers-mongo" if os.getenv("IS_PROD", "0") != "0" else "127.0.0.1"


async def get_db(collection: str) -> AgnosticCollection:
    global __collection
    if not __collection:
        client = AsyncIOMotorClient(MONGO_HOST)
        __collection = client.modifiers[collection]
        __collection.create_index("username")
    return __collection


async def get_character(username: str) -> Optional[schema.Armor]:
    collection = await get_db("armor")
    data = await collection.find_one({"username": username})
    return schema.Armor(**data) if data else None


async def save_character(character: schema.Armor):
    collection = await get_db("armor")
    await collection.update_one(
        {"username": character.username},
        {"$set": character.dict()},
        upsert=True
    )


async def get_wounds(username: str) -> List[schema.Wound]:
    collection = await get_db("wounds")

    result = collection \
        .find({"username": username}) \
        .sort("_id", pymongo.DESCENDING)

    return [
        schema.Wound(
            id=str(data["_id"]),
            **data
        )
        async for data in result
    ]


async def get_wound(wound_id: str) -> Optional[schema.Wound]:
    if not ObjectId.is_valid(wound_id):
        return None

    collection = await get_db("wounds")
    data = await collection.find_one({"_id": ObjectId(wound_id)})
    return schema.Wound(
        id=str(data["_id"]),
        **data
    ) if data else None


async def save_wound(wound: schema.Wound) -> None:
    collection = await get_db("wounds")
    await collection.update_one(
        {"_id": ObjectId(wound.id)},
        {"$set": wound.dict(exclude={"id"})},
        upsert=True
    )
