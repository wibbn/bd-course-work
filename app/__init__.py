import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

print(__name__)
app = Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate()

migrate.init_app(app, db)

lm = LoginManager()
lm.init_app(app)

from app.models import *
from app.routes import *

db.create_all()

if __name__ == '__main__':
    app.run()
