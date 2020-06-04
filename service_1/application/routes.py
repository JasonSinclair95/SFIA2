from flask import render_template, Flask, request, url_for, redirect
from application import app 
import requests

@app.route('/', methods=['GET'])
def home():
        response = requests.get('http://service4:5003/CarAndWeapon')
        generate_vehicle_config = response.text
        print(generate_vehicle_config)
        return render_template('home.html', generate_vehicle_config = generate_vehicle_config, title='Home')

 