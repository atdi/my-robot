#!/usr/bin/env python3

from flask import Flask
from app import init


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    init()
    app.run(host= '0.0.0.0')
