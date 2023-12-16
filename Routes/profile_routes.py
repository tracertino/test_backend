from flask import request, jsonify, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt


bp_profile = Blueprint('profile', __name__)

block_list_tokens = []

jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    token = None
    jti = jwt_payload["jti"]
    # print(f"{jti}")
    if jti in block_list_tokens:
        token = True
    # token = block_list_tokens.count(jti)
    return token is not None



@bp_profile.route("/profile/registration", methods=["POST"])
def registration():
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

@bp_profile.route("/profile/logout", methods=["GET"])
# @jwt.token_in_blocklist_loader
@jwt_required()
def logout():
    # print(request.headers)
    user = get_jwt_identity()
    # print(jti) 
    token = get_jwt()["jti"]
    # print(user)
    block_list_tokens.append(token)
    # print(block_list_tokens)
    return "True", 200