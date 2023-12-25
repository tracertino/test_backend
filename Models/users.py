from . import db
from werkzeug.security import generate_password_hash
from flask_security import UserMixin, RoleMixin
from flask_security import Security, SQLAlchemyUserDatastore



class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    users = db.relationship('User', backref='role', lazy=True)
    
    def __str__(self) -> str:
        return self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # email = Column(String(50), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    family_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.DateTime) 
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    token =  db.Column(db.String(200)) 
    # calculation = relationship("Calculation")
    
    
# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True)
    
#     def __str__(self) -> str:
#         return self.name

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     roles = db.relationship('Role', secondary='user_roles')

# # Создание таблицы для связи пользователей и ролей
# class UserRoles(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
#     role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(user_datastore)