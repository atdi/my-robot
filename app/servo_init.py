#!/usr/bin/python3
from .pwm import PWM
import time


def init_servo():
    #servoMin = 150  # Min pulse length out of 4096
    #servoMax = 600  # Max pulse length out of 4096
    pwm = PWM(0x40)
    #pwm = PWM(0x40, debug=True)
    pwm.set_freq(60)                      # Set frequency to 60 Hz
    #pwm.setPWM(0, 0, 450)   #medium
    return pwm


if __name__ == '__main__':
    pwm_smp = init_servo()
    while True:
        pwm_smp.set(0, 0, 375)
        time.sleep(1)
        pwm_smp.set(0, 0, 450)
        time.sleep(1)
        pwm_smp.set(0, 0, 525)
        time.sleep(1)
        pwm_smp.set(0, 0, 450)
        time.sleep(1)
