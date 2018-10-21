from gpiozero import LED
from time import sleep

# Create an instance of an LED called blueLED, which is connected to pin 17:
blueLED = LED(17)

# Create an infinite loop:
while True:
    blueLED.on()
    sleep(1)
    blueLED.off()
    sleep(1)
