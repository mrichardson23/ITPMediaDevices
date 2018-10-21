from gpiozero import LED, Button
from time import sleep

blueLED = LED(17)
# Create an instance of the Button object, and set that it's on pin 14:
redButton = Button(14)
# Hint: input pins are pulled up, so just connect one side of the button to the GPIO pin and the other side of the button to GND.

while True:
    redButton.wait_for_press() # Wait here until the button is pressed.
    blueLED.toggle() # Turn the LED off if it's on and vice versa.
    sleep(1) # a super simple way to "debounce," to make sure one button press is interpreted as only one press