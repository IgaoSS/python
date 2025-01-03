from flask import Blueprint, jsonify, request

# Nomear todas as rotas de calculadoras associadas a esse nome
calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    print(request)
    return jsonify({"success": True}), 200