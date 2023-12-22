from . import db

class Support(db.Model):
    __tablename__ = 'support'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement="auto")
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(500), nullable=False)

    @classmethod
    def add_item(self, question, answer):
        try:
            post=Support(question=question, answer=answer)
            db.session.add(post)
            db.session.commit()
            return {"message": "Данные добавлены"}, 200
        except Exception as e:
            return {"message": e.args[0]}, 404

    @classmethod
    def get_items(cls):
        try:
            response_json = []
            items = db.session.query(cls).all()
            for item in items:
                response_json.append({"id": item.id,
                                    "question": item.question,
                                    "answer": item.answer})
            return response_json, 200
        except Exception as e:
            return {"message": e.args[0]}, 404
            
        