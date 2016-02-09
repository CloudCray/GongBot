__author__ = 'Cloud'
from flask import Flask
import time

app = Flask(__name__)

delay_period = 0.01


@app.route("/<mode>/<value>/<delay>")
def bang(mode, value, delay):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + mode, 'w')
        f.write(value)
        f.close()
        time.sleep(delay_period)
        return "Success!"
    except Exception as ex:
        return "Error writing to: " + mode + " value: " + value + ";\n" + str(ex)


app.run(host='0.0.0.0', port=9009, debug=True)
