# Usando y controlando la matriz de botones

from gpiozero import Button, LED

row_pins = [27, 22, 5, 6]
col_pins = [25, 26, 19, 13]

# Definición del mapa de teclas
key_map = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
    ['13', '14', '15', '16']
]

# Inicializar filas como entrada y columnas como salida
rows = [Button(pin, pull_up=True) for pin in row_pins]
cols = [LED(pin) for pin in col_pins]

# Continuar escaneando teclas
try: