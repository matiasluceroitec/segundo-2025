from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/states')
def states():
    with open('data/states.json') as f:
        data = json.load(f)

        return render_template(
            'states.html',
            data=data['provincias'],
        )


@app.route('/welcome/<name>')
def welcome(name):
    return f"Welcome , {name}!"

@app.route('/sum/<a>/<b>')
def suma(a, b):
    c = int(a) + int(b)
    return str(c)

