from tkinter import ttk as t
from ttkthemes import ThemedTk
import sys
import os
from colorama import Fore, Style
import pytoml
import traceback

# Initialize colorama
import colorama
colorama.init(autoreset=True)

windows = {}

def azura_exception_handler(exctype, value, tb):
    """Overrides Python's default crash behavior to catch missing functions cleanly."""
    if exctype is NameError:
        # Extract the line number where the NameError occurred
        # tb_next loops down the traceback stack to get to the actual execution line
        current_tb = tb
        while current_tb.tb_next:
            current_tb = current_tb.tb_next
        line_number = str(current_tb.tb_lineno)

        # Format a clear message showing what variable/function name is missing
        error_message = str(value)

        # Route it directly into your premium custom error engine!
        reporterror(
            code="0x02",
            message=error_message,
            er_line=line_number,
            err_type="Name / Reference Error"
        )

        # Optional: You can choose to exit or let the program try to continue.
        # Since missing names usually break the UI, a clean exit keeps the terminal neat:
        sys.exit(1)

    else:
        # If it's a completely different kind of error (like a SyntaxError),
        # let standard Python handle it normally so you can still debug it.
        sys.__excepthook__(exctype, value, tb)

# Tell Python to use your custom handler for all unhandled runtime crashes
sys.excepthook = azura_exception_handler


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
    print(f"{Style.BRIGHT}{Fore.RED}An error has acured at line {er_line}. Code: {code}")
    print(f"{Style.BRIGHT}{Fore.RED}{err_type} => {message}")
    print(f"{Style.BRIGHT}\033[38;5;208mThis error is indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang")
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
        widget = Text(frame, height=4, width=30, bg=_THEME["text_bg"], fg=_THEME["text_fg"], relief="flat", padx=5, pady=5)
        widget.pack(side="right", expand=True, fill="x", padx=5)
        frame.get = lambda: widget.get("1.0", "end").strip()

    elif input_type == "Select":
        frame.stored_value = ""
        value_label = t.Label(frame, text="None selected", relief="sunken", width=20)
        value_label.pack(side="left", padx=5, expand=True, fill="x")

        def handle_selection():
            if select_mode == "file":
                # Swapped to asksaveasfilename to force your native system file manager layout!
                filepath = filedialog.asksaveasfilename(title="Save As / Select File Location")
                if filepath:
                    frame.stored_value = filepath
                    # Cross-platform safe path splitter to keep the UI clean
                    frame.stored_value = filepath
                    value_label.config(text=os.path.basename(filepath))
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

    # 1. Look inside the execution namespace for 'run'
    if "run" not in globals() or not callable(globals()["run"]):
        # Safe fallback defaults if line or type isn't tracked yet
        reporterror(
            code="0x04",
            message="The core application execution hook 'run()' is missing from the workspace runtime!",
            er_line="N/A",
            err_type="Compilation / Namespace Error"
        )
        sys.exit(1) # Gracefully kill execution since the app can't start

    # 2. Continue with your normal boot routing blocks if it exists
    if "-t" in args or "--test" in args:
        window("aaa")
        label("aaa", text="testlabel")
        button("aaa", text="Click!", command=lambda: print("TEST! BUTTON CLICKED!"))
    elif "-h" in args or "--help" in args:
        print("		AzuraLang help\n azuralang [command] <value> or")
        print("\nazuralang")

    run()
