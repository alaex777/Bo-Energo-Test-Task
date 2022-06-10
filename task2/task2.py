import random

from flask import Flask, jsonify

app = Flask(__name__)

BLUE = 60
GREEN = 21
RED = 19

@app.route("/guess/<int:n>/")
def guess(n: int):
    number = random.randrange(1, 101)
    if number <= BLUE:
        return jsonify({'color': 'blue'})
    elif number <= BLUE + GREEN:
        return jsonify({'color': 'green'})
    else:
        return jsonify({'color': 'red'})
    