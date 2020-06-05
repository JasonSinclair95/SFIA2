from flask import render_template, Flask, request, url_for, redirect, Response
from application import app 
import requests
from random import randint


@app.route('/CarModel', methods=['GET'])
def CarModel():
    car = ['Bugatti Veyron Super Sport', 'Aston Martin Valkyrrie', 'Tesla Roadster', 'Pagani Huayra BC', 'McLaren F1']
    return Response(car[randint(0,4)], mimetype='text/plain')

