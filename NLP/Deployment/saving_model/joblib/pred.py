import joblib

loaded_model = joblib.load('dib_75.pkl')
print(loaded_model.predict([[50,700,930,4,5,6,7,8]]))
