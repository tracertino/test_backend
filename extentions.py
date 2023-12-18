from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from app import jwt
# # Проверка, находится ли токен в черном списке
# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     jti = decrypted_token['jti']
#     return "TokenBlacklist.query.filter_by(jti=jti).first() is not None"