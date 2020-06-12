from flask import render_template, Flask, request, url_for, redirect
from application import app, db
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

from application.models import CarConfig

@app.route('/', methods=['GET'])
@app.route('/home')
def home():
        carconfigData = CarConfig.query.all()
        response = requests.get('http://service4:5003/').text
        return render_template('home.html', car=carconfigData, display=response, title='Home')

@app.route('/Delete/<id>/CarConfig/', methods=['GET','POST'])
def DeleteCarConfig(id):
	carconfigData = CarConfig.query.filter_by(id=id).first()
	
	
	db.session.delete(carconfigData)

	db.session.commit()
	return redirect(url_for('home'))