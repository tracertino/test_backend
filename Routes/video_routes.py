from flask import Blueprint
from Models.videos import Category, Subcategory, Video
from flask import jsonify, request
from flask_jwt_extended import jwt_required

bp_video = Blueprint('video_bp', __name__)

# @bp_video.route('/video/get', methods=["GET"])
# def get_video():
#     question = request.args.get("question")
#     answer = request.args.get("answer")
    # if question and answer:
    #     Support.add_items_support(session=session, answer=answer, question=question)
        
    #     return jsonify({"message": "Данные добавлены"}), 200
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404
    
@bp_video.route('/video/add', methods=["GET"])
# @jwt_required()
def add_video():
    # category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    title = request.args.get("title")
    description = request.args.get("description")
    URL = request.args.get("URL")
    role = request.args.get("role")
    message, status = Video.add_item(subcategory=subcategory, title=title, description=description,
                                     URL=URL, role=role)
    return jsonify(message), status

@bp_video.route('/video/get', methods=["GET"])
def get_videos():
    # category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    message, status = Video.get_items(subcategory)
    return jsonify(message), status
    
@bp_video.route('/video/category/add', methods=["GET"])
def add_category():
    category = request.args.get("category")
    message, status = Category.add_item(category)
    return jsonify(message), status    

@bp_video.route('/video/category/get', methods=["GET"])
def get_categories():
    # category = request.args.get("category")
    # subcategory = request.args.get("subcategory")
    message, status = Category.get_items()
    return jsonify(message), status

@bp_video.route('/video/category/del', methods=["GET"])
def delete_category():
    category = request.args.get("category")
    message, status = Category.delete_item(category)
    return jsonify(message), status

@bp_video.route('/video/category/subcategory/add', methods=["GET"])
def add_subcategory():
    category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    message, status = Subcategory.add_item(category=category, subcategory=subcategory)
    return jsonify(message), status

@bp_video.route('/video/category/subcategory/get', methods=["GET"])
def get_subcategories():
    category = request.args.get("category")
    # subcategory = request.args.get("subcategory")
    message, status = Subcategory.get_items(category=category)
    return jsonify(message), status