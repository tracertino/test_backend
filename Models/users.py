from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement="auto")
    # email = Column(String(50), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    family_name = db.Column(db.String(20), nullable=False)
    # last_name = Column(String(20), nullable=True)
    # password = Column(String(30), nullable=False)
    # birthday = Column(DateTime, nullable=False) 
    # role = Column(String(10), nullable=False)
    # token =  Column(String(200), nullable=False) 
    # calculation = relationship("Calculation")
    