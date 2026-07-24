from AzuraLang import useDarkMode, window, label, guiInput, button, run

# Globally pass the Equilux dark configuration to everything before window creation
useDarkMode()

# Initialize the main test frame
window("darkWin", title="AzuraLang Dark Theme Style Test", size="450x350")

# Verify label background blending with the main dark canvas
label("darkWin", text="Seamless Style Injection Test Matrix")

# Deploy components to verify that legacy Text elements match charcoal dark values
guiInput("darkWin", text="System Query:", input_type="TextString")
guiInput("darkWin", text="Verbose Logs:", input_type="TextBox")

# Confirm dialog interaction works cleanly under the dark engine
filepath = guiInput("darkWin", text="Output Path:", input_type="Select", select_mode="file")

button("darkWin", text="Execute Script", command=lambda: print("Dark mode engine online!"))

run()