from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
button = Button(14)

camera.start_preview(alpha=200)
for i in range(5): # run the code below five times, counting with the integer i
    button.wait_for_press()
    camera.capture("/home/pi/button” + str(i) + “.jpg”) # save the file with the number appended to it
camera.stop_preview()
