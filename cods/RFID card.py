# Leer  y escribir en una tarjeta RFID usando el modulo correspondiente

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

id, text = reader.read()
print(id)
print(text)