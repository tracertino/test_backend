
from sqlalchemy.exc import IntegrityError

from extentions import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    subcategories = db.relationship('Subcategory', backref='category', lazy=True)

    @classmethod
    def get_items(cls):        
        categories = db.session.query(cls).all()
        return [{"category": category.name, "id": category.id} for category in categories], 200

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
            return [{"subcategory": subcategory.name} for subcategory in subcategories], 200
        else:
            return {"message": "Ошибка"}, 500

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    URL = db.Column(db.String)
    role = db.Column(db.String)
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

    # @classmethod
    # def get_items_support(cls, session):
    #     response_json = []
    #     items = session.query(cls).all()
    #     for item in items:
    #         response_json.append({"id": item.id,
    #                             "question": item.question,
    #                             "answer": item.answer})
    #     session.close()
    #     return response_json