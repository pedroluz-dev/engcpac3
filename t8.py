import os
from flask import Flask
from flask import jsonify
from flask import request
from math import sqrt

app = Flask(__name__)

@app.route('/')


def ehprimo(numero):
    primo = True
    
    if (numero == 1 ):
        primo = False
    else:
        primo = True

    for i in range (2, numero):
        if (numero % i == 0):
            primo = False
    return primo

def cade_os_primos ():
    numero = 1
    primos = []
    while len(primos) <= 100:
        if (ehprimo(numero)):
            primos.append(numero)
        numero+= 1

    return primos

cade_os_primos()
            

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    