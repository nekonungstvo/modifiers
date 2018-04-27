from aiohttp import web

from modifiers.aiohttp_controller.v1.app import v1_app
from modifiers.model.database import init_db

app = web.Application()
app.add_subapp("/v1", v1_app)


def run():
    init_db()
    web.run_app(app, port=8080)


if __name__ == "__main__":
    run()
