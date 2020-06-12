from application import db

class CarConfig(db.Model):
    __tablename__ = 'carconfig'
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String(30), nullable=False)
    weapon = db.Column(db.String(30), nullable=False)