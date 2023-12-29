from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from Utils.middleware import jwt
from Utils import basic_auth
from Routes.profile_routes import bp_profile
from Routes.feedback_routes import bp_feedback
from Routes.support_routes import bp_support
from Routes.video_routes import bp_video
from Routes.calculation_routes import bp_calculation
from Routes.consultation_routes import bp_consultation
from Routes.study_routes import bp_study
from Models import db
from Utils.admin_panel import admin
from flask_jwt_extended import JWTManager





app = Flask(__name__)
app.secret_key = 'ваш_секретный_ключ_здесь'
app.config["JWT_SECRET_KEY"] = "kniga_code"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASIC_AUTH_REALM'] = 'Login required'
app.config['JWT_BLOCKLIST_ENABLED'] = True


db.init_app(app)
basic_auth.init_app(app)
migrate = Migrate(app, db)

table_name = {
    "alembic_version",
    "category",
    "calculation",
    "feedback",
    "subcategory",
    "support",
    "token_blacklist",
    "user",
    "videos",
    "role",
    "level",
    "consultation",
    "study",
    "page"
}

with app.app_context():
    inspector = db.inspect(db.engine)
    table_names = set(inspector.get_table_names())
    if not table_name.issubset(table_names):
        db.create_all()
    
    admin.init_app(app)
# from flask_jwt_extended import jwt_required
# jwt = JWTManager(app)

# @jwt.token_in_blocklist_loader
# def check_if_token_in_blocklist(jwt_header, jwt_payload):
#     # Проверяем, находится ли маркер в черном списке базы данных
#     token = jwt_header + '.' + jwt_payload
#     print(token)
#     return 2

# @app.route('/profile')
# @jwt_required()
# def protected():
#     return 1

# from Models.blacklist import TokenBlacklist
# jwt = JWTManager(app)

# @jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
#     jti = jwt_payload["jti"]
#     print(jti)
#     token = TokenBlacklist.find_token(token=jti)
    
#     return token is not None        


    
app.register_blueprint(bp_feedback)
app.register_blueprint(bp_support)
app.register_blueprint(bp_profile)
app.register_blueprint(bp_video)
app.register_blueprint(bp_calculation)
app.register_blueprint(bp_consultation)
app.register_blueprint(bp_study)
CORS(app)

if __name__ == "__main__":
    
    jwt.init_app(app)
    app.run(debug=True, host="0.0.0.0", port=80)

