# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,R0801
from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.juridic_person_creator_composer import juridic_person_creator_composer
from src.main.composer.juridic_person_lister_composer import juridic_person_lister_composer
from src.main.composer.juridic_person_statement_composer import juridic_person_statement_composer
from src.main.composer.juridic_person_withdraw_composer import juridic_person_withdraw_composer

juridic_person_route_bp = Blueprint("juridic_person_routes", __name__)

@juridic_person_route_bp.route("/juridic_person/create", methods=["POST"])
def create_person():
    http_request = HttpRequest(body=request.json)
    view = juridic_person_creator_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@juridic_person_route_bp.route("/juridic_person/list", methods=["GET"])
def list_persons():
    http_request = HttpRequest()
    view = juridic_person_lister_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@juridic_person_route_bp.route("/juridic_person/statement/<person_id>", methods=["GET"])
def get_statement(person_id):
    http_request = HttpRequest(param={"person_id": person_id})
    view = juridic_person_statement_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@juridic_person_route_bp.route("/juridic_person/withdraw", methods=["PUT"])
def withdraw_person():
    http_request = HttpRequest(body=request.json)
    view = juridic_person_withdraw_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code