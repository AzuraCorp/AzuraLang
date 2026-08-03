import colorsys
import inspect
import subprocess
import os
from os import system
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
orangeColorForPrint = "\033[38;5;208m"

window_blueprints = {}
windows = {}

_THEME = {
    "win_bg": "#f5f6f7",     # Default flat light grey canvas style
    "label_fg": "#333333",   # Dark charcoal text
    "label_bg": "#f5f6f7",
    "entry_bg": "#ffffff",   # Solid white text cells
    "entry_fg": "#333333",
    "btn_bg": "#e1e1e1",     # Soft grey interactive buttons
    "btn_fg": "#000000"
}

def useDarkMode():
    """Modifies structural theme maps and applies custom native styles for dark mode."""
    global _THEME
    _THEME["win_bg"] = "#2b2b2b"    # Charcoal theme background canvas
    _THEME["label_fg"] = "#ffffff"  # High-contrast text
    _THEME["label_bg"] = "#2b2b2b"
    _THEME["entry_bg"] = "#3c3c3c"  # Dark grey input slots
    _THEME["entry_fg"] = "#ffffff"
    _THEME["btn_bg"] = "#4a4a4a"    # Dark interactive buttons
    _THEME["btn_fg"] = "#ffffff"

    # Configure global native TTK widget mapping changes for Dark Mode
    style = ttk.Style()
    style.theme_use('clam')  # Native cross-platform engine allowing custom coloration mapping
    style.configure('.', background="#2b2b2b", foreground="#ffffff")
    style.configure('TLabel', background="#2b2b2b", foreground="#ffffff")
    style.configure('TButton', background="#4a4a4a", foreground="#ffffff")

def reporterror(code="err.code", message="Test report! No errors found.", er_line: str | int = "!not detected", err_type="Test/Envierment Error"):
    if code == "0x00":
        print(f"{Style.BRIGHT}{Fore.CYAN}==AzuraLang Log==")
        print(f"{Style.BRIGHT}{Fore.RED}An error has occured at line {er_line}.")
        print(f"{Style.BRIGHT}{Fore.RED}[{code}]RuntimeError: {Style.NORMAL}{message}")
        print(f"{orangeColorForPrint}This error is a dev-error, it's indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues")
        print(f"{Style.RESET_ALL}")
        sys.exit(1)
    elif code == "0x01":
        print(f"{Style.BRIGHT}{Fore.CYAN}==AzuraLang Log==")
        print(f"{Style.BRIGHT}{Fore.RED}An error has occured at line {er_line}.")
        print(f"{Style.BRIGHT}{Fore.RED}[{code}]WindowLookupError: {Style.NORMAL}{message}")
        print(f"{orangeColorForPrint}This error is a dev-error, it's indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues")
        print(f"{Style.RESET_ALL}")
        sys.exit(1)
    elif code == "0x02":
        print(f"{Style.BRIGHT}{Fore.CYAN}==AzuraLang Log==")
        print(f"{Style.BRIGHT}{Fore.RED}An error has occured at line {er_line}.")
        print(f"{Style.BRIGHT}{Fore.RED}[{code}]NameError: {Style.NORMAL}{message}")
        print(f"{orangeColorForPrint}This error is a dev-error, it's indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues")
        print(f"{Style.RESET_ALL}")
        sys.exit(1)
    elif code == "0x03":
        print(f"{Style.BRIGHT}{Fore.CYAN}==AzuraLang Log==")
        print(f"{Style.BRIGHT}{Fore.RED}An error has occured at line {er_line}.")
        print(f"{Style.BRIGHT}{Fore.RED}[{code}]AtrributeValueNameError: {Style.NORMAL}{message}")
        print(f"{orangeColorForPrint}This error is a dev-error, it's indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues")
        print(f"{Style.RESET_ALL}")
        sys.exit(1)
    elif code == "0x04":
        print(f"{Style.BRIGHT}{Fore.CYAN}==AzuraLang Log==")
        print(f"{Style.BRIGHT}{Fore.RED}An error has occured at line {er_line}.")
        print(f"{Style.BRIGHT}{Fore.RED}[{code}]NamespaceError: {Style.NORMAL}{message}")
        print(f"{orangeColorForPrint}This error is a dev-error, it's indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues")
        print(f"{Style.RESET_ALL}")
        sys.exit(1)
    else:
        print(f"{Style.BRIGHT}{Fore.CYAN}==AzuraLang Log==")
        print(f"{Style.BRIGHT}{Fore.RED}An error has occured at line"+er_line)
        print(f"{Style.BRIGHT}{Fore.RED}[{code}]{err_type}: {message}")
        print(f"{orangeColorForPrint}This error is a dev-error, it's indeed fixable. If not, please file an issue at:\nhttps://github.com/AzuraCorp/AzuraLang/issues")
        print(f"{Style.RESET_ALL}")
        sys.exit(1)

