from aiohttp import web

from modifiers.aiohttp_controller.armor import armor_app
from modifiers.aiohttp_controller.character import character_app
from modifiers.aiohttp_controller.wound import wound_app

app = web.Application()
app.add_subapp("/character", character_app)
app.add_subapp("/armor", armor_app)
app.add_subapp("/wound", wound_app)


def run():
    web.run_app(app, port=8080)


if __name__ == "__main__":
    run()
