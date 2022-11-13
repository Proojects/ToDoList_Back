from flask.cli import FlaskGroup

from to_do_list import flask_app

manager = FlaskGroup(flask_app)

if(__name__ == '__main__'):
    manager()

