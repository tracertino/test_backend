from flask import request, jsonify, Blueprint
from Models.babyNames import BabyNames
from Models.babyLastnames import BabyLastnames
from Utils.raschet_tlk_sovmestimost import raschet_tlk_fio, raschet
from flask_jwt_extended import jwt_required, get_jwt

bp_calculation = Blueprint('calculation_bp', __name__)

@bp_calculation.route("/calculation", methods=["POST"])
@jwt_required()
def calculation():
    name = request.json.get("name")
    familyname = request.json.get('familyname')
    lastname = request.json.get('lastname')
    day = request.json.get("birthday")
    month = request.json.get('month')
    year = request.json.get('year')
    if name and familyname and lastname and \
        day and month and year:
        birthday = f"{day}{month}{year}"
        result = raschet(f"{name}{familyname}{lastname}", birthday)
        return jsonify(result), 200
    else: 
        return jsonify({"message": "Введены не все данные"}), 500


#Подбор имени или отчества
@bp_calculation.route("/calculation/selection", methods=["POST"])
@jwt_required()
def selection_name():
    gender = request.json.get("gender")
    mission = int(request.json.get('mission'))
    familyname = request.json.get('familyname')
    data = request.json.get("data")
    option = request.json.get('option')
    if gender and mission and familyname and data and option:
        message = []
        if option == 'name':
            names, status = BabyNames.get_items(gender=gender)
            if status == 200:
                for name in names:
                    res = raschet_tlk_fio(f'{familyname}{data}{name}', mission)
                    if res:
                        message.append({"value": f'{name} {res}'})
                return jsonify(message), status
            else:
                return jsonify(names), status
        else:
            lastnames, status = BabyLastnames.get_items(gender=gender)
            if status == 200:
                for lastname in lastnames:
                    res = raschet_tlk_fio(f'{familyname}{lastname}{data}', mission)
                    if res:
                        message.append({"value": f'{lastname} {res}'})
                return jsonify(message), status
            else:
                return jsonify(lastnames), status  
                  
    else:
        return jsonify({"message": "Не все поля заполнены"}), 500
