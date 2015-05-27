# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('default.html')

@app.route('/<name>/')
def hello(name):
    return render_template('index.html',name=name)

@app.route('/upload/')
def upload():
	return render_template('upload.html')

if __name__ =='__main__':
	app.run(port=5001,debug=True)

