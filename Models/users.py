from . import db

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
    