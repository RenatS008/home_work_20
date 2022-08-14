from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from application.views.director import director_ns
from application.views.genre import genre_ns
from application.views.movie import movie_ns
from application.views.user import user_ns
from application.views.auth import auth_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())


if __name__ == '__main__':
    app.run(debug=False)