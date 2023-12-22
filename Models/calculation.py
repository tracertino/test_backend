from . import db

class Calculation(db.Model):
    __tablename__ = 'calculation'
    id = db.Column(db.String(200), primary_key=True)
    # calc_id = db.Column(db.Integer,  db.ForeignKey(Users.id))
    fio = db.Column(db.String(200), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    # calc = db.Column(db.String(200), nullable=True)
    # email = Column(String(50), nullable=False)
    # user_name = Column(String(20), nullable=False)
    # family_name = Column(String(20), nullable=False)
    # last_name = Column(String(20), nullable=True)
    # password = Column(String(50), nullable=False)
    # birthday = Column(DateTime, nullable=False) 
    # role = Column(String(10), nullable=False)
    # token =  Column(String(200), nullable=False) 
    