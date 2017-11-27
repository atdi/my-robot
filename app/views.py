import app.engine as engine
import app.direction as direction
import app.video_dir as video_dir
from flask import request
from flask import json

def init_views(app):
    @app.route('/')
    def init_robot():
        engine.setup()
        direction.setup()
        response = app.response_class(
            response=json.dumps({'message': 'Robot has been initialized!'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/car/forward')
    def move_forward():
        engine.forwardWithSpeed(50)
        response = app.response_class(
            response=json.dumps({'message': 'Move forward'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/car/backward')
    def move_backward():
        engine.backwardWithSpeed(50)
        response = app.response_class(
            response=json.dumps({'message': 'Move backward'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/car/left')
    def turn_left():
        direction.turn_left()
        response = app.response_class(
            response=json.dumps({'message': 'Turn left'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/car/right')
    def turn_right():
        direction.turn_right()
        response = app.response_class(
            response=json.dumps({'message': 'Turn ritght'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/car/home')
    def home():
        direction.home()
        response = app.response_class(
            response=json.dumps({'message': 'Home'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/car/stop')
    def stop():
        engine.stop()
        response = app.response_class(
            response=json.dumps({'message': 'Stop engine'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/camera/dir/calibrate')
    def calibrate_dir():
        x = int(request.args.get("x"))
        y = int(request.args.get("y"))
        video_dir.calibrate(x, y)
        response = app.response_class(
            response=json.dumps({'message': 'Calibrate'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/camera/up')
    def move_up():
        video_dir.move_increase_y()
        response = app.response_class(
            response=json.dumps({'message': 'Camera up'}),
            status=200,
            mimetype='application/json'
        )
        return response


    @app.route('/camera/down')
    def move_down():
        video_dir.move_decrease_y()
        response = app.response_class(
            response=json.dumps({'message': 'Camera down'}),
            status=200,
            mimetype='application/json'
        )
        return response

    @app.route('/camera/left')
    def move_left():
        video_dir.move_decrease_x()
        response = app.response_class(
            response=json.dumps({'message': 'Camera left'}),
            status=200,
            mimetype='application/json'
        )
        return response

    @app.route('/camera/right')
    def move_right():
        video_dir.move_increase_x()
        response = app.response_class(
            response=json.dumps({'message': 'Camera right'}),
            status=200,
            mimetype='application/json'
        )
        return response
