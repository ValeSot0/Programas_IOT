# Detección touch usando el sensor touch

from gpiozero import DigitalInputDevice as Touch
import time

# define touch pin
touch_sensor = Touch(17)

while True:
    # check if touch detected
    if touch_sensor.value:
        print('Touch Detected')
    time.sleep(0.1)