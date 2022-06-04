from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return("Hello World!!")

@app.route('/sports')
def mars():
    return("Hello Sports!!")
    
app.run(debug=True)