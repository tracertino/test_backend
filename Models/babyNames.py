from . import db
from Models.gender import Gender

class BabyNames(db.Model):
    __tablename__ = 'babyNames'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    gender = db.relationship("Gender", backref='genders_name', lazy=True)
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_items(cls, gender):   
        get_gender = Gender.query.filter_by(name=gender).one_or_none()   
        
        if get_gender:
            items = get_gender.genders_name
            return [item.name for item in items], 200
        else:
             return {"message": "Ошибка"}, 500