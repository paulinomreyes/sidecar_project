from flask import Flask, request
import os
import sys

app = Flask(__name__)
app.debug = True

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form['msg'])
    return "Success"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True) 
