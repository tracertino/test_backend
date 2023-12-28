
from sqlalchemy.exc import IntegrityError

from . import db

class Page(db.Model):
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    
    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    page = db.relationship("Page", backref='pages', lazy=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_items(cls, _page):  

        page = Page.query.filter_by(name=_page).one_or_none()
        if page:
            items = page.pages
            return [{"title": item.name, "id": item.id} for item in items], 200
        else:
            return {"message": "Ошибка"}, 500

        # categories = db.session.query(cls).all()
        # return [{"title": category.name, "id": category.id} for category in categories], 200

class Subcategory(db.Model):
    __tablename__ = 'subcategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    videos = db.relationship('Video', backref='subcategory', lazy=True)
    category = db.relationship('Category', backref='subcategories')
    # category = db.relationship('Category', back_populates='subcategories')
    # videos = relationship("Video", back_populates="subcategory")
    
    def __str__(self):
        return self.name

    @classmethod
    def get_items(cls, _page, _category):        
        page = Page.query.filter_by(name=_page).one_or_none()
        if page:
            result = cls.query.join(Category).filter(Category.page == page, Category.name == _category).all()
            return [{"title": item.name} for item in result], 200
        else:
            return {"message": "Ошибка"}, 500

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    URL = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=False)

    @classmethod
    def get_items(cls, _page, _subcategory ):
        page = Page.query.filter_by(name=_page).one_or_none()
        subcategory = Subcategory.query.filter_by(name=_subcategory).one_or_none()

        if page and subcategory:
            result = cls.query.join(Subcategory).join(Category).filter(Category.page == page, Subcategory.name == _subcategory).all()
            return [{"title": item.title,
                     "description": item.description,
                     "URL": item.URL,
                     "role": item.role} for item in result], 200
        else:
            return {"message": "Ошибка"}, 500