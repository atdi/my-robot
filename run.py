#!/usr/bin/env python3

from flask import Flask
import app.engine as engine
import app.direction as direction


app = Flask(__name__)
engine.setup()
direction.setup()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/forward')
def move_forward():
    engine.forwardWithSpeed(50)
    return 'Move forward'


@app.route('/backward')
def move_backward():
    engine.backwardWithSpeed(50)
    return 'Move forward'


@app.route('/left')
def turn_left():
    direction.turn_left()
    return 'Turn left'

@app.route('/right')
def turn_right():
    direction.turn_right()
    return 'Turn right'


@app.route('/stop')
def stop():
    engine.stop()
    return 'Stop'


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
