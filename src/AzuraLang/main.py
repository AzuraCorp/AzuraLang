from tkinter import ttk as t
from ttkthemes import ThemedTk
import sys
import os
from colorama import Fore, Style
import pytoml

# Initialize colorama
import colorama
colorama.init(autoreset=True)

windows = {}

# Global theme dictionary to sync ttkthemes and layout background colors automatically
_THEME = {
    "name": "arc",        # Default light theme
    "win_bg": "#f5f6f7",  # Light background color for the main window canvas
    "label_fg": "#333333",# Dark text for light mode readability
    "text_bg": "#ffffff", # Default TextBox background
    "text_fg": "#333333"  # Default TextBox text color
}

# AUTO-PASS DARK THEME FUNCTION
def useDarkMode():
    """Switches the entire engine layout configuration to a dark theme."""
    global _THEME
    _THEME["name"] = "equilux"     # Sleek dark mode theme from ttkthemes
    _THEME["win_bg"] = "#3c3c3c"   # Pure Equilux layout background hex color
    _THEME["label_fg"] = "#ffffff" # Crisp white text color for dark mode labels
    _THEME["text_bg"] = "#2b2b2b"  # Dark gray background for legacy Text widgets
    _THEME["text_fg"] = "#ffffff"  # Crisp white text for readability

# Make the window...
def window(Name, title="Window", size="100x200"):
    # Automatically pulls whichever theme name is globally active
    win = ThemedTk(theme=_THEME["name"])
    win.title(title)
    win.geometry(size)

    # --- GLOBAL STYLE OVERRIDES FOR TTK THEME CLEANLINESS ---
    # Create a style engine mapping bound directly to this window instance
    style = t.Style(win)

    # Dynamically configure styles to completely wipe out any light-gray artifact blocks
    style.configure("TLabel", background=_THEME["win_bg"], foreground=_THEME["label_fg"])
    style.configure("TFrame", background=_THEME["win_bg"])

    # Configure the underlying root Tkinter frame color to seamlessly blend with the style palette
    win.configure(bg=_THEME["win_bg"])
    # ---------------------------------------------------------

    windows[Name] = win
    return win

# RARARRARARARARARARARARA
def reporterror(code="err.code", message="Test report! No errors found.", er_line=str(0), err_type="Test/Enviermont Error"):
    print(f"{Style.BRIGHT}{Fore.CYAN}AzuraLang(GUI) Log:")
    print(f"{Style.BRIGHT}{Fore.RED}An error has accured at line {er_line}. Code: {code}")
    print(f"{Style.BRIGHT}{Fore.RED}{err_type} => {message}")
    print(f"{Style.BRIGHT}\033[38;5;208mThis arror is indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang")
    print(f"{Style.RESET_ALL}")

# Make the label widget
def label(inWinName, text="label"):
    parent = windows.get(inWinName)
    if parent:
        lbl = t.Label(parent, text=text)
        lbl.pack() 
        return lbl
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")

# Make the button widget
def button(inWinName, text="button", command=lambda: print('Hello, World!')):
    parent = windows.get(inWinName)
    if parent:
        btn = t.Button(parent, text=text, command=command)
        btn.pack() 
        return btn
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")

# Make an input widget (guiInput())
def guiInput(inWinName, text="", input_type="TextString", select_mode="file"):
    from tkinter import Text, filedialog, colorchooser
    
    parent = windows.get(inWinName)
    if not parent:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!")
        return None
        
    frame = t.Frame(parent)
    frame.pack(fill="x", padx=5, pady=5)
    
    if text:
        lbl = t.Label(frame, text=text)
        lbl.pack(side="left", padx=5)
        
    if input_type == "TextString":
        widget = t.Entry(frame)
        widget.pack(side="right", expand=True, fill="x", padx=5)
        frame.get = widget.get
        
    elif input_type == "TextBox":
        # Automatically inherits global text layout colors to completely prevent background clashing!
        widget = Text(frame, height=4, width=30, bg=_THEME["text_bg"], fg=_THEME["text_fg"], relief="flat", padx=5, pady=5)
        widget.pack(side="right", expand=True, fill="x", padx=5)
        frame.get = lambda: widget.get("1.0", "end").strip()
        
    elif input_type == "Select":
        frame.stored_value = ""
        value_label = t.Label(frame, text="None selected", relief="sunken", width=20)
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
        btn = t.Button(frame, text=button_title, command=handle_selection)
        btn.pack(side="right", padx=5)
        
        frame.get = lambda: frame.stored_value
        
    return frame

def run():
    if windows:
        list(windows.values())[0].mainloop()
    else:
        reporterror(code="0x00", message="No windows existing!")

if __name__ == "__main__":
    args = sys.argv[1:]

    if "-t" in args or "--test" in args:
        window("aaa")
        label("aaa", text="testlabel")
        button("aaa", text="Click!", command=lambda: print("TEST! BUTTON CLICKED!"))
    elif "-h" in args or "--help" in args:
        print("		AzuraLang help\n azuralang [command] <value> or")
        print("\nazuralang")

    run()
