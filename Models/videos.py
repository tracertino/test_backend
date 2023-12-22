
from sqlalchemy.exc import IntegrityError

from . import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    subcategories = db.relationship('Subcategory', backref='category', lazy=True)

    @classmethod
    def get_items(cls):        
        categories = db.session.query(cls).all()
        return [{"title": category.name, "id": category.id} for category in categories], 200

    @classmethod
    def add_item(self, name):
        try:
            post=Category(name=name)
            db.session.add(post)
            db.session.commit()
            return {"message": "Категория добавлена"}, 200
        except IntegrityError:
            return {"message": "Такая категория уже есть в БД"}, 200
        except Exception as e:
            return {"message": f"{e.args[0]}"}, 500
        finally:
            db.session.close()

    @classmethod
    def delete_item(cls, name):
        try:
            item=db.session.query(cls).filter_by(name=name).one_or_none()
            if item:
                db.session.delete(item)
                db.session.commit()
                return {"message": "Категория удалена из БД"}, 200
            else:
                return {"message": "Нет такой категории"}, 200
        except Exception as e:
            return {"mesage": e.args}, 500
        finally:
            db.session.close()


class Subcategory(db.Model):
    __tablename__ = 'subcategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    videos = db.relationship('Video', backref='subcategory', lazy=True)
    # category = db.relationship('Category', back_populates='subcategories')
    # videos = relationship("Video", back_populates="subcategory")

    @classmethod
    def add_item(self, category, subcategory):
        try:
            get_category = db.session.query(Category).filter_by(name=category).first()
            print(get_category)
            post=Subcategory(category=get_category, name=subcategory)
            db.session.add(post)
            db.session.commit()
            return {"message": "Ok"}, 200
        except IntegrityError:
            return {"message": "Name is not unique"}, 500
        except Exception as e:
            return {"message": e.args[0]}, 500
        finally:
            db.session.close()

    @classmethod
    def delete_item(cls, name):
        try:
            item=db.session.query(cls).get(name)
            db.session.delete(item)
            db.session.commit()
            return True
        except:
            return False
        finally:
            db.session.close()
            
    @classmethod
    def get_items(self, category):        
        category = Category.query.filter_by(name=category).one_or_none()
        if category:
            subcategories = category.subcategories
            return [{"title": subcategory.name} for subcategory in subcategories], 200
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
    # subcategory = relationship('Subcategory', back_populates='videos')

    @classmethod
    def add_item(self, subcategory, title, description, URL, role):
        try:
            # get_category = session.query(Category).filter_by(name=category).first()
            get_subcategory = db.session.query(Subcategory).filter_by(name=subcategory).first()
            post=Video(title=title, description=description, URL=URL, role=role, subcategory=get_subcategory)
            db.session.add(post)
            db.session.commit()
            return {"message": "Видео добавлено"}, 200
        except Exception as e:
            return {"message": f"Не удалось добавить видео. {e.args[0]}"}, 500
        finally:
            db.session.close()

    @classmethod
    def get_items(cls, subcategory):
        get_subcategory = db.session.query(Subcategory).filter_by(name=subcategory).one_or_none()
        print(get_subcategory)
        if get_subcategory:
            # result = db.session.query(cls).filter_by(subcategory=get_subcategory.id).all()
            result = get_subcategory.videos
            return [{"title": item.title,
                     "description": item.description,
                     "URL": item.URL,
                     "role": item.role} for item in result], 200
        else:
            return {"message": "non video"}, 500