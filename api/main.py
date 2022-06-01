from flask import Flask, request
import pickle 
import json 

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def hello():
    response = {}
    loaded_model = pickle.load(open('../models/Random_Forest_2022-06-01.sav', 'rb'))
    json = request.json
    values = [json[x] for x in json]

    response['model'] = str(loaded_model)

    pred = loaded_model[1].predict([values])[0]
    proba = loaded_model[1].predict_proba([values])[0][1]

    if str(pred) == "1":
        fraude = True
    else: 
        fraude = False

    response['fraude'] = fraude
    response['fraude_probabilidade'] = str(int(proba*100))+"%"
    return response

if __name__ == "__main__":
    app.run()