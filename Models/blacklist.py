# from flask_jwt_extended import get_raw_jwt
from flask_jwt_extended import get_jwt, jwt_manager
from app import jwt, db

# Модель для черного списка токенов
class TokenBlacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), unique=True, nullable=False)

# # Маршрут для добавления токена в черный список
# @app.route('/logout', methods=['DELETE'])
# @jwt_required()
# def logout():
#     jti = get_raw_jwt()['jti']
#     token = TokenBlacklist(jti=jti)
#     db.session.add(token)
#     db.session.commit()
#     return 'Вы успешно вышли'

blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

# Добавление токена в черный список
# def add_token_to_blacklist(token):
#     jti = get_raw_jwt(token)['jti']
#     blacklist.add(jti)