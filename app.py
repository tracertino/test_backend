from flask import Flask
from flask_migrate import Migrate, upgrade
from flask_cors import CORS
from utils.jwt_utils import jwt
from Routes.feedback_routes import bp_feedback
from Routes.profile_routes import bp_profile
from Routes.support_routes import bp_support
from Routes.video_routes import bp_video
from Routes.calculation_routes import bp_calculation
from Models import db   

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "kniga_code"
jwt.init_app(app)

migrate = Migrate(app, db)
   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


with app.app_context():
    db.init_app(app)
    db.create_all()
    # migrate.init_app(app, db)
    upgrade()

app.register_blueprint(bp_feedback)
app.register_blueprint(bp_support)
app.register_blueprint(bp_profile)
app.register_blueprint(bp_video)
app.register_blueprint(bp_calculation)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

