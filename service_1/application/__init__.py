from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=getenv('RECRUITMENT_VM_DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']=getenv('SECRET_KEY')
db = SQLAlchemy(app)

from application.models import cars

from application import routes
