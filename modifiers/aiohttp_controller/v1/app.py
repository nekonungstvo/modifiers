from aiohttp import web

from modifiers.aiohttp_controller.v1.armor import armor_app
from modifiers.aiohttp_controller.v1.character import character_app
from modifiers.aiohttp_controller.v1.wound import wound_app

v1_app = web.Application()
v1_app.add_subapp("/character", character_app)
v1_app.add_subapp("/armor", armor_app)
v1_app.add_subapp("/wound", wound_app)
