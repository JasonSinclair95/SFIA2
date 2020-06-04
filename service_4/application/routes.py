from flask import render_template, Response
from application import app 
import requests

@app.route('/CarAndWeapon', methods=['GET'])
def CarAndWeapon():
    car = requests.get('http://service2:5001/car_model')
    weapon = requests.get('http://service3:5002/car_weapon')
    response = car.text + " " + weapon.text
    print(response)
    return response
