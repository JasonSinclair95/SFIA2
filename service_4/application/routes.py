from flask import render_template, Flask, request, url_for, redirect
from application import app, db
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from application.models import CarConfig
@app.route('/', methods=['GET', 'POST'])
def carconfig():
    car = requests.get('http://service2:5001/').text
    weapon = requests.get('http://service3:5002/').text
    output = CarsConfig(
        car = car,
        weapon = weapon
    )    
    db.session.add(output)
    db.session.commit()
    response = "your car is" + " " + car.text + " and your special weapon is " + weapon.text
    return response


