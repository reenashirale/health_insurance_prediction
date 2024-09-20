from flask import Flask, jsonify, render_template, request
from config import *
from utils import HealthInsurance

app = Flask(__name__)

insurance = HealthInsurance()
@app.route('/')
def home():
    return render_template('home.html', charges='')


@app.route('/get_charges', methods=['POST'])
def get_insurance_charges():
    if request.method == 'POST':
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']
        charges = insurance.predict_insurance_charges(age, sex, bmi, children, smoker, region)
    else:
        return jsonify('Bad Request')
    return render_template('home.html', charges=charges)


if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')
