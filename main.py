__author__ = 'Cloud'
from flask import Flask
import RPi.GPIO as GPIO
from threading import Thread
import time

DEFAULT_ANGLE = 90

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)


app = Flask(__name__)


def map_val(val, minx, maxx, miny, maxy):
    return (val - minx) * (maxy - miny) / (maxx - minx) + miny


@app.route("/<angle>/<seconds>")
def bang(angle, seconds):
    angle = map_val(angle, 0, 180, 5.0, 10.0)
    pwm.ChangeDutyCycle(angle)
    time.sleep(seconds * 1000)
    pwm.ChangeDutyCycle(map_val(DEFAULT_ANGLE, 0, 180, 5.0, 10.0))
    return "Success!"


pwm.start(map_val(DEFAULT_ANGLE, 0, 180, 5.0, 10.0))
app.run(host='0.0.0.0', port=9009, debug=True)
