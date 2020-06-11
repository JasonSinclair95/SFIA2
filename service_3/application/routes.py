from flask import render_template, Flask, request, url_for, redirect, Response
from application import app, db
import requests
import random 
from flask_sqlalchemy import SQLAlchemy

from application.models import Weapon

@app.route('/', methods=['GET', 'POST'])
def weapon():
    rand = random.randint(1,6)
    getWeapon = Weapon.query.filter_by(id=rand).first()
    print(getWeapon)
    return str(getWeapon)
