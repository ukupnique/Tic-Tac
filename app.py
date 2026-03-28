from flask import Flask
from di.container import Container
from web.route.game_route import register_routes


def create_app():

    app = Flask(__name__)

    container = Container()

    app_service = container.get_app_service()
    game_logic = container.get_game_logic()

    register_routes(app, app_service, game_logic)

    return app


if __name__ == "__main__":
    app = create_app
    app.run(debug=True, port=5000)
