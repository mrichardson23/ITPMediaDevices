from omxplayer.player import OMXPlayer
from gpiozero import Button
from time import sleep

# this will start the player and it will suppress the on-screen display:
player = OMXPlayer("matt.mp4", args=['--no-osd'])

myButton = Button(14)

# this sets the playback to semi-transparent, which is helpful for debugging:
player.set_alpha(100)

# the video will start playing as soon as you load it, so pause it right away.
player.pause()

while True:
    myButton.wait_for_press()
    player.play()
    sleep(.3)
    myButton.wait_for_press()
    player.pause()
    sleep(.3)
