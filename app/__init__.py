from .servo_init import *
from .pwm import *
from .direction import *
from flask import Flask
from .views import init_views

app = Flask(__name__)

init_views(app)