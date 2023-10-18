#Este archivo y 2index.html tienen como proposito explorar otras formas de usar CSRF tokens
#Usando Flask-wtf
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect, CSRFError

import os

app = Flask(__name__)
app.secret_key = os.urandom(16)
csrf = CSRFProtect(app)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        session['balance'] = 0
        return render_template('2index.html')
    else:
        print ('POST request on /')
        amount = request.form['amount']
        session['balance'] -= int(amount)
        return redirect(url_for('transfer_success'))
        

@app.route('/transfer-success')
def transfer_success():
    return render_template('transfer.html')


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return(render_template('csrf_error.html', status=e.description))

if __name__ == '__main__':
    app.run(debug=True)
