from flask import render_template, Flask, request, url_for, redirect, Response
from application import app, db
import requests
from random import randint 
from flask_sqlalchemy import SQLAlchemy

@app.route('/', methods=['GET', 'POST'])
def weapon():
    rand = random.randint(1,6)
    getWeapon = Weapon.query.filter_by(id=rand).first()
    print(getWeapon)
    return str(getWeapon)
