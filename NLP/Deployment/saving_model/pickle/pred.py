import pickle

loaded_model = pickle.load(open('dib_76.pkl','rb'))
print(loaded_model.predict([[50,700,930,4,5,6,7,8]]))