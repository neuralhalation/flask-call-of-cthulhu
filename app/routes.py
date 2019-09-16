from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lyon'}
    return render_template('main.html', title='Home', user=user)
