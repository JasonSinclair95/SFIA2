from flask import render_template, Flask, request, url_for, redirect
from application import app, db
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from service_4.application.models import CarConfig

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
        carconfigData = CarConfig.query.all()
        response = requests.get('http://service4:5003/').text
        return render_template('home.html', car=carconfigData, display=response, title='Home')



