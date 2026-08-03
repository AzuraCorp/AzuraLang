import AzuraLang as azl

wn = azl.window("root", size="500x400")

fntslct = azl.guiInput("root", inputType="textString", text="Type fontname e.g. Calibri") # Singleline input
fntsz = azl.guiInput("root", inputType="textString", text="Type text size e.g. 12") # "" ""
txt = azl.guiInput("root", inputType="textBox", text="What should the label say?") ## Multiline input
lbal = azl.label("root", text="A quick brown fox jumps over a lazy dog.")

def raer(fonttype, size, text): # A function to change the label
    lbal.config(font=(fonttype, size), text=text)

btn = azl.button("root", text="Change ", command=lambda: raer(fntslct.get(), fntsz.get(), txt.get())) # Edit the label by clicking

azl.run("root") # Run the script!
