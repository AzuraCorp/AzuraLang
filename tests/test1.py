import AzuraLang as azl

azl.window("root", title="Label test") # Make a window
azl.label("root", text="This label is pink with a black bg!", fg="pink", bg="black") # Make a coloured label
azl.label("root", text="This label's font is 18pt Hack Nerd.", font=("Hack Nerd", 18)) # Make a custom label
azl.label("root", text="This label is Bold+Italic...", font=("Arial", 11, "bold", "italic")) # Make an attributive(?) label
azl.label(
    "root",
    text="A quick brown fox jumps over a lazy dog",
    fg="pink", bg="black",
    font=("Hack Nerd", 11, "bold", "italic", "underline")
) # Make an alltogether styled label

azl.run("root") # Run the script