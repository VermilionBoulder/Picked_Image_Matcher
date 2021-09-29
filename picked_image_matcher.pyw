#! "C:\\Users\\ksurowka\\PycharmProjects\\FileRenamer\\venv\\Scripts\\pythonw.exe"
# Modify the path above to lead to the desired pythonw.exe interpreter executable.
# This will prevent the script from opening a Python console window.
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox


def main():
    cwd = os.getcwd()
    files = []
    file_list = os.listdir()

    # No 'raw' folder in cwd
    if 'raw' not in file_list:
        root = tk.Tk()
        root.overrideredirect(1)
        root.withdraw()
        messagebox.showerror(title="Error",
                             message=f"No 'raw' folder found. Please rename the folder with RAW files\n"
                                     f"to that name. The program cannot proceed otherwise.")
        root.destroy()
        return 1

    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    dialog = messagebox.askokcancel(title="Warning",
                                    message=f"This operation will create a separate folder for RAWs and move\n"
                                            f"the ones from the 'raw' folder matching the JPG filenames into it.\n"
                                            f"This cannot be undone. Proceed?")
    root.destroy()

    if dialog:
        padding = len(str(len(file_list)))

        for file in os.listdir():
            files.append((datetime.fromtimestamp(os.path.getmtime(file)),
                          file,
                          file.split('.')[-1]))

        for idx, file_entry in enumerate(files, start=1):
            _, filename, extension = file_entry
            os.rename(filename, f"{cwd}\\{idx:0>{padding}}.{extension}")


if __name__ == "__main__":
    main()
