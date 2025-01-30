from flask import Flask
from app.routes import setup_routes
from flask_admin import Admin
from model.db_engine import get_db_engine
from model.init_data import init_db
from sqlalchemy.orm import Session


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'g2o4gifn32ogrvsecret'
db_engine=get_db_engine()
admin=Admin(app)
session=Session(db_engine)

def init_admin():
    admin.add_view(ModelView(User, session))

setup_routes(app)

def get_app():
    return app

def main():
    init_admin()
    init_db()

