import app.engine as engine
import app.direction as direction
import app.video_dir as video_dir
from flask import request

def init_views(app):
    @app.route('/')
    def init_robot():
        engine.setup()
        direction.setup()
        return 'Robot has been initialized!'


    @app.route('/car/forward')
    def move_forward():
        engine.forwardWithSpeed(50)
        return 'Move forward'


    @app.route('/car/backward')
    def move_backward():
        engine.backwardWithSpeed(50)
        return 'Move forward'


    @app.route('/car/left')
    def turn_left():
        direction.turn_left()
        return 'Turn left'


    @app.route('/car/right')
    def turn_right():
        direction.turn_right()
        return 'Turn right'


    @app.route('/car/home')
    def home():
        direction.home()
        return 'Home'


    @app.route('/car/stop')
    def stop():
        engine.stop()
        return 'Stop'


    @app.route('/camera/dir/calibrate')
    def calibrate_dir():
        x = int(request.args.get("x"))
        y = int(request.args.get("y"))
        video_dir.calibrate(x, y)
        return 'Calibrate'

    @app.route('/camera/up')
    def move_up():
        video_dir.move_increase_y()
        return "Up"

    @app.route('/camera/down')
    def move_down():
        video_dir.move_decrease_y()
        return "Down"

    @app.route('/camera/left')
    def move_left():
        video_dir.move_decrease_x()
        return "Left"

    @app.route('/camera/right')
    def move_right():
        video_dir.move_increase_x()
        return "Right"
