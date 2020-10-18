import os
from flask import Flask
from flask import jsonify
from flask import request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def primos():
    primos = []
    i = 2
    while i < 101:
        if i % i == 0 and i % 2 == 0 and i % 3 == 0:
            primos.append(i)
            i += 1
    return primos
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    