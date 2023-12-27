from . import db
from Models.level import Level

class Consultation(db.Model):
    __tablename__ = 'consultation'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    link = db.Column(db.String)
    videolink = db.Column(db.String)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    levels = db.relationship("Level", backref='consultations', lazy=True)
    
    def __str__(self):
        return self.title

    @classmethod
    def get_items(cls, level):   
        get_level = Level.query.filter_by(name=level).one_or_none()   
        
        if get_level:
            consultations = get_level.consultations
            return [{"title": consultation.title,
                    "description": consultation.description,
                    "price": consultation.price,
                    "videolink": consultation.videolink,
                    "link": consultation.link} for consultation in consultations], 200
        else:
             return {"message": "Ошибка"}, 500