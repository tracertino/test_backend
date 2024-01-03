from . import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
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
    email = db.Column(db.String(50), nullable=False, unique=True)
    user_name = db.Column(db.String(20))
    family_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime)
    phone =  db.Column(db.Integer, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    token =  db.Column(db.String) 
    # calculation = relationship("Calculation")

    @classmethod
    def add_user(cls, email, password, token):
        try:
            post = cls(email=email, password=password, role_id = 1)
            db.session.add(post) 
            db.session.commit() 
            return {"message": "Пользователь зарегистрирован", "accessToken": token}, 200 
        except IntegrityError:
            return {"message": "Такой email уже существует в БД."}, 409

    @classmethod
    def user_is_auth(cls, email, password ):
        user = cls.query.filter_by(email=email).one_or_none()
        if user:
            if check_password_hash(user.password, password):
                return {"roles": f"{user.role}"}, 200
            else:
                return {"message": "Неверный пароль"}, 401
        else:
            return {"message": "Неверный логин"}, 402
    
    @classmethod
    def get_profile(cls, email):
        user = cls.query.filter_by(email=email).one_or_none()
        if user:
            return {"role": f"{user.role}",
                    "username": user.user_name,
                    "lastname": user.last_name,
                    "familyname": user.family_name,
                    "birthday": user.birthday,
                    "phone": user.phone,
                    "email": user.email}, 200
        else:
            return {"message": "Пользователь не найден"}, 404
    
    @classmethod
    def update_profile(cls, email, data):
        user = cls.query.filter_by(email=email).one_or_none()
        if user:
            if "username" in data:
                user.user_name = data["username"]
            if "lastname" in data:
                user.last_name = data["lastname"]
            if "familyname" in data:
                user.family_name = data["familyname"]
            if "birthday" in data:
                user.birthday = data["birthday"]
            if "phone" in data:
                user.phone = data["phone"]
            db.session.commit()
            return {"message": "Данные обновлены"}, 200
        else:
            return {"message": "Пользователь не найден"}, 404
 