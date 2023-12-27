from . import db
from Models.level import Level

class Study(db.Model):
    __tablename__ = 'study'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    link = db.Column(db.String)
    videolink = db.Column(db.String)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    levels = db.relationship("Level", backref='studies', lazy=True)
    
    def __str__(self):
        return self.title

    @classmethod
    def get_items(cls, level):   
        get_level = Level.query.filter_by(name=level).one_or_none()   
        
        if get_level:
            studies = get_level.studies
            return [{"title": study.title,
                    "link": study.link,
                    "videolink": study.videolink} for study in studies], 200
        else:
             return {"message": "Ошибка"}, 500