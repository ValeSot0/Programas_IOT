# Controlar servomotores usando interfaces para servomotores

from gpiozero import Servo
import time

servo = Servo(25)
while True:
    servo.min()
    time.sleep(1)
    servo.mid()
    time.sleep(1)
    servo.max()
    time.sleep(1)