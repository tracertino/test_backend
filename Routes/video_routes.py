from flask import Blueprint
from Models.videos import Category, Subcategory, PageVideo, PageStars, PageBook
from flask import jsonify, request
from flask_jwt_extended import jwt_required

bp_video = Blueprint('video_bp', __name__)

#Получение видео
@bp_video.route('/<page>/<subcategory>/video', methods=["GET"])
def get_videos(page, subcategory):
    message, status = PageVideo.get_items(page, subcategory)
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

@bp_video.route('/<page>/<subcategory>/stars', methods=["GET"])
def get_stars(page, subcategory):
    message, status = PageStars.get_items(page, subcategory)
    return jsonify(message), status

@bp_video.route('/<page>/<subcategory>/book', methods=["GET"])
def get_books(page, subcategory):
    message, status = PageBook.get_items(page, subcategory)
    return jsonify(message), status