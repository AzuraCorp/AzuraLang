from tkinter import ttk as t
from tkinter import Tk
import sys
import os
from colorama import Fore, Style

# Initialize colorama
import colorama
colorama.init(autoreset=True)

# 1. We'll store our windows in a dictionary so we can find them by name
windows = {}
def reporterror(code="err.code", message="Test report! No errors found."):
    print(f"{Fore.CYAN}AzuraLang: Log:")
    print(f"{Fore.RED}Error[{code}]:")
    print(f"{Fore.RED}{message}")
    print(f"{Style.RESET_ALL}")

def window(Name, title="Window", size="100x200"):
    win = Tk()
    win.title(title)
    win.geometry(size)
    windows[Name] = win  # Store the actual object
    return win

def label(inWinName, text=""):
    # Pull the actual window object from our dictionary
    parent = windows.get(inWinName)
    if parent:
        lbl = t.Label(parent, text=text)
        lbl.pack() # You need to pack/grid it to see it!
        return lbl
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")


if __name__ == "__main__":
    if windows:
        # This grabs the actual window object of the first entry
        first_name = list(windows.keys())[0]
        # Start the loop using the first window object
        list(windows.values())[0].mainloop()
    else:
        reporterror(code="0x00", message="No windows existing!")
