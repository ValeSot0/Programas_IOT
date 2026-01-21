# Usar el motor paso a paso y realizar movimientos por pasos

from gpiozero import OutputDevice
import time
import math

# Declare pins as output
pin_A = OutputDevice(5)
pin_B = OutputDevice(6)
pin_C = OutputDevice(13)
pin_D = OutputDevice(19)

class Stepmotor:

    def __init__(self):
        self.interval = 0.010

    def Step1(self):