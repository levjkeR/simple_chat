from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

login_manager = LoginManager(app)


socketio = SocketIO(app, ping_interval=5, ping_timeout=5)

db = SQLAlchemy(app)

from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from .router import router as router_blueprint

app.register_blueprint(router_blueprint)

from .model import User, Anonymous
login_manager.anonymous_user = Anonymous



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from . import chat