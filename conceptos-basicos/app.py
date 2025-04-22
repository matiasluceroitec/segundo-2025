from datetime import date
import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def acerca():
    return render_template('acerca_de.html')

@app.route('/users')
def usuarios():
    response = requests.get(
        'https://randomuser.me/api/?results=5'
    ).json()
    list_usuarios = response['results']
    return render_template(
        'users.html',
        usuarios=list_usuarios,
        hoy=date.today()
    )
