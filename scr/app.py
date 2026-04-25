from tkinter import ttk as t
from tkinter import Tk
import sys
import os
from colorama import Fore, Style

# Initialize colorama
import colorama
colorama.init(autoreset=True)

windows = {}

# RARARRARARARARARARARARA
def reporterror(code="err.code", message="Test report! No errors found."):
    print(f"{Fore.CYAN}AzuraLang: Log:")
    print(f"{Fore.RED}Error[{code}]:")
    print(f"{Fore.RED}{message}")
    print(f"{Style.RESET_ALL}")

# Make the window...
def window(Name, title="Window", size="100x200"):
    win = Tk()
    win.title(title)
    win.geometry(size)
    windows[Name] = win  # Store the actual object
    return win

# Make the label widget
def label(inWinName, text="label"):
    # Pull the actual window object from our dictionary
    parent = windows.get(inWinName)
    if parent:
        lbl = t.Label(parent, text=text)
        lbl.pack() # Make it appear
        return lbl
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")

# Make the button widget
def button(inWinName, text="button", command=print('Hello, World!')):
    # Pull the actual window object from our dictionary
    parent = windows.get(inWinName)
    if parent:
        btn = t.Button(parent, text=text, command=command)
        btn.pack() # Make it appear
        return btn
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")

#init the stuff
if __name__ == "__main__":
    if windows:
        # This grabs the actual window object of the first entry
        first_name = list(windows.keys())[0]
        # Start the loop using the first window object
        list(windows.values())[0].mainloop()
    else:
        reporterror(code="0x00", message="No windows existing!")

    # sys.argv[0] is the script name, so we start at index 1
    args = sys.argv[1:]

    if args = "-t" or "--test":
        window("aaa")
        label("aaa", text="testlabel")
        button("aaa", text="Click!" command=print("TEST! BUTTON CLICKED!"))

    name = args[0]
