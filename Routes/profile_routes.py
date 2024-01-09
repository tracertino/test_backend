from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from Models.blacklist import TokenBlacklist
from Models.users import User
from werkzeug.security import generate_password_hash
from flask import g

bp_profile = Blueprint('profile_bp', __name__)

@bp_profile.route("/profile/registration", methods=["POST"])
def registration():
    # g.current_user
    username = request.json.get("email")
    password = request.json.get("password")
    password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    if username=="admin":
        return "False", 409
    message, status = User.add_user(username, password_hash)
    access_token = create_access_token(identity=username, additional_claims={"role": message.get("role")})
    message["accessToken"] = access_token
    return jsonify(message), status

@bp_profile.route("/profile/auth", methods=["POST"])
def login():
    username = request.json.get("email")
    password = request.json.get("password")
    # Проверка учетных данных и генерация токена доступа
    message, status  = User.user_is_auth(username, password)
    if status == 200:
        access_token = create_access_token(identity=username, additional_claims={"role": message.get("role")})
        message["accessToken"] = access_token
    return jsonify(message), status

# Маршрут для добавления токена в черный список
@bp_profile.route('/profile/logout', methods=['GET'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    TokenBlacklist.add_token(token=jti)
    return {"message":'Вы успешно вышли'}, 200

@bp_profile.route('/profile/update', methods=['PUT'])
@jwt_required()
def update_user():
    data = request.get_json()
    email = get_jwt_identity()
    message, status = User.update_profile(email=email, data=data)
    return jsonify(message), status

@bp_profile.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    email = get_jwt_identity()
    message, status = User.get_profile(email)
    return jsonify(message), status

@bp_profile.route("/role", methods=["GET"])
@jwt_required()
def get_role():
    role = get_jwt()['role']
    return jsonify({"role": role}), 200