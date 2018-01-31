from aiohttp import web

from modifiers.model import database, model
from modifiers.model.schema import Character


async def fetch_player(request):
    login = request.match_info.get('login')

    character = await database.get_character(login)

    if not character:
        character = Character(username=login)

    return web.json_response(character.dict())


async def fetch_modifiers(request):
    login = request.match_info.get('login')
    summary = await model.get_roll_modifiers(login)
    return web.json_response(summary.dict())


async def update_modifier(request: web.Request):
    data = await request.json()
    character = Character(**data)

    await database.save_character(character)

    return web.json_response({
        "status: ""ok"
    })


app = web.Application()
app.router.add_get('/fetch/{login}', fetch_player)
app.router.add_get('/fetch/{login}/modifiers', fetch_modifiers)
app.router.add_post('/update', update_modifier)

web.run_app(app, host="127.0.0.1")