def get_line_number():
    # .f_back gets the frame of the caller who called this function
    caller_frame = inspect.currentframe().f_back
    return caller_frame.f_lineno


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
            er_line={line_number},
            err_type="NameError"
        )
    else:
        # Pass non-NameErrors directly to standard Python crash handler tools
        sys.__excepthook__(exctype, value, tb)
# Assign our global error shield interceptor mapping directly to Python system core
sys.excepthook = azura_exception_handler

def registerWindow(name, builder_func):
    """Registers a function that builds the window."""
    window_blueprints[name] = builder_func

def openWindow(name):
    """Opens a window, creating it if it was destroyed."""
    # Check if it exists and is a valid Tkinter widget
    if name in windows and windows[name].winfo_exists():
        windows[name].deiconify()
        windows[name].lift() # Optional: Bring to front
    else:
        # If it doesn't exist (never created or destroyed), run the blueprint
        if name in window_blueprints:
            print(f"Creating fresh instance of '{name}'...")
            windows[name] = window_blueprints[name]()
        else:
            print(f"Error: No blueprint found for '{name}'")

# noinspection PyPep8Naming
def window(Name, title="Window", size="400x300", icon=None, silentFail=False):
    """Creates a base window instance utilizing standard Tkinter windows as containers."""
    win = tk.Tk()  # Replaced legacy ThemedTk reference
    win.title(title)
    win.geometry(size)
    win.configure(bg=_THEME["win_bg"])

    if icon:
        try:
            # For Windows .ico files
            win.iconbitmap(icon)
        except Exception:
            # Fallback for other formats (like .png) on other platforms
            try:
                icon_img = tk.PhotoImage(file=icon)
                win.iconphoto(True, icon_img)
            except Exception as e:
                print(f"Could not load icon: {e}")
                if not silentFail:
                    reporterror(code="0x03", message=f"File \"{icon}\" not found! Maybe you forgot to add \"./\" at the start?")

    # Initialize basic native TTK layout styles for default setups
    style = ttk.Style(win)
    if _THEME["win_bg"] == "#2b2b2b":
        style.theme_use('clam')
        style.configure('.', background="#2b2b2b", foreground="#ffffff")
    else:
        style.theme_use('default')

    windows[Name] = win
    return win

def label(inWinName, text="label", **kwargs):
    """Renders a standard clean layout tracking system text inside TTK."""
    parent = windows.get(inWinName)

    if parent:
        # Check if user provided custom colors, otherwise use the theme defaults
        if 'bg' not in kwargs and 'background' not in kwargs:
            kwargs['bg'] = _THEME["label_bg"]
        if 'fg' not in kwargs and 'foreground' not in kwargs:
            kwargs['fg'] = _THEME["label_fg"]

        lbl = tk.Label(parent, text=text, **kwargs)
        lbl.pack(pady=5)
        return lbl
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!", er_line={get_line_number()}, err_type="Window Lookup Error")
        return None


def button(inWinName, text="button", command=lambda: print('Hello, World!')):
    """Renders an interactive system action button using TTK styling structures."""
    parent = windows.get(inWinName)
    if parent:
        btn = ttk.Button(parent, text=text, command=command)  # Native TTK element mapping
        btn.pack(pady=5)
        return btn
    else:
        reporterror(code="0x01", message=f"Window '{inWinName}' not found!", er_line={get_line_number()}, err_type="Window Lookup Error")
        return None

