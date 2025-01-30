import os
from flask import request, jsonify, send_file
from model.models import Booking
from model.db_engine import get_db_engine
from sqlalchemy.orm import Session


def setup_routes(app):
    @app.route("/")
    def home():
        return send_file(os.path.join(app.root_path, '../../..', 'frontend', 'index.html'))

    @app.route('/components/<path:filename>')
    def static_files(filename):
        return send_file(os.path.join(app.root_path, '../../..', 'frontend', 'components', filename))
