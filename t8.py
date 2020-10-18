import os
from flask import Flask
from flask import jsonify
from flask import request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def primo():
    primos = []
    div = 0
    i = 2
    while len(primos) < 101:
        for div in range (1, i):
            if i % div == 0:
                div += 1
                if div > 1:
                    break
        if div < 1:
            primos.append(i)

    return primos

    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
