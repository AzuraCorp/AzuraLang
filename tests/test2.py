from AzuraLang import *

useDarkMode() # Just for fun, make the window dark
window("root", title="Buton test")

def newwin():
    window("2")
    label("2", text="Hello! :3")

btn0 = button("root", text="Button0", command=lambda: label("root", text="button0 triggered!"))
btn1 = button("root", text="Button1", command=lambda: newwin())

run("root")