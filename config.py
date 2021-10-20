import os

app_dir = os.path.abspath(os.path.dirname(__file__)).replace('\\', "/")


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supEveJkeR'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{app_dir}/base.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
