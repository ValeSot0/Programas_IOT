import MultiToolKit as mtk 
from gpiozero import Buzzer
import time

buzzer = Buzzer(18)  


mtk.buzzerzBeep(buzzer, on_time=0.1, off_time=0.2, repeat=9)
#mtk.buzzerzBeep(buzzer, 1, 1, 2)