from AzuraLang import window, label, button, guiInput, run, useDarkMode

# 0. Make the windows dark by default!
useDarkMode()

# 1. Initialize the window
window("formWin", title="User Registration", size="300x250")

# 2. Add some text
label("formWin", text="Welcome to AzuraLang! Enter your info:")

# 3. Add the input fields and SAVE their references to variables
username_field = guiInput("formWin", text="Username:", input_type="TextString")
bio_field = guiInput("formWin", text="Short Bio:", input_type="TextBox")

# 4. Define the command that runs when the button is clicked
def on_submit():
    print("\n--- NEW USER REGISTERED ---")
    print(f"Name: {username_field.get()}")
    print(f"Bio: {bio_field.get()}")
    print("---------------------------\n")

# 5. Add the button and bind the command
button("formWin", text="Register User", command=on_submit)

# 6. Start the engine
run()
