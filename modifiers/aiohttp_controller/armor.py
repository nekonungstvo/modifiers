from aiohttp import web

from modifiers.aiohttp_controller import serialization
from modifiers.model import database
from modifiers.model.schema import Armor


async def fetch_character(request):
    login = request.match_info.get('login')

    character = await database.get_armor(login)

    if not character:
        character = Armor(username=login)

    return web.json_response(character, dumps=serialization.dumps)


async def update_character(request: web.Request):
    login = request.match_info.get('login')

    data = await request.json()
    character = Armor(username=login, **data)

    await database.save_armor(character)

    return web.json_response({
        "status": "ok"
    })


armor_app = web.Application()
armor_app.router.add_get('/{login}/fetch', fetch_character)
armor_app.router.add_post('/{login}/update', update_character)
