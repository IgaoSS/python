# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler
from src.main.routes.pets_routes import pet_route_bp # Importar blueprints

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp)