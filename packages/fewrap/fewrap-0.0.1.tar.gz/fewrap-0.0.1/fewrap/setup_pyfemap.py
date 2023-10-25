r"""
This script is used to set up the FEMAP API for Python.

Before you can start working with the FEMAP API in Python, you need to transfer the FEMAP API type library into
something Python can read.

If you upgrade to a newer version of Python or FEMAP, you should re-run this script. Otherwise, once it's installed,
you're good to go.

Pyfemap Setup Instructions:
---------------------------
1.  Recommend that you have Python 3.9 or newer installed.

2.  Install the pywin32 module if you don't have it already. If you don't, open command prompt and type
        pip install pywin32
    Or if using Anaconda:
        conda install -c anaconda pywin32

3.  Run this script directly.
        - To run from Command Prompt: Navigate to the directory where this script is located and type:
            python setup_pyfemap.py

        - Or to run from Python Shell:
            from fewrap import setup_pyfemap
                setup_pyfemap.main()

4.  Follow the GUI instructions and select the femap.tlb file in your Femap installation directory.

5.  A Pyfemap.py file will be created and placed in \\Lib folder in the Python installation directory.
"""
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

try:
    from win32com.client import makepy
except ModuleNotFoundError as e:
    print(
        'Could not import win32com.client. Please install pywin32 and try again.'
        'You can install pywin32 by entering the following in command prompt:\n'
        'pip install pywin32')


def _make_pyfemap(tlb_file_path: str) -> None:
    """Generates the Pyfemap.py file needed for Python to work with the FEMAP API.

    Will try to create the Pyfemap.py file in your \\Lib folder in the Python installation directory. If we can't find
    it, the file will be placed in the current working directory. Regardless, the location of the created file
    will be printed to the console.

    Parameters
    ----------
    tlb_file_path
        Path to the femap.tlb file.
    """
    lib_path = Path(sys.base_prefix) / "Lib"

    pyfemap_path = lib_path / "Pyfemap.py" if lib_path.exists() else Path(os.getcwd()) / "Pyfemap.py"

    sys.argv = ["makepy", "-o", str(pyfemap_path), tlb_file_path]
    makepy.main()

    if pyfemap_path.exists():
        print(f"Pyfemap.py file generated successfully at {pyfemap_path}")
    else:
        print("Could not generate Pyfemap.py file")

    try:
        import Pyfemap
    except ImportError as fe_error:
        print(f"Could not import Pyfemap.py file. Please check the path to the Pyfemap.py file in your Python "
              f"installation directory. {fe_error}")
    return


class _FileSelectorGUI:
    """A GUI for selecting a file from the user's computer and returning the path to the selected file.
    """
    def __init__(self, instructions_to_user: str = 'Select File', file_desired: str = ""):
        self.instructions = instructions_to_user
        self.file_desired = file_desired
        self.file_selected = None

        # Logic to determine the file extension
        if self.file_desired:
            if self.file_desired.startswith("."):
                self.extension = self.file_desired
            else:
                self.extension = os.path.splitext(self.file_desired)[1]

        # Initialize the tkinter window
        self.root = tk.Tk()
        self.root.title("File Selector")

        # Create a label for instructions
        self.instruction_label = tk.Label(self.root, text=self.instructions)
        self.instruction_label.pack(pady=10, fill=tk.X)

        # Create a button to open file dialog and an entry to show the file path
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT, padx=5)
        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.pack(side=tk.LEFT, padx=5, pady=20, fill=tk.X, expand=True)

        # Create the OK and Cancel buttons
        self.ok_button = tk.Button(self.root, text="OK", command=self.submit)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=20)
        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.root.destroy)
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=20)

    def browse_file(self):
        # Open the file selection dialog and get the selected file's path
        if self.file_desired:
            file_chosen = filedialog.askopenfilename(
                title=f"Select {self.file_desired} file",
                filetypes=((f"{self.file_desired} files", f"*{self.extension}"), ("All Files", "*.*"))
            )
        else:
            file_chosen = filedialog.askopenfilename(title=f"Select {self.file_desired} file")

        # Check if the selected file has the correct extension
        if not file_chosen.lower().endswith(self.file_desired):
            self.show_error_message('Invalid file')
            return  # Exit the function early if the file doesn't have the correct extension

        # Update the entry widget with the selected file path
        if file_chosen:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_chosen)

    def submit(self):
        self.file_selected = self.file_entry.get()
        if self.file_selected:
            print(f"Selected file: {Path(self.file_selected)}")
            self.root.destroy()
            return self.file_selected
        else:
            messagebox.showerror("Select a file", f"Please select a {self.file_desired} file.")

    def show_error_message(self, error_title):
        messagebox.showerror(error_title, f"Please select a {self.file_desired} file.")

    def run(self):
        self.root.mainloop()
        return self.file_selected


def main():
    instructions = "Select the femap.tlb file to generate the Pyfemap.py file.\n"\
                   "It should be located in the same directory as the femap.exe file"
    file_type = "femap.tlb"
    tlb_file = _FileSelectorGUI(instructions, file_type).run()
    if os.path.exists(tlb_file):
        _make_pyfemap(tlb_file)
    else:
        print(f"Could not find {tlb_file}")
        print(f"Please make sure that the femap.tlb path selected is correct")


if __name__ == "__main__":
    main()






