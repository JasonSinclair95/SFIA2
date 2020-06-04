from flask import render_template
from application import app 
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
                response = requests.get('http://end_product:5003/CarAndWeapon')
                generate_vehicle_config = response.text
                print(generate_vehicle_config)
                return render_template('home.html', generate_vehicle_config = generate_vehicle_config, title='Home')

 