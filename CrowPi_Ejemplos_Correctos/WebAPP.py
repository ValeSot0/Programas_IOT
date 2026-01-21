from flask import Flask, render_template_string
import time
import MultiToolKit as mtk 
from gpiozero import OutputDevice as Relay, Buzzer

# Import all the modules 
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

app = Flask(__name__)

button_state = "apagado"

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control de Botones</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #222; color: #fff; }
        .button { padding: 20px 40px; font-size: 20px; cursor: pointer; border-radius: 10px; color: white; border: none; margin: 10px; }
        .buttonGreen { background-color: #4CAF50; }
        .buttonRed { background-color: #FF6347; }
        .buttonBlue { background-color: #007BFF; }
        .buttonYellow { background-color: #FFC107; }
    </style>
</head>
<body>
    <h1>Control de Estado del Botón</h1>
    <p>Estado actual del botón: {{ state }}</p>
    <a href="/toggle"><button class="button buttonGreen {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Verde)</button></a>
    <a href="/toggle_red"><button class="button buttonRed {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Rojo)</button></a>
    <a href="/toggle_blue"><button class="button buttonBlue {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Azul)</button></a>
    <a href="/toggle_yellow"><button class="button buttonYellow {{ 'buttonOff' if state == 'encendido' else '' }}">Mi nombre (Amarillo)</button></a>
</body>
</html>
"""

@app.route('/')
def home():
    print('Accedió a la app') 
    return render_template_string(html, state=button_state)

@app.route('/toggle')
def toggle_button():
    relay = Relay(21)
    global button_state
    if button_state == "apagado":
        button_state = "encendido"
        relay.on()
    else:
        button_state = "apagado"
        relay.off()
        
    print(button_state)  
    return render_template_string(html, state=button_state)

@app.route('/toggle_red')
def toggle_button_red():
    buzzer = Buzzer(18)
    global button_state
    if button_state == "apagado":
        
        button_state = "encendido"
        mtk.buzzerzBeep(buzzer, on_time=0.1, off_time=0, repeat=1)
    else:
        button_state = "apagado"
        mtk.buzzerzBeep(buzzer, on_time=0.1, off_time=0, repeat=1)
        
    print(button_state)  
    return render_template_string(html, state=button_state)

@app.route('/toggle_blue')
def toggle_button_blue():
    vibration = Relay(27)
    global button_state
    if button_state == "apagado":
        button_state = "encendido"
        mtk.vibrationBlink(vibration, on_time=0.1, off_time=0, n=2)
    else:
        button_state = "apagado"
        mtk.vibrationBlink(vibration, on_time=0.1, off_time=0, n=2)
        
    print(button_state)  
    return render_template_string(html, state=button_state)

@app.route('/toggle_yellow')
def toggle_button_yellow():
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
    msg ="ALEX" 

    global button_state
    if button_state == "apagado":
        button_state = "encendido"
        show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
    else:
        button_state = "apagado"
        
    print(button_state)  
    return render_template_string(html, state=button_state)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)