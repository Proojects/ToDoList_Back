from to_do_list.plugins import db


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String())
    user_lastname = db.Column(db.String())
    user_email = db.Column(db.String())
    user_password = db.Column(db.String())
