from gpiozero import Button
from signal import pause

def say_hello():
    print("Cerrado!")

def say_goodbye():
    print("Abierto!")

button = Button(2)

button.when_pressed = say_hello
button.when_released = say_goodbye

pause()