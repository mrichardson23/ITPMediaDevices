from guizero import App, Text
from gpiozero import Button

app = App(title="Hello world")
myButton = Button(14)

message = Text(app, text="Hello, world!", size=40)

def changeText():
    message.value = "Button was pressed."

# Execute the changeText function when the button is pressed:    
myButton.when_pressed = changeText

app.display()
