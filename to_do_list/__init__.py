from flask import Flask


def create_app(config_class: str):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)
    return flask_app


def register_plugins(flask_app):
    from .plugins import db
    db.init_app(flask_app)


def configure_app(config_class):
    flask_app = create_app(config_class)
    register_plugins(flask_app)
    return flask_app


flask_app = configure_app('to_do_list.settings.Config')
