from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from Utils.middleware import jwt
from AdminPanel import basic_auth
from Routes.profile_routes import bp_profile
from Routes.feedback_routes import bp_feedback
from Routes.support_routes import bp_support
from Routes.video_routes import bp_video
from Routes.calculation_routes import bp_calculation
from Routes.consultation_routes import bp_consultation
from Routes.study_routes import bp_study
from Models import db
from AdminPanel.view import admin
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'ваш_секретный_ключ_здесь'
app.config["JWT_SECRET_KEY"] = "kniga_code"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASIC_AUTH_REALM'] = 'Login required'
app.config['JWT_BLOCKLIST_ENABLED'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

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
    "users",
    "videos",
    "role",
    "level",
    "consultation",
    "study",
    "page",
    "gender",
    "babyNames",
    "babyLastnames",
    "stars",
    "books",
    "studyVideo"
}

with app.app_context():
    db.init_app(app)
    basic_auth.init_app(app)
    migrate = Migrate(app, db)
    inspector = db.inspect(db.engine)
    table_names = set(inspector.get_table_names())
    
    if not table_name.issubset(table_names):
        print(table_name.difference(table_names))
        db.create_all()
    
    jwt.init_app(app)
    admin.init_app(app)
    
allowed_ips = ["127.0.0.1", "192.168.1.1", "46.180.209.249"]  # Замените этот список разрешенных IP-адресов на свой

class IPFilterMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ['REMOTE_ADDR'] not in allowed_ips:
            start_response('403 Forbidden', [('Content-Type', 'text/plain')])
            return [b'fuck you']
        return self.app(environ, start_response)

app.wsgi_app = IPFilterMiddleware(app.wsgi_app)
   
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

