from extentions import db

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement="auto")
    username = db.Column(db.String(20), nullable=False)
    data = db.Column(db.String(500), nullable=False)

    @classmethod
    def add_item(self, username, data):
        try:
            res=Feedback(username=username, data=data)
            db.session.add(res)
            db.session.commit()
            return {"message": "Данные добавлены"}, 200
        except Exception as e:
            return {"message": e.args[0]}, 404

    @classmethod
    def get_items(cls):
        
        items = db.session.query(cls).all()
        # for item in items:
        #     response_json.append({"id": item.id,
        #                         "username": item.username,
        #                         "data": item.data})
        return [{"id": item.id,
                 "username": item.username,
                 "data": item.data} for item in items], 200
