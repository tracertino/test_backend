from flask_basicauth import BasicAuth
from werkzeug.security import check_password_hash
from Models.users import User

basic_auth = BasicAuth()
# @basic_auth.required
def authenticate(username, password):
    # user = User.query.filter_by(username=username).first()
    if username == "admin" and password == "qw":
    # if user and check_password_hash(user.password, password):
        return True
    return False

basic_auth.check_credentials = authenticate

