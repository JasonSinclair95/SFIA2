from flask import render_template, Flask, request, url_for, redirect
from application import app, db
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from application.models import CarConfig

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
        
        response = requests.get('http://service4:5003/').text
        return render_template('home.html', display=response, title='Home')

@app.route('/carconfigs')
def carconfigs():
        carconfigData = CarConfig.query.all()
        return render_template('carconfigs.html', car=carconfigData, title='car configuration')



	

