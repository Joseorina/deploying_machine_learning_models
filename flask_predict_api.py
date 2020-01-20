import pickle
from flask import Flask, request
import pandas as pd
import numpy as np

with open('srf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
app = Flask(__name__)

@app.route('/predict')
def predict_iris():
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')
    
    prediction = model.predict(np.array([[s_length, s_width, 
                                          p_length, p_width]]))
    return str(prediction)

if __name__ == '__main__':
    app.run()