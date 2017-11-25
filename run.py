#!/usr/bin/env python3

from flask import Flask
import app.engine as engine


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/forward')
def move_forward():
    engine.forward()
    return 'Move forward'


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
