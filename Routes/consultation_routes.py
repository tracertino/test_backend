from flask import request, jsonify, Blueprint
from Models.consultation import Consultation

bp_consultation = Blueprint('consultation_bp', __name__)

@bp_consultation.route("/consultation/get", methods=["GET"])
def get_consultation():
    level = request.args.get("level")
    message, status = Consultation.get_items(level=level)
    return jsonify(message), status