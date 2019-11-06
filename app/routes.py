from flask import render_template

from app import app


@app.route('/')
@app.route('/home')
@app.route('/index')
def home_page():
    return render_template('home.html')
