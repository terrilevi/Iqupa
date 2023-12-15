from picamera2 import Picamera2

def capture_image():
    picam = Picamera2()
    config = picam.create_still_configuration()
    picam.configure(config)


    picam.start()

    picam.capture_file('/home/moises/Documents/proyectos/codes/image.jpg')

    picam.stop()

capture_image()
