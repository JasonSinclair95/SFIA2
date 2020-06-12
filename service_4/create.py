from application import db
from application.models import CarConfig

db.drop_all()
db.create_all()