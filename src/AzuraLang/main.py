import sys
import os
import traceback
import tkinter as tk
from tkinter import ttk  # Standard native engine components
from tkinter import filedialog, colorchooser
from tkinterweb import HtmlFrame
from colorama import Fore, Style
import colorama
import inspect

colorama.init(autoreset=True)

# Global framework window registry mapping
windows = {}

# Master theme configuration mapping for raw tk widgets and window backdrops
_THEME = {
    "win_bg": "#f5f6f7",     # Default flat light grey canvas style
    "label_fg": "#333333",   # Dark charcoal text
    "entry_bg": "#ffffff",   # Solid white text cells
    "entry_fg": "#333333",
    "btn_bg": "#e1e1e1",     # Soft grey interactive buttons
    "btn_fg": "#000000"
}

def get_line_number():
    # .f_back gets the frame of the caller who called this function
    caller_frame = inspect.currentframe().f_back
    return caller_frame.f_lineno

def useDarkMode():
    """Modifies structural theme maps and applies custom native styles for dark mode."""
    global _THEME
    _THEME["win_bg"] = "#2b2b2b"    # Charcoal theme background canvas
    _THEME["label_fg"] = "#ffffff"  # High-contrast text
    _THEME["entry_bg"] = "#3c3c3c"  # Dark gray input slots
    _THEME["entry_fg"] = "#ffffff"
    _THEME["btn_bg"] = "#4a4a4a"    # Dark interactive buttons
    _THEME["btn_fg"] = "#ffffff"

    # Configure global native TTK widget mapping changes for Dark Mode
    style = ttk.Style()
    style.theme_use('clam')  # Native cross-platform engine allowing custom coloration mapping
    style.configure('.', background="#2b2b2b", foreground="#ffffff")
    style.configure('TLabel', background="#2b2b2b", foreground="#ffffff")
    style.configure('TButton', background="#4a4a4a", foreground="#ffffff")

def reporterror(code="err.code", message="Test report! No errors found.", er_line={get_line_number()}, err_type="Test/Enviermont Error"):
    print(f"{Style.BRIGHT}{Fore.CYAN}AzuraLang(GUI) Log:")
    print(f"{Style.BRIGHT}{Fore.RED}An error has acured at line {er_line}. Code: {code}")
    print(f"{Style.BRIGHT}{Fore.RED}{err_type} => {message}")
    print(f"{Style.BRIGHT}\033[38;5;208mThis error is indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issiues")
    print(f"{Style.RESET_ALL}")
    sys.exit(1)


def azura_exception_handler(exctype, value, tb):
    """Intercepts unhandled NameErrors and formats them cleanly inside the framework engine."""
    if exctype is NameError:
        current_tb = tb
        while current_tb.tb_next:
            current_tb = current_tb.tb_next
        line_number = str(current_tb.tb_lineno)

        error_message = str(value)
        reporterror(
            code="0x02",
            message=error_message,
            er_line={get_line_number()},
            err_type="Name / Reference Error"
        )
    else:
        # Pass non-NameErrors directly to standard Python crash handler tools
        sys.__excepthook__(exctype, value, tb)

# Assign our global error shield interceptor mapping directly to Python system core
sys.excepthook = azura_exception_handler

def window(Name, title="Window", size="400x300"):
    """Creates a base window instance utilizing standard Tkinter windows as containers."""
    win = tk.Tk()  # Replaced legacy ThemedTk reference
    win.title(title)
    win.geometry(size)
    win.configure(bg=_THEME["win_bg"])

    # Initialize basic native TTK layout styles for default setups
    style = ttk.Style(win)
    if _THEME["win_bg"] == "#2b2b2b":
        style.theme_use('clam')
        style.configure('.', background="#2b2b2b", foreground="#ffffff")
    else:
        style.theme_use('default')

    windows[Name] = win
    return win

def label(inWinName, text="label"):
    """Renders a standard clean layout tracking system text inside TTK."""
    parent = windows.get(inWinName)
    if parent:
        lbl = ttk.Label(parent, text=text)  # Native TTK element mapping
        lbl.pack(pady=5)
        return lbl
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!", er_line={get_line_number()}, err_type="Window Lookup Error")

def button(inWinName, text="button", command=lambda: print('Hello, World!')):
    """Renders an interactive system action button using TTK styling structures."""
    parent = windows.get(inWinName)
    if parent:
        btn = ttk.Button(parent, text=text, command=command)  # Native TTK element mapping
        btn.pack(pady=5)
        return btn
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!", er_line={get_line_number()}, err_type="Window Lookup Error")

def guiInput(inWinName, text="", input_type="TextString", select_mode="file"):
    """Returns a pure raw tk.Frame containing manually colored widgets to allow flat custom sizing."""
    parent = windows.get(inWinName)
    if not parent:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!", er_line={get_line_number()}, err_type="Window Lookup Error")
        return None

    # 1. Use a raw tk.Frame container to isolate geometry properties from styling engines
    frame = tk.Frame(parent, bg=_THEME["win_bg"])
    frame.pack(fill="x", padx=5, pady=5)

    # 2. Raw tk.Label for explicit color overrides
    if text:
        lbl = tk.Label(frame, text=text, bg=_THEME["win_bg"], fg=_THEME["label_fg"])
        lbl.pack(side="left", padx=5)

    # 3. Handle specific Input Type rendering layouts manually
    if input_type == "TextString":
        widget = tk.Entry(
            frame,
            bg=_THEME["entry_bg"],
            fg=_THEME["entry_fg"],
            insertbackground=_THEME["entry_fg"],
            relief="solid",
            bd=1
        )
        widget.pack(side="right", expand=True, fill="x", padx=5)
        frame.get = widget.get

    elif input_type == "TextBox":
        widget = tk.Text(
            frame,
            height=4,
            width=30,
            bg=_THEME["entry_bg"],
            fg=_THEME["entry_fg"],
            insertbackground=_THEME["entry_fg"],
            relief="solid",
            bd=1,
            padx=5,
            pady=5
        )
        widget.pack(side="right", expand=True, fill="x", padx=5)
        frame.get = lambda: widget.get("1.0", "end").strip()

    elif input_type == "Select":
        frame.stored_value = ""
        value_label = tk.Label(
            frame,
            text="None selected",
            relief="solid",
            bd=1,
            width=20,
            bg=_THEME["entry_bg"],
            fg=_THEME["entry_fg"]
        )
        value_label.pack(side="left", padx=5, expand=True, fill="x")

        def handle_selection():
            if select_mode == "file":
                filepath = filedialog.asksaveasfilename(title="Save As / Select File Location")
                if filepath:
                    frame.stored_value = filepath
                    value_label.config(text=os.path.basename(filepath))
            elif select_mode == "color":
                color_code = colorchooser.askcolor(title="Select Color")[1]
                if color_code:
                    frame.stored_value = color_code
                    value_label.config(text=color_code)

        button_title = f"Choose {select_mode.capitalize()}"
        btn = tk.Button(
            frame,
            text=button_title,
            command=handle_selection,
            bg=_THEME["btn_bg"],
            fg=_THEME["btn_fg"],
            relief="flat",
            activebackground=_THEME["btn_bg"]
        )
        btn.pack(side="right", padx=5)

        frame.get = lambda: frame.stored_value

    return frame

def webDisplay(inWinName, url="https://google.com", bg="#2b2b2b"):

    parent = windows.get(inWinName)
    if not parent:
        reporterror(
            code="0x01",
            message=f"Window '{inWinName}' not found!",
            er_line={get_line_number()},
            err_type="Window Lookup Error"
        )
        return None

    containerDisplay = tk.Frame(parent, bg=bg)
    containerDisplay.pack(fill="both", expand=True, padx=5, pady=5)

    browser = HtmlFrame(wrapper)
    browser.pack(fill="both", expand=True)

    if url.startswith("http://") or url.startswith("https://"):
        browser.load_url(url)
    else:
        browser.load_file(url)

    return containerDisplay


'''=====SEPARATE HERE, END!!!====='''

def run():
    """Starts the application window loop sequence."""
    if windows:
        list(windows.values())[0].mainloop()
    else:
        reporterror(code="0x00", message="No active window instances exist to execute!", er_line={get_line_number()}, err_type="Runtime Error")

if __name__ == "__main__":
    args = sys.argv[1:]

    # Pre-flight environment verify checks
    if "run" not in globals() or not callable(globals()["run"]):
        reporterror(code="0x04", message="The core run() loop execution system is missing!", er_line={get_line_number()}, err_type="Namespace Error")
        sys.exit(1)

    # Local diagnostic argument checking
    if "-t" in args or "--test" in args:
        useDarkMode()  # Test global dark layout setups seamlessly

        window("main_canvas", title="Azura Lang Native Environment Test", size="500x400")
        label("main_canvas", text="Testing System-Native UI Elements (TTK)")

        # Elements processed cleanly through the custom pure tk design mapping parameters
        guiInput("main_canvas", text="Input Command String:", input_type="TextString")
        io = guiInput("main_canvas", text="Target Compilation Directory:", input_type="Select", select_mode="file")

        button("main_canvas", text="Confirm Workspace Launch", command=lambda: print("Framework Engine Diagnostic Check Clear."))

    run()
