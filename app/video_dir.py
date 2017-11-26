from .servo_init import init_servo
import time                  # Import necessary modules

MinPulse = 200
MaxPulse = 700

Current_x = 0
Current_y = 0

def setup():
    global Xmin, Ymin, Xmax, Ymax, home_x, home_y, pwm
    offset_x = 0
    offset_y = 0
    Xmin = MinPulse + offset_x
    Xmax = MaxPulse + offset_x
    Ymin = MinPulse + offset_y
    Ymax = MaxPulse + offset_y
    home_x = (Xmax + Xmin)/2
    home_y = Ymin + 80
    pwm = init_servo()           # Initialize the servo controller.

# ==========================================================================================
# Control the servo connected to channel 14 of the servo control board to make the camera
# turning towards the positive direction of the x axis.
# ==========================================================================================
def move_decrease_x():
    global Current_x
    Current_x += 25
    if Current_x > Xmax:
        Current_x = Xmax
    pwm.set(14, 0, Current_x)   # CH14 <---> X axis
# ==========================================================================================
# Control the servo connected to channel 14 of the servo control board to make the camera
# turning towards the negative direction of the x axis.
# ==========================================================================================
def move_increase_x():
    global Current_x
    Current_x -= 25
    if Current_x <= Xmin:
        Current_x = Xmin
    pwm.set(14, 0, Current_x)
# ==========================================================================================
# Control the servo connected to channel 15 of the servo control board to make the camera
# turning towards the positive direction of the y axis.
# ==========================================================================================
def move_increase_y():
    global Current_y
    Current_y += 25
    if Current_y > Ymax:
        Current_y = Ymax
    pwm.set(15, 0, Current_y)   # CH15 <---> Y axis
# ==========================================================================================
# Control the servo connected to channel 15 of the servo control board to make the camera
# turning towards the negative direction of the y axis.
# ==========================================================================================
def move_decrease_y():
    global Current_y
    Current_y -= 25
    if Current_y <= Ymin:
        Current_y = Ymin
    pwm.set(15, 0, Current_y)
# ==========================================================================================
# Control the servos connected with channel 14 and 15 at the same time to make the camera
# move forward.
# ==========================================================================================
def home_x_y():
    global Current_y
    global Current_x
    Current_y = home_y
    Current_x = home_x
    pwm.set(14, 0, Current_x)
    pwm.set(15, 0, Current_y)

def calibrate(x,y):
    pwm.set(14, 0, (MaxPulse+MinPulse)/2+x)
    pwm.set(15, 0, (MaxPulse+MinPulse)/2+y)
