from . import db

class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    def __str__(self) -> str:
        return self.name