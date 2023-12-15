from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from Models.users import Users
from Models.support import Support
from Models.feedback import Feedback
from Models.videos import Category, Subcategory, Video
from sqlalchemy.orm import sessionmaker
from Routes.video_routes import bp_video



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# app.register_blueprint(bp_video)
CORS(app)

block_list_tokens = []
# Создание сессии SQLAlchemy
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблиц на основе объявленных моделей
Users.metadata.create_all(engine)
Support.metadata.create_all(engine)
Feedback.metadata.create_all(engine)
Video.metadata.create_all(engine)

Category.add_item(session=session, name="Mission")

@app.route('/video/get', methods=["GET"])
def get_video():
    category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    title = request.args.get("title")
    description = request.args.get("description")
    URL = request.args.get("URL")
    role = request.args.get("role")
    # if question and answer:
    #     Support.add_items_support(session=session, answer=answer, question=question)
        
    #     return jsonify({"message": "Данные добавлены"}), 200
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404

@app.route('/video/category/add', methods=["GET"])
def add_category():
    category = request.args.get("category")
    if category:
        message, status = Category.add_item(session=session, name=category)  
        return jsonify(message), status
    
@app.route('/video/subcategory/get', methods=["GET"])
def get_subcategory():
        category = request.args.get("category")
        message, status = Subcategory.get_item(session=session, category=category)  
        return message, status
    
@app.route('/video/subcategory/add', methods=["GET"])
def add_subcategory():
    category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    if category:
        message, status = Subcategory.add_item(session=session, category=category, name=subcategory)  
        return jsonify(message), status
    
@app.route('/video/add', methods=["GET"])
def add_video():
    category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    title = request.args.get("title")
    description = request.args.get("description")
    URL = request.args.get("URL")
    role = request.args.get("role")

    if category and subcategory and title and role and URL:
        message, status = Video.add_item(session=session, subcategory=subcategory, title=title,
                             description=description, URL=URL, role=role)
        
        return jsonify(message), status
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404
    
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


@app.route("/support", methods=["GET"])
def support():
    question = request.args.get("question")
    answer = request.args.get("answer")
    if question and answer:
        Support.add_items_support(session=session, answer=answer, question=question)
        
        return jsonify({"message": "Данные добавлены"}), 200
    res = Support.get_items_support(session)
    if res:
        return jsonify(res), 200
    else:
        return jsonify({"message": "нет данных"}), 404 
    
@app.route("/feedback", methods=["GET"])
def feedback():
    username = request.args.get("username")
    data = request.args.get("data")
    if username and data:
        Feedback.add_item(session=session, username=username, data=data)
        return jsonify({"message": "Данные добавлены"}), 200
    res = Feedback.get_items(session)
    if res:
        return jsonify(res), 200
    else:
        return jsonify({"message": "нет данных"}), 404
    
@app.route("/feedback/add", methods=["GET"])
@jwt_required()
def feedback_add():
    username = request.args.get("username")
    data = request.args.get("data")
    if username and data:
        Feedback.add_item(session=session, username=username, data=data)
        return jsonify({"message": "Данные добавлены"}), 200
    else:
        return jsonify({"message": "не все поля заполнены"}), 404


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
    # print(f"{jti}")
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
    # print(block_list_tokens)
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