class AzuraColorPicker(tk.Toplevel):
    """Modern color picker modal defaulting to HSV with switchable RGB support."""
    def __init__(self, parent, title="Choose Color", initial_color="#3b82f6"):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)

        # Modal configuration
        self.transient(parent)
        self.grab_set()

        self.selected_color = None
        self.current_hex = initial_color if (initial_color and initial_color.startswith("#")) else "#3b82f6"

        # Default mode: "HSV"
        self.mode_var = tk.StringVar(value="HSV")

        # Slider variables
        self.val1_var = tk.IntVar()
        self.val2_var = tk.IntVar()
        self.val3_var = tk.IntVar()
        self.hex_var = tk.StringVar(value=self.current_hex)

        # Internal RGB state (0-255)
        self.r, self.g, self.b = 59, 130, 246

        # Preset Swatches
        self.presets = [
            "#ef4444", "#f97316", "#f59e0b", "#10b981",
            "#06b6d4", "#3b82f6", "#6366f1", "#a855f7",
            "#ec4899", "#111827", "#6b7280", "#ffffff"
        ]

        self._build_ui()
        self._parse_hex_and_update(self.current_hex)

        # Centre relative to parent
        self.geometry(f"+{parent.winfo_rootx() + 40}+{parent.winfo_rooty() + 40}")

        # Halt execution until user accepts or cancels
        self.wait_window(self)

    def _build_ui(self):
        container = ttk.Frame(self, padding=15)
        container.pack(fill="both", expand=True)

        # Top Bar: Preview & Hex Field
        top_frame = ttk.Frame(container)
        top_frame.pack(fill="x", pady=(0, 10))

        self.preview_box = tk.Frame(top_frame, width=110, height=45, relief="solid", bd=1)
        self.preview_box.pack(side="left", padx=(0, 10))
        self.preview_box.pack_propagate(False)

        hex_frame = ttk.Frame(top_frame)
        hex_frame.pack(side="left", fill="x", expand=True)

        ttk.Label(hex_frame, text="HEX Code:", font=("sans-serif", 9, "bold")).pack(anchor="w")
        hex_entry = ttk.Entry(hex_frame, textvariable=self.hex_var, width=10)
        hex_entry.pack(anchor="w", pady=(2, 0))
        hex_entry.bind("<KeyRelease>", self._on_hex_entry)

        # Mode Selector Radio Buttons
        mode_frame = ttk.Frame(container)
        mode_frame.pack(fill="x", pady=(0, 5))

        ttk.Label(mode_frame, text="Color Model:", font=("sans-serif", 9, "bold")).pack(side="left")
        ttk.Radiobutton(
            mode_frame, text="HSV", value="HSV",
            variable=self.mode_var, command=self._on_mode_change
        ).pack(side="left", padx=(10, 5))

        ttk.Radiobutton(
            mode_frame, text="RGB", value="RGB",
            variable=self.mode_var, command=self._on_mode_change
        ).pack(side="left")

        # Sliders Section
        self.sliders_frame = ttk.LabelFrame(container, text=" Adjust Color ", padding=10)
        self.sliders_frame.pack(fill="x", pady=5)

        self.lbl1 = ttk.Label(self.sliders_frame, text="", width=8)
        self.lbl2 = ttk.Label(self.sliders_frame, text="", width=8)
        self.lbl3 = ttk.Label(self.sliders_frame, text="", width=8)

        self.scale1 = ttk.Scale(self.sliders_frame, variable=self.val1_var, command=lambda e: self._on_slider_change())
        self.scale2 = ttk.Scale(self.sliders_frame, variable=self.val2_var, command=lambda e: self._on_slider_change())
        self.scale3 = ttk.Scale(self.sliders_frame, variable=self.val3_var, command=lambda e: self._on_slider_change())

        for lbl, scale, var in [
            (self.lbl1, self.scale1, self.val1_var),
            (self.lbl2, self.scale2, self.val2_var),
            (self.lbl3, self.scale3, self.val3_var)
        ]:
            row = ttk.Frame(self.sliders_frame)
            row.pack(fill="x", pady=3)
            lbl.master = row
            scale.master = row

            lbl.pack(side="left")
            scale.pack(side="left", fill="x", expand=True, padx=5)
            ttk.Label(row, textvariable=var, width=4).pack(side="right")

        # Quick Presets Palette
        swatch_frame = ttk.LabelFrame(container, text=" Quick Presets ", padding=8)
        swatch_frame.pack(fill="x", pady=5)

        grid_frame = ttk.Frame(swatch_frame)
        grid_frame.pack(anchor="center")

        for idx, hex_code in enumerate(self.presets):
            btn = tk.Button(
                grid_frame, bg=hex_code, activebackground=hex_code,
                width=3, height=1, relief="flat", bd=1,
                command=lambda c=hex_code: self._select_preset(c)
            )
            btn.grid(row=idx // 6, column=idx % 6, padx=3, pady=3)

        # Dialog Buttons
        btn_frame = ttk.Frame(container)
        btn_frame.pack(fill="x", pady=(10, 0))

        ttk.Button(btn_frame, text="Cancel", command=self.destroy).pack(side="right", padx=(5, 0))
        ttk.Button(btn_frame, text="OK", command=self._apply).pack(side="right")

    def _configure_slider_bounds(self):
        """Sets bounds and labels dynamically based on HSV or RGB selection."""
        mode = self.mode_var.get()
        if mode == "HSV":
            self.lbl1.config(text="Hue (°):")
            self.lbl2.config(text="Sat (%):")
            self.lbl3.config(text="Val (%):")
            self.scale1.config(from_=0, to=360)
            self.scale2.config(from_=0, to=100)
            self.scale3.config(from_=0, to=100)
        else: # RGB
            self.lbl1.config(text="Red:")
            self.lbl2.config(text="Green:")
            self.lbl3.config(text="Blue:")
            self.scale1.config(from_=0, to=255)
            self.scale2.config(from_=0, to=255)
            self.scale3.config(from_=0, to=255)

    def _sync_sliders_from_rgb(self):
        self._configure_slider_bounds()
        mode = self.mode_var.get()

        # 1. Lock the listener to prevent infinite loops
        self.is_syncing = True

        if mode == "HSV":
            h, s, v = colorsys.rgb_to_hsv(self.r / 255.0, self.g / 255.0, self.b / 255.0)
            v1, v2, v3 = int(round(h * 360)), int(round(s * 100)), int(round(v * 100))
        else:
            v1, v2, v3 = self.r, self.g, self.b

        # 2. Update the numeric text labels
        self.val1_var.set(v1)
        self.val2_var.set(v2)
        self.val3_var.set(v3)

        # 3. CRITICAL FIX: Force the physical slider handles to move!
        self.scale1.set(v1)
        self.scale2.set(v2)
        self.scale3.set(v3)

        # 4. Unlock the listener
        self.is_syncing = False

    def _on_slider_change(self):
        # Prevent infinite loops when the script updates the sliders programmatically
        if getattr(self, 'is_syncing', False):
            return

        mode = self.mode_var.get()

        # Force the raw slider float values into clean integers
        v1 = int(round(self.scale1.get()))
        v2 = int(round(self.scale2.get()))
        v3 = int(round(self.scale3.get()))

        # Update the labels immediately to reflect the snapped integer
        self.val1_var.set(v1)
        self.val2_var.set(v2)
        self.val3_var.set(v3)

        # Convert based on active mode
        if mode == "HSV":
            r_norm, g_norm, b_norm = colorsys.hsv_to_rgb(v1 / 360.0, v2 / 100.0, v3 / 100.0)
            self.r, self.g, self.b = int(r_norm * 255), int(g_norm * 255), int(b_norm * 255)
        else:
            self.r, self.g, self.b = v1, v2, v3

        self.current_hex = f"#{self.r:02x}{self.g:02x}{self.b:02x}"
        self.hex_var.set(self.current_hex)
        self.preview_box.configure(bg=self.current_hex)

    def _on_mode_change(self):
        self._sync_sliders_from_rgb()

    def _parse_hex_and_update(self, hex_str):
        hex_str = hex_str.strip().lstrip('#')
        if len(hex_str) == 6:
            try:
                self.r = int(hex_str[0:2], 16)
                self.g = int(hex_str[2:4], 16)
                self.b = int(hex_str[4:6], 16)
                self.current_hex = f"#{hex_str}"
                self.preview_box.configure(bg=self.current_hex)
                self._sync_sliders_from_rgb()
            except ValueError:
                pass

    def _on_hex_entry(self):
        self._parse_hex_and_update(self.hex_var.get())

    def _select_preset(self, hex_code):
        self.hex_var.set(hex_code)
        self._parse_hex_and_update(hex_code)

    def _apply(self):
        self.selected_color = self.current_hex
        self.destroy()

def guiInput(inWinName, text="", inputType="textString", selectMode="file", initialColor="#000000"):
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

    # Normalize input_type to avoid case-sensitivity bugs (e.g., "Select" vs "select")
    input_type_lower = inputType.lower()

    # 3. Handle specific Input Type rendering layouts manually
    if input_type_lower == "textstring":
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

    elif input_type_lower == "textbox":
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

    elif input_type_lower == "select":
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
            if selectMode == "file":
                filepath = filedialog.asksaveasfilename(title="Save As / Select File Location")
                if filepath:
                    frame.stored_value = filepath
                    value_label.config(text=os.path.basename(filepath))

            elif selectMode == "color":
                # Create the picker window instance
                picker_window = AzuraColorPicker(parent, initial_color=initialColor)

                # Fetch the selected_color property AFTER the window closes
                hex_color = picker_window.selected_color

                if hex_color:
                    frame.stored_value = hex_color
                    value_label.config(text=hex_color)

        button_title = f"Choose {selectMode.capitalize()}"
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

    else:
        reporterror(code="0x03", message=f"guiInput's attribute \"inputType\" doesn't have the value \"{inputType}\"!", err_type="AtrributeValueNameError")
    return frame



'''=====SEPARATE HERE, END!!!====='''

def run(main_window_name):
    if main_window_name and main_window_name in windows:
        windows[main_window_name].mainloop()
    else:
        print("Error: No valid main window specified for run().")
        reporterror(code="0x01", message=f"Window '{main_window_name}' not found!", er_line={get_line_number()})

if __name__ == "__main__":
    args = sys.argv[1:]

    # Pre-flight environment verify checks
    if "run" not in globals() or not callable(globals()["run"]):
        reporterror(code="0x04", message="The core run() loop execution system is missing!", er_line={get_line_number()}, err_type="NamespaceError")

    # Local diagnostic argument checking
    if "-t" in args or "--test" in args:
        subprocess.run("sh ./tests/test.sh", shell=True)
