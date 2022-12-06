from flask.cli import FlaskGroup
from flask_migrate import Migrate

from to_do_list import flask_app
from to_do_list.plugins import db
from to_do_list.user.domain.respostories import UserModel

manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


if (__name__ == '__main__'):
    with flask_app.app_context():
        db.create_all()
    manager()
