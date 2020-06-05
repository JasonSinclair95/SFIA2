from flask import render_template, Flask, request, url_for, redirect, Response
from application import app 
import requests
from random import randint 



@app.route('/car_weapon', methods=['GET'])
def car_weapon():
    weapon = ['oil spill', 'machine gun', 'EMP', 'Rockets', 'Nitrous', 'Invisibility cloak']
    return Response(weapon[randint(0,5)], mimetype='text/plain')

