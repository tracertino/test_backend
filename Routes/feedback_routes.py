from flask import request, jsonify, Blueprint
from Models.feedback import Feedback

bp_feedback = Blueprint('feedback_bp', __name__)

@bp_feedback.route("/feedback/get", methods=["GET"])
def get_feedback():
    message, status = Feedback.get_items()
    return jsonify(message), status
    
    
@bp_feedback.route("/feedback/add", methods=["GET"])
def add_feedback():
    username = request.args.get("username")
    data = request.args.get("data")
    if username and data:
        message, status = Feedback.add_item(username=username, data=data)
        if status == 200:
            message, status = Feedback.get_items()
            return jsonify(message), status
        else:
            return jsonify(message), status
