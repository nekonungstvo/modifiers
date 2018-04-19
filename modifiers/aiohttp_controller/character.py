from aiohttp import web

from modifiers.model import database, model


async def fetch_wounds(request):
    login = request.match_info.get('login')

    wounds = await database.get_wounds(login)

    return web.json_response([
        wound.dict()
        for wound in wounds
    ])


async def fetch_modifiers(request):
    login = request.match_info.get('login')
    summary = await model.get_roll_modifiers(login)
    return web.json_response(summary.dict())


character_app = web.Application()
character_app.router.add_get('/{login}/wounds', fetch_wounds)
character_app.router.add_get('/{login}/modifiers', fetch_modifiers)
