#import the necessary packages
import ktrain
from flask import Flask, request,jsonify
import json



# initialize our Flask application and the Ktrain model
app = Flask(__name__)
predictor = None

#we load our trained ktrainmodel
def load_predictor():
    global predictor
    predictor = ktrain.load_predictor("model_corps_mail_bert")
    if hasattr(predictor.model, '_make_predict_function'):
        predictor.model._make_predict_function()
    return predictor

@app.route('/predict',methods=['POST'])
def predict():
    #fonction user : prédiction d'un texte contenu dans le body 
    # return : une prédiction 

    data = request.get_json()
    
    print(data)
    print(type(data))
    #initialize a data dictionary that will be returned from the view
    result = {"status": "No_prediction"}
    #récupération du text
    if 'text'in data:
        prediction = predictor.predict(data['text'])
        result["prediction"] = prediction
        result["status"] = "prediction_done"
    else:
        result["status"] = "no_text"
    return result
        
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_predictor()
    port = 8008
    app.run(host='0.0.0.0', port=port)
