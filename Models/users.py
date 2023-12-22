from . import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # email = Column(String(50), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    family_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False) 
    role = db.Column(db.String(10), nullable=False)
    token =  db.Column(db.String(200), nullable=False) 
    # calculation = relationship("Calculation")
    