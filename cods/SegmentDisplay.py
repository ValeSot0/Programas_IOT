# Controlando el diplay de 7 segmentos

from ht16k33segment_python import HT16K33Segment
import smbus
import time

def count(max, display, delay=1):
    if max < 0:
        max = 0
    if max > 9998:
        max = 9998
    for i in range(0, max + 1):
        bcd = int(str(i), 16)
        display.set_number((bcd & 0xF000) >> 12, 0)
        display.set_number((bcd & 0x0F00) >> 8, 1)
        display.set_number((bcd & 0xF0) >> 4, 2)
        display.set_number((bcd & 0x0F), 3)
        display.update()
        time.sleep(delay)