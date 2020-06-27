from flask import request, make_response, redirect, render_template, session, url_for, flash
from app import create_app

app  = create_app


@app.route('/')
def index():
    
    return 'Hello world flask'


@app.route('/hello')
def hello():
    context={
        'message': 'Hello'
    }
    return render_template('hello.html', **context)