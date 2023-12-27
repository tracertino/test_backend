from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from Models.blacklist import TokenBlacklist
from Models.users import User
from flask import g

bp_profile = Blueprint('profile_bp', __name__)

@bp_profile.route("/profile/registration", methods=["POST"])
def registration():
    # g.current_user
    username = request.json.get("username")
    password = request.json.get("password")
    print(f"{username=} {password=}")
    if username=="admin":
        return "False", 409
    access_token = create_access_token(identity=username)
    return jsonify({"accessToken": access_token, "roles": "user"})

@bp_profile.route("/profile/auth", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    print(f"{username=} {password=}")
    # Проверка учетных данных и генерация токена доступа
    if username == "admin" and password == "123456Q":
        access_token = create_access_token(identity=username)
        print(access_token)
        return jsonify({"accessToken": access_token})

    return jsonify({"error": "Invalid credentials"}), 401


# Маршрут для добавления токена в черный список
@bp_profile.route('/profile/logout', methods=['GET'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    TokenBlacklist.add_token(token=jti)
    return {"message":'Вы успешно вышли'}, 200

@bp_profile.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return {"message":'Вы успешно вошли'}, 200