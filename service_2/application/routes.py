from flask import render_template, Flask, request, url_for, redirect, Response
from application import app, db
import requests
from random import randint
from flask_sqlalchemy import SQLAlchemy

@app.route('/', methods=['GET', 'POST'])
def car():
    rand = random.randint(1,5)
    getCar = Car.query.filter_by(id=rand).first()
    print(getCar)
    return str(getCar)