from tkinter import ttk as t
from tkinter import Tk
import sys
import os
from colorama import Fore, Style
import pytoml

# Initialize colorama
import colorama
colorama.init(autoreset=True)

windows = {}

# RARARRARARARARARARARARA
def reporterror(code="err.code", message="Test report! No errors found.", er_line=str(0), err_type="Test/Envierment Error"):
    print(f"{Style.BRIGHT}{Fore.CYAN}AzuraLang(GUI) Log:")
    print(f"{Style.BRIGHT}{Fore.RED}An error has accured at line {er_line}. Code: {code}")
    print(f"{Style.BRIGHT}{Fore.RED}{err_type} => {message}")
    print(f"{Style.BRIGHT}\033[38;5;208mThis arror is indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues !")
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
def button(inWinName, text="button", command=lambda: print('Hello, World!')):
    # Pull the actual window object from our dictionary
    parent = windows.get(inWinName)
    if parent:
        btn = t.Button(parent, text=text, command=command)
        btn.pack() # Make it appear
        return btn
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")

# Make an input widget (guiInput())
def guiInput(inWinName, text="", input_type="TextString", select_mode="file"):
    from tkinter import Text, filedialog, colorchooser
    
    # Pull the actual window object from our dictionary
    parent = windows.get(inWinName) [cite: 43]
    if not parent:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!") [cite: 43]
        return None
        
    # Create a layout frame container inside the target window
    frame = t.Frame(parent) [cite: 42, 44]
    frame.pack(fill="x", padx=5, pady=5)
    
    if text:
        lbl = t.Label(frame, text=text) [cite: 42, 44]
        lbl.pack(side="left", padx=5)
        
    if input_type == "TextString":
        widget = t.Entry(frame) [cite: 42]
        widget.pack(side="right", expand=True, fill="x", padx=5)
        # Directly map the entry's getter
        frame.get = widget.get
        
    elif input_type == "TextBox":
        # Standard tk.Text is used here since ttk doesn't feature a multiline widget
        widget = Text(frame, height=4, width=30)
        widget.pack(side="right", expand=True, fill="x", padx=5)
        # Bind a cleaner text retriever to extract content cleanly
        frame.get = lambda: widget.get("1.0", "end").strip()
        
    elif input_type == "Select":
        frame.stored_value = ""
        value_label = t.Label(frame, text="None selected", relief="sunken", width=20) [cite: 42]
        value_label.pack(side="left", padx=5, expand=True, fill="x")
        
        def handle_selection():
            if select_mode == "file":
                filepath = filedialog.askopenfilename(title="Select File")
                if filepath:
                    frame.stored_value = filepath
                    value_label.config(text=filepath.split("/")[-1])
            elif select_mode == "color":
                color_code = colorchooser.askcolor(title="Select Color")[1]
                if color_code:
                    frame.stored_value = color_code
                    value_label.config(text=color_code)
                    
        button_title = f"Choose {select_mode.capitalize()}"
        btn = t.Button(frame, text=button_title, command=handle_selection) [cite: 42]
        btn.pack(side="right", padx=5)
        
        # Expose the hidden value via the identical .get() hook
        frame.get = lambda: frame.stored_value
        
    return frame

# Define run at the top level so it can be imported!
def run():
    if windows:
        # This grabs the actual window object of the first entry
        first_name = list(windows.keys())[0]
        # Start the loop using the first window object
        list(windows.values())[0].mainloop()
    else:
        reporterror(code="0x00", message="No windows existing!")

# init the stuff
if __name__ == "__main__":

    # sys.argv[0] is the script name, so we start at index 1
    args = sys.argv[1:]

    if "-t" in args or "--test" in args:
        window("aaa")
        label("aaa", text="testlabel")
        button("aaa", text="Click!", command=lambda: print("TEST! BUTTON CLICKED!"))
    elif "-h" in args or "--help" in args:
        print("		AzuraLang help\n azuralang [command] <value> or")
        print("\nazuralang")

    run()
