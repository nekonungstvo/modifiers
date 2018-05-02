from aiohttp import web

from modifiers.aiohttp_controller import serialization
from modifiers.model import model, database


async def fetch_wounds(request):
    login = request.match_info.get('login')

    wounds = await database.get_wounds(login)

    return web.json_response(wounds, dumps=serialization.dumps)


async def fetch_modifiers(request):
    login = request.match_info.get('login')
    summary = await model.get_roll_modifiers(login)
    return web.json_response(summary, dumps=serialization.dumps)


character_app = web.Application()
character_app.router.add_get('/{login}/wounds', fetch_wounds)
character_app.router.add_get('/{login}/modifiers', fetch_modifiers)
