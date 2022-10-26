from flask import Blueprint, request, jsonify
from models import RequestParams, BatchRequestParams
from marshmallow import ValidationError
from builder import build_query

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 404

    resoult = None
    for query in params["queries"]:
        result = build_query(cmd=query["cmd"], param=query["value"], data=resoult)

    return jsonify(resoult)
