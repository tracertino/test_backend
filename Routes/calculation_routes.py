from flask import request, jsonify, Blueprint
from Models.calculation import Calculation

bp_calculation = Blueprint('calculation', __name__)