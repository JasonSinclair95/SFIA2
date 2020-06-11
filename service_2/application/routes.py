from flask import render_template, Flask, request, url_for, redirect, Response
from application import app 
import requests
from random import randint

@app.route('/', methods=['GET', 'POST'])
def car():
    rand = random.randint(0,4)
    getCar = Car.query.filter_by(id=rand).first()
    print(getCar)
    return str(getCar)