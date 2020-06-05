from flask import render_template, Flask, request, url_for, redirect
from application import app 
import requests

@app.route('/CarAndWeapon', methods=['GET'])
def CarAndWeapon():
    car = requests.get('http://service2:5001/CarModel')
    weapon = requests.get('http://service3:5002/car_weapon')
    response = "your car is" + " " + car.text + " and your special weapon is " + weapon.text
   
    return response
