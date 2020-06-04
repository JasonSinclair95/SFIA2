from flask import render_template, Response
from application import app 
import requests

app.route('/car_weapon', method=['GET'])
def car_weapon():
    weapon = ['oil spill, machine gun, EMP, Rockets, Nitrous, Invisibility cloak,']
    return Response(weapon[randint(0,5)], mimetype='text/plain')

