from omxplayer.player import OMXPlayer
from gpiozero import LED
from time import sleep

player = OMXPlayer("candle.mp4", args=['--no-osd'])

greenLED = LED(18)
greenLED.on()

while True:
	# Check if the playhead is past 6.9 seconds. If so, turn the LED off and stop checking.
    if player.position() > 6.9:
        greenLED.off()
        break
