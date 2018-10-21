from picamera import PiCamera
from time import sleep

# Instantiate a camera object:
myCamera = PiCamera()

# Start the preview, setting it to be semi-transparent, so that you can see what's going on behind it:
myCamera.start_preview(alpha=200)
sleep(1)
myCamera.capture("image.jpg")
myCamera.stop_preview()
