from decouple import config


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}/{}".format(
        config("DATABASE_USER"),
        config("DATABASE_PASSWORD"),
        config("DB_HOST"),
        config("DATABASE_NAME"),
    )
