from application import db

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return str(self.car)