from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)
CORS(app)

block_list_tokens = []

@app.route("/auth", methods=["POST"])
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

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    print(f"{username=} {password=}")
    if username=="admin":
        return "False", 409
    access_token = create_access_token(identity=username)
    return jsonify({"accessToken": access_token, "roles": "user"})

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    token = None
    jti = jwt_payload["jti"]
    print(f"{jti}")
    if jti in block_list_tokens:
        token = True
    # token = block_list_tokens.count(jti)
    return token is not None

@app.route("/logout", methods=["GET"])
# @jwt.token_in_blocklist_loader
@jwt_required()
def logout():
    # print(request.headers)
    user = get_jwt_identity()
    # print(jti) 
    token = get_jwt()["jti"]
    # print(user)
    block_list_tokens.append(token)
    print(block_list_tokens)
    return "True", 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}!"})

@app.route('/home', methods=('GET', 'POST'))
@jwt_required()
def diagnostic():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

