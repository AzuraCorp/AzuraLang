import AzuraLang as azl
import time

wn = azl.window("root")
cl = azl.guiInput("root", text="Select a colour:", input_type="select", select_mode="color")

lbal = azl.label("root", text="This window's bg would apper as the slected colour.")
wn.config(bg=cl.get())

azl.run()
while True:
    print(cl.get())
    time.sleep(0.2)