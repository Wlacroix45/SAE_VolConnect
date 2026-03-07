from flask import Flask
from .extensions import api, db
from .views import ns

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
api.init_app(app)
db.init_app(app)
api.add_namespace(ns)