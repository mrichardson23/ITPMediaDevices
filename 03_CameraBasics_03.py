from picamera import PiCamera

camera = PiCamera()

camera.start_preview(alpha=200)
camera.start_recording('myVideo.h264') # record video
camera.wait_recording(5) # wait for 5 seconds of video recorded

camera.stop_recording()
camera.stop_preview()
