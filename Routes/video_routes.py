from flask import Blueprint
from Models.videos import Category, Subcategory, Video
from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
# from app import db



# Category.add_item(session=session, name="Mission")

bp_video = Blueprint('video', __name__)
# db = SQLAlchemy(app)

@bp_video.route('/video/get', methods=["GET"])
def get_video():
    question = request.args.get("question")
    answer = request.args.get("answer")
    # if question and answer:
    #     Support.add_items_support(session=session, answer=answer, question=question)
        
    #     return jsonify({"message": "Данные добавлены"}), 200
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404
    
@bp_video.route('/video/add', methods=["GET"])
def add_video():
    category = request.args.get("category")
    subcategory = request.args.get("subcategory")
    title = request.args.get("title")

    # if category and subcategory and title:
    #     Video.add_item(session=session, answer=answer, question=question)
        
    #     return jsonify({"message": "Данные добавлены"}), 200
    # res = Support.get_items_support(session)
    # if res:
    #     return jsonify(res), 200
    # else:
    #     return jsonify({"message": "нет данных"}), 404