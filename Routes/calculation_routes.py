from flask import request, jsonify, Blueprint
from Models.calculation import Calculation
from Models.babyNames import BabyNames
from Models.babyLastnames import BabyLastnames
from Utils.raschet_tlk_sovmestimost import raschet_tlk_fio

bp_calculation = Blueprint('calculation_bp', __name__)

@bp_calculation.route("/calculation/selection", methods=["POST"])
def selection_name():
    print(request.json)
    gender = request.json.get("gender")
    mission = int(request.json.get('mission'))
    familyname = request.json.get('familyname')
    data = request.json.get("data")
    option = request.json.get('option')
    if gender and mission and familyname and data and option:
        if option == 'name':
            names, status = BabyNames.get_items(gender=gender)
            if status == 200:
                message = [{"value": name} for name in names if raschet_tlk_fio(f'{familyname}{data}{name}', mission)]
                return jsonify(message), status
            else:
                return jsonify(names), status
        else:
            lastnames, status = BabyLastnames.get_items(gender=gender)
            if status == 200:
                message = [{"value": lastname} for lastname in lastnames if raschet_tlk_fio(f'{familyname}{lastname}{data}', mission)]
                return jsonify(message), status
            else:
                return jsonify(lastnames), status  
                  
    else:
        return jsonify({"message": "Не все поля заполнены"}), 500
