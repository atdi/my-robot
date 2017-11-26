from .servo_init import init_servo
import time                # Import necessary modules

def Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setup():
    global leftPWM, rightPWM, homePWM, pwm
    leftPWM = 330
    homePWM = 380
    rightPWM = 430
    offset =0
    leftPWM += offset
    homePWM += offset
    rightPWM += offset
    pwm = init_servo()         # Initialize the servo controller.

# ==========================================================================================
# Control the servo connected to channel 0 of the servo control board, so as to make the
# car turn left.
# ==========================================================================================
def turn_left():
    global leftPWM
    pwm.set(0, 0, leftPWM)  # CH0

# ==========================================================================================
# Make the car turn right.
# ==========================================================================================
def turn_right():
    global rightPWM
    pwm.set(0, 0, rightPWM)

# ==========================================================================================
# Make the car turn back.
# ==========================================================================================
def turn(angle):
    angle = Map(angle, 0, 255, leftPWM, rightPWM)
    pwm.set(0, 0, angle)

def home():
    global homePWM
    pwm.set(0, 0, homePWM)

def calibrate(x):
    pwm.set(0, 0, 380+x)
