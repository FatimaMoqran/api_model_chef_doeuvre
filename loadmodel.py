import ktrain
print(ktrain.__version__)

predictor = ktrain.load_predictor("model_corps_mail_bert")
data = 'les fournisseurs ne sont pas là'
result = predictor.predict(data)
print(result)