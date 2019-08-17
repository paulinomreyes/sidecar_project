from flask import Flask
import requests
import os

app = Flask(__name__)
app.debug = True

def log(message):
    data = {"msg": message}
    url = "http://localhost/submit"
    print requests.post(url, data).text


@app.route('/')
def index():

    log("This is a message")
    
    return "Welcome to My SideCar Project"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080) 
