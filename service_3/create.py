from application import db
from application.models import Weapon

db.drop_all()
db.create_all()