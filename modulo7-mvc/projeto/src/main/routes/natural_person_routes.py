# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,R0801
from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.natural_person_creator_composer import natural_person_creator_composer
from src.main.composer.natural_person_lister_composer import natural_person_lister_composer
from src.main.composer.natural_person_statement_composer import natural_person_statement_composer
from src.main.composer.natural_person_withdraw_composer import natural_person_withdraw_composer
from src.errors.error_handle import handle_errors

natural_person_route_bp = Blueprint("natural_person_routes", __name__)

@natural_person_route_bp.route("/natural_person/create", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = natural_person_creator_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@natural_person_route_bp.route("/natural_person/list", methods=["GET"])
def list_persons():
    try:
        http_request = HttpRequest()
        view = natural_person_lister_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@natural_person_route_bp.route("/natural_person/statement/<person_id>", methods=["GET"])
def get_statement(person_id):
    try:
        http_request = HttpRequest(param={"person_id": person_id})
        view = natural_person_statement_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@natural_person_route_bp.route("/natural_person/withdraw", methods=["PUT"])
def withdraw_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = natural_person_withdraw_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code