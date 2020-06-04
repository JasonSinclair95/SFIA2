from flask import render_template
from application import app 
import requests

app.route('/car_model', method=['GET'])
def car_model():
    car = ['Bugatti Veyron Super Sport, Aston Martin Valkyrrie, Tesla Roadster, Pagani Huayra BC, McLaren F1']
    num = randint(0,4)
    return Response((car[num]), mimetype='text/plain')

