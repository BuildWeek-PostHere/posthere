from flask import Flask, render_template, request

APP = Flask(__name__) 

@APP.route('/')
def hello_world():

    return render_template('base.html', title = 'Home')
  