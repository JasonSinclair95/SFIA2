from application import db

class Weapon(db.Model):
    __tablename__ = 'weapon'
    id = db.Column(db.Integer, primary_key=True)
    weapon = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return str(self.weapon)