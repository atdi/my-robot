#!/usr/bin/env python3

from flask import Flask
from app import init
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    pwm_smp = init()
    while True:
        pwm_smp.set(0, 0, 375)
        time.sleep(1)
        pwm_smp.set(0, 0, 450)
        time.sleep(1)
        pwm_smp.set(0, 0, 525)
        time.sleep(1)
        pwm_smp.set(0, 0, 450)
        time.sleep(1)
    #app.run(host= '0.0.0.0')
