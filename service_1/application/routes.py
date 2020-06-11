from flask import render_template, Flask, request, url_for, redirect
from application import app 
import requests

from application.models import CarConfig

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
        carconfigData = CarConfig.query.all()
        response = requests.get('http://service4:5003/').text
        return render_template('home.html', car=carconfigData display=response, title='Home')


