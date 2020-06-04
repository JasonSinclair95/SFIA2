from flask import render_template
from application import app 
import requests

app.route('/car_weapon', method=['GET'])
def car_weapon():
    weapon = ['oil spill, machine gun, EMP, Rockets, Nitrous, Invisibility cloak,']
    num = randint(0,4)
    return Response((weapon[num]), mimetype='text/plain')

