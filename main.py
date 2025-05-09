'''
---------------------------------
PyDF Merger - PDF Merger Program
---------------------------------

Version: 1.3.2

Author: Joa98

Email: joaquinpuente98@gmail.com

----------------------------------
MIT License

Copyright (c) 2025 Joaquín Puente.
----------------------------------
'''

# Import the GUI module (tkinter)
import tkinter as tk

# Import the PdfMergerApp class
from ui import PdfMergerApp

# This block ensures that the program only runs when is executed with this file
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()

    # Instance pdfMergerApp class
    app = PdfMergerApp(root)

    # Manage window size and prevent the resizing feature
    root.geometry("447x398")
    root.resizable(False, False)

    # Kepps the app running
    root.mainloop()
