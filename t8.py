import os
from flask import Flask
from flask import jsonify
from flask import request
from math import sqrt

app = Flask(__name__)

@app.route('/')



def primo(num):
   if num != 1:
         t = True
         for i in range(2,num):
             if (num % i == 0):
                 t = False
                 break
         return t
         
e = []
lim = 100
 
for num in range(2, lim + 1):

    test = primo(num)

    if (test):
        e.append(num)
        return e


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    