from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Support(Base):
    __tablename__ = 'support'
    id = Column(Integer, primary_key=True, unique=True, autoincrement="auto")
    question = Column(String(500), nullable=False)
    answer = Column(String(500), nullable=False)

    @classmethod
    def add_items_support(self, session, question, answer):
        post=Support(question=question, answer=answer)
        session.add(post)
        session.commit()

    @classmethod
    def get_items_support(cls, session):
        response_json = []
        items = session.query(cls).all()
        for item in items:
            response_json.append({"id": item.id,
                                "question": item.question,
                                "answer": item.answer})
        session.close()
        return response_json