from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from flask_sqlalchemy import SQLAlchemy
from Routes.video_routes import bp_video
from Routes.feedback_routes import bp_feedback
from Routes.profile_routes import bp_profile
from Routes.support_routes import bp_support



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "kniga_code"
jwt = JWTManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(bp_feedback)
app.register_blueprint(bp_support)
app.register_blueprint(bp_profile)
app.register_blueprint(bp_video)
CORS(app)

# @app.route('/video/get', methods=["GET"])
# def get_video():
#     category = request.args.get("category")
#     subcategory = request.args.get("subcategory")
#     title = request.args.get("title")
#     description = request.args.get("description")
#     URL = request.args.get("URL")
#     role = request.args.get("role")
    # if question and answer:
    #     Support.add_items_support(session=session, answer=answer, question=question)
        
    #     return jsonify({"message": "Данные добавлены"}), 200
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404

# @app.route('/video/category/add', methods=["GET"])
# def add_category():
#     category = request.args.get("category")
#     if category:
#         message, status = Category.add_item(session=session, name=category)  
#         return jsonify(message), status
    
# @app.route('/video/subcategory/get', methods=["GET"])
# def get_subcategory():
#         category = request.args.get("category")
#         message, status = Subcategory.get_item(session=session, category=category)  
#         return message, status
    
# @app.route('/video/subcategory/add', methods=["GET"])
# def add_subcategory():
#     category = request.args.get("category")
#     subcategory = request.args.get("subcategory")
#     if category:
#         message, status = Subcategory.add_item(session=session, category=category, name=subcategory)  
#         return jsonify(message), status
    
# @app.route('/video/add', methods=["GET"])
# def add_video():
#     category = request.args.get("category")
#     subcategory = request.args.get("subcategory")
#     title = request.args.get("title")
#     description = request.args.get("description")
#     URL = request.args.get("URL")
#     role = request.args.get("role")

#     if category and subcategory and title and role and URL:
#         message, status = Video.add_item(session=session, subcategory=subcategory, title=title,
#                              description=description, URL=URL, role=role)
        
#         return jsonify(message), status
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404


# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify({"message": f"Hello, {current_user}!"})

# @app.route('/home', methods=('GET', 'POST'))
# @jwt_required()
# def diagnostic():
#     return "OK", 200

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=80)

