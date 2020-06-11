from flask import render_template, Flask, request, url_for, redirect
from application import app 
import requests

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
        carconfigData = CarConfig.query.all()
        response = requests.get('http://service4:5003/')
        generate_vehicle_config = response.text
        return render_template('home.html', generate_vehicle_config = generate_vehicle_config, car=carconfigData, title='Home')

