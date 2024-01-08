
from Models.users import Role

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
    name = db.Column(db.String(20), nullable=False, unique=False)
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

class Subcategory(db.Model):
    __tablename__ = 'subcategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    videos = db.relationship('PageVideo', backref='subcategory', lazy=True)
    category = db.relationship('Category', backref='subcategories')
    
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

class PageVideo(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    URL = db.Column(db.String, nullable=False)
    role = db.relationship("Role", backref='rolies', lazy=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
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
                     "role": f"{item.role}"} for item in result], 200
        else:
            return {"message": "Ошибка"}, 500
        
class PageStars(db.Model):
    __tablename__ = 'stars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    familyname = db.Column(db.String)
    lastname = db.Column(db.String)
    birthday = db.Column(db.Date)
    description = db.Column(db.String)
    calculation = db.Column(db.JSON)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=False)
    subcategory = db.relationship("Subcategory", backref='stars_subcategory', lazy=True)

    @classmethod
    def get_items(cls, _page, _subcategory ):
        page = Page.query.filter_by(name=_page).one_or_none()
        subcategory = Subcategory.query.filter_by(name=_subcategory).one_or_none()

        if page and subcategory:
            result = cls.query.join(Subcategory).join(Category).filter(Category.page == page, Subcategory.name == _subcategory).all()
            return [{"name": item.name,
                     "lastname": item.lastname,
                     "familyname": item.familyname,
                     "birthday": item.birthday,
                     "description": item.description,
                     "calculation": item.calculation} for item in result], 200
        else:
            return {"message": "Ошибка"}, 500
        
class PageBook(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image_paths = db.Column(db.String)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=False)
    subcategory = db.relationship("Subcategory", backref='book_subcategory', lazy=True)

    @classmethod
    def get_items(cls, _page, _subcategory ):
        page = Page.query.filter_by(name=_page).one_or_none()
        subcategory = Subcategory.query.filter_by(name=_subcategory).one_or_none()

        if page and subcategory:
            result = cls.query.join(Subcategory).join(Category).filter(Category.page == page, Subcategory.name == _subcategory).all()
            return [{"title": item.title,
                     "description": item.description,
                     "imagePaths": item.image_paths} for item in result], 200
        else:
            return {"message": "Ошибка"}, 500

class PageStudyVideo(db.Model):
    __tablename__ = 'studyVideo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    link = db.Column(db.String)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=False)
    subcategory = db.relationship("Subcategory", backref='studyVideo_subcategory', lazy=True)

    @classmethod
    def get_items(cls, _page, _subcategory ):
        page = Page.query.filter_by(name=_page).one_or_none()
        subcategory = Subcategory.query.filter_by(name=_subcategory).one_or_none()

        if page and subcategory:
            result = cls.query.join(Subcategory).join(Category).filter(Category.page == page, Subcategory.name == _subcategory).all()
            return [{"title": item.title,
                     "description": item.description,
                     "link": item.link} for item in result], 200
        else:
            return {"message": "Ошибка"}, 500