from guizero import App, Text, PushButton
from gpiozero import Button, LED

app = App(title="Hello world")
myButton = Button(14)
myLED = LED(18)

message = Text(app, text="Hello, world!", size=40)

def changeText():
    message.value = "Button was pressed."
    
def changeLED():
    myLED.toggle()

myButton.when_pressed = changeText

# Create a button on screen and execute the function changeLED when it's clicked
myScreenButton = PushButton(app, command=changeLED, text="toggle LED")

app.display()
