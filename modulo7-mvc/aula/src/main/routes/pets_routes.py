# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from flask import Blueprint, jsonify

pet_route_bp = Blueprint("pets_routes", __name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"message": "Teste retorno"}), 200