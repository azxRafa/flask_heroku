from flask import Flask
from flask import request
import joblib
import pickle
import pandas as pd
import json


app = Flask(__name__)


@app.route("/api/predict",methods=["POST"])
def predict():
    d = json.loads(request.data)
    df = pd.DataFrame.from_dict(d, orient='index').T
    df.iloc[:, [0, 5, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 40, 41]] = df.iloc[:, [0, 5, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 40, 41]].astype('int')
    df.iloc[:, [6, 7, 8, 17, 30, 31, 32, 33]] = df.iloc[:, [6, 7, 8, 17, 30, 31, 32, 33]].astype('float')
    # model = joblib.load('../models/catboost1.pkt')
    model = joblib.load('./models/catboost1.pkt')
    return str(model.predict(df)[0])


@app.route("/api/model")
def model():
    return str([{"catboost":"model1", "desc": "Катбустит"}, {"LogisticRegression":"model2", "desc": "Логично думает"}])

@app.route("/api/model1/predict",methods=["POST"])
def predict_model1():
    return predict()

@app.route("/api/model2/predict",methods=["POST"])
def predict_model2():
    d = json.loads(request.data)
    df = pd.DataFrame.from_dict(d, orient='index').T
    df.iloc[:, [0, 5, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 40, 41]] = df.iloc[:, [0, 5, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 40, 41]].astype('int')
    df.iloc[:, [6, 7, 8, 17, 30, 31, 32, 33]] = df.iloc[:, [6, 7, 8, 17, 30, 31, 32, 33]].astype('float')
    df = df.drop(df.iloc[:, 1:5], axis=1)
    model = pickle.load(open('../models/logistic.pkt', 'rb'))
    return str(model.predict(df)[0])

#app.run()