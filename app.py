from flask import Flask
from flask_cors import CORS
from jwt_utils import jwt
from Routes.feedback_routes import bp_feedback
from Routes.profile_routes import bp_profile
from Routes.support_routes import bp_support
from Routes.video_routes import bp_video
from Models.support import db   

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "kniga_code"
jwt.init_app(app)

    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()

app.register_blueprint(bp_feedback)
app.register_blueprint(bp_support)
app.register_blueprint(bp_profile)
app.register_blueprint(bp_video)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

