from flask import render_template, Flask, request, url_for, redirect, Response
from application import app, db
import requests
import random 
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from application.models import Car

@app.route('/', methods=['GET', 'POST'])
def car():
    rand = random.randint(1,5)
    getCar = Car.query.filter_by(id=rand).first()
    print(getCar)
    return str(getCar)