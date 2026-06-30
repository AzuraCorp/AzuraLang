from AzuraLang import *
window("root")
button("root", name="button1", text="I'm clickable", onclick=lambda:print("Hello!"))
label("root", pos=lambda:beforeWidget.name("button1"))
run()