from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check/<int:a>/<int:b>/<int:c>/')
def check(a: int, b: int, c: int):
    if a == 0 and b == 0:
        if c == 0:
            return jsonify({'result': 'every number'})
        else:
            return jsonify({'result': 'no answer'})
    if a == 0:
        return jsonify({'result': -b/c})
    if b ** 2 - 4 * a * c == 0:
        return jsonify({'result': -b/(2*a)})
    elif b ** 2 - 4 * a * c > 0:
        d = b ** 2 - 4 * a * c
        return jsonify({'result': {'x_1': (-b + d ** 0.5) / (2 * a), 'x_2': (-b - d ** 0.5) / (2 * a)}})
    else:
        return jsonify({'result': 'no answer'})
    

if __name__ == '__main__':
    app.run(host= '127.0.0.1',debug=True)
