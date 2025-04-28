# Main application structure using Python with Flask
from flask import Flask, render_template, request, jsonify
import pygame
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/challenge')
def challenge():
    return render_template('challenge.html')

if __name__ == '__main__':
    app.run(debug=True)