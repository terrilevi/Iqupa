from picamera2 import Picamera2
from time import sleep
from gpiozero import LED
from time import sleep

led = LED(17)

camera = Picamera2()
camera.start()

led.off()
sleep(1)
camera.capture_file('/home/moises/Documents/proyectos/codes/image.jpg')
led.on()

camera.stop()
#camera.stop()
