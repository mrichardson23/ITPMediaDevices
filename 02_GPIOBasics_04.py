from gpiozero import LED, Button
from signal import pause

blueLED = LED(17)
redButton = Button(14)

blueLED.on()
    
def changeLED():
    blueLED.toggle()

# tell the redButton object which function to execute when the button is pressed:
redButton.when_pressed = changeLED

pause()
