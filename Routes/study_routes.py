from flask import request, jsonify, Blueprint
from Models.study import Study

bp_study = Blueprint('study_bp', __name__)

@bp_study.route("/study/get", methods=["GET"])
def get_consultation():
    level = request.args.get("level")
    message, status = Study.get_items(level=level)
    return jsonify(message), status