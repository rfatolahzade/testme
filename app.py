#!/usr/bin/python3
import os
from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'The quick brown fox jumps over the lazy dog'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    os.system('python3 app.py')
    os.system('python3 app.py')


