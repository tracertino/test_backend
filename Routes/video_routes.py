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

#Получение видео
@bp_video.route('/<page>/<subcategory>/video_get', methods=["GET"])
def get_videos(page, subcategory):
    message, status = Video.get_items(page, subcategory)
    return jsonify(message), status

#Получение категорий 
@bp_video.route('/<page>/category/get', methods=["GET"])
def get_categories(page):
    message, status = Category.get_items(page)
    return jsonify(message), status

#Получение подкатегорий 
@bp_video.route('/<page>/<category>/subcategory/get', methods=["GET"])
def get_subcategories(page, category):
    message, status = Subcategory.get_items(page, category)
    return jsonify(message), status