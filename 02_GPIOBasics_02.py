from gpiozero import LED
from signal import pause

blueLED = LED(17)
blueLED.blink()

# if you're executing from the command line, this will make sure that the script runs until you terminate it:
pause()
