from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True, unique=True, autoincrement="auto")
    username = Column(String(20), nullable=False)
    data = Column(String(500), nullable=False)

    @classmethod
    def add_item(self, session, username, data):
        res=Feedback(username=username, data=data)
        session.add(res)
        session.commit()

    @classmethod
    def get_items(cls, session):
        response_json = []
        items = session.query(cls).all()
        for item in items:
            response_json.append({"id": item.id,
                                "username": item.username,
                                "data": item.data})
        session.close()
        return response_json