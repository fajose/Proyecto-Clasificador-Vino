from flask import Flask, render_template, request
import jsonify
import requests
from datetime import date, datetime
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def prepare_data(request_form):
    columns = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
               'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    
    data = []
    for column in columns:
        data.append(float(request_form.get(column, 0)))

    # Escala los datos de entrada utilizando el scaler cargado
    data_scaled = scaler.transform([data])  # Transforma los datos de entrada con el scaler

    return data_scaled[0]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = prepare_data(request.form)
        prediction = model.predict([data])
        output = prediction[0]+3

        return render_template('index.html', prediction_text=f'La calidad del vino es {output}')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)