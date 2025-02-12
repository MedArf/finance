import os
from flask import request, jsonify, send_file
from model.db_engine import get_db_engine
from api
from sqlalchemy.orm import Session

def setup_routes(app):
    @app.route("/")
    def home():
        return send_file(os.path.join(app.root_path, '../../..', 'frontend', 'index.html'))


    @app.route("/components/<path:path>")
    def static_files(path):
        print(path)
        return send_file(os.path.join(app.root_path, '../../..', 'frontend/components', path))
    @app.route("/api/entries")
    #eventually will call for api based on te user
    def get_entries():
        with Session(get_db_engine()) as session:
            return jsonify([entry.to_dict() for entry in entries])

   # @app.route('/components/<path:filename>')
  #  def static_files(filename):
 #       return send_file(os.path.join(app.root_path, '../../..', 'frontend', 'components', filename))
