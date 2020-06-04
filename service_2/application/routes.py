from flask import render_template, Response
from application import app 
import requests

app.route('/car_model', method=['GET'])
def car_model():
    car = ['Bugatti Veyron Super Sport, Aston Martin Valkyrrie, Tesla Roadster, Pagani Huayra BC, McLaren F1']
    return Response(car[randint(0,4)], mimetype='text/plain')

