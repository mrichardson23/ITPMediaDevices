from guizero import App, Text
app = App(title="Hello world")

welcome_message = Text(app, text="Welcome!", size=40)

app.display()
