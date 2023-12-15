from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
# from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

# db = SQLAlchemy()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    subcategories = relationship('Subcategory', back_populates='category')

    @classmethod
    def add_item(self, session, name):
        try:
            post=Category(name=name)
            session.add(post)
            session.commit()
            return {"message": "Ok"}, 200
        except IntegrityError:
            return {"message": "Name is not unique"}, 404
        finally:
            session.close()

    @classmethod
    def delete_item(cls, session, name):
        try:
            item=session.query(cls).get(name)
            session.delete(item)
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()


class Subcategory(Base):
    __tablename__ = 'subcategories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='subcategories')
    videos = relationship("Video", back_populates="subcategory")

    @classmethod
    def add_item(self, session, category, name):
        try:
            get_category = session.query(Category).filter_by(name=category).first()
            print(get_category)
            post=Subcategory(category=get_category, name=name)
            session.add(post)
            session.commit()
            return {"message": "Ok"}, 200
        except IntegrityError:
            return {"message": "Name is not unique"}, 404
        finally:
            session.close()

    @classmethod
    def delete_item(cls, session, name):
        try:
            item=session.query(cls).get(name)
            session.delete(item)
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    URL = Column(String)
    role = Column(String)
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'))
    subcategory = relationship('Subcategory', back_populates='videos')

    @classmethod
    def add_item(self, session, category, subcategory, title, description, URL, role):
        try:
            get_category = session.query(Category).filter_by(name=category).first()
            get_subcategory = session.query(Subcategory).filter_by(name=subcategory).first()
            post=Video(title=title, description=description, URL=URL, role=role, subcategory=get_subcategory)
            session.add(post)
            session.commit()
            return {"message": "Видео добавлено"}, 200
        except:
            return {"message": "Не удалось добавить видео"}, 404
        finally:
            session.close()

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