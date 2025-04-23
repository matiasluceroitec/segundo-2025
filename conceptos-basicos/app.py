from datetime import date
import requests

from flask import (
    Flask, 
    render_template,
    request,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def acerca():
    return render_template('acerca_de.html')

@app.route('/users/')
def usuarios():
    cant = request.args.get('cant', 3, int)
    response = requests.get(
        f'https://randomuser.me/api/?results={cant}'
    ).json()
    list_usuarios = response['results']
    return render_template(
        'users.html',
        usuarios=list_usuarios,
        hoy=date.today()
    )
