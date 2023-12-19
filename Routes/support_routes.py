from flask import request, jsonify, Blueprint
from Models.support import Support

bp_support = Blueprint('support', __name__)

@bp_support.route("/support/get", methods=["GET"])
def get_support():
    message, status = Support.get_items()
    return jsonify(message), status
    
@bp_support.route("/support/add", methods=["GET"])
def add_support():
    question = request.args.get("question")
    answer = request.args.get("answer")
    if question and answer:
        message, status = Support.add_item(answer=answer, question=question)
        if status == 200:
            message, status = Support.get_items()
            return jsonify(message), status
        else:
            return jsonify(message), status
    else:
        return jsonify({"message": "Не все поля заполнены"}), 404
