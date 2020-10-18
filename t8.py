import os
from flask import Flask
from flask import jsonify
from flask import request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def primos():
    primos = "Somos primos"
    return primos
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    