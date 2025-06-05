# Import the Tkinter and merger libraries
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
from merger import merge_pdfs

# Class that manage all the program logic
class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyDF Merger") # Window title
        self.pdf_files = [] # Internal list that store selected PDF paths

        # Set up the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Create a menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Add a Help button with an "About" option
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.about_window)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Button to add PDF files
        self.add_button = tk.Button(self.root, text="Add PDFs", command=self.add_files)
        self.add_button.pack(pady=5)

        # Button to merge PDF files
        self.merge_button = tk.Button(self.root, text="Merge PDFs", command=self.merge)
        self.merge_button.pack(pady=5)
        
        # Button to remove the selected PDF file
        self.remove_button = tk.Button(self.root, text="Remove PDFs", command=self.remove_selected)
        self.remove_button.pack(pady=5)

        # Display the selected PDF files
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=5)

    def about_window(self):
        about_win = tk.Toplevel(self.root)
        about_win.title("About PyDF Merger")
        about_win.geometry("300x160")
        about_win.resizable(False, False)

        tk.Label(about_win, text="PyDF Merger v1.4.0", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        tk.Label(about_win, text="A simple open-source tool to merge PDF files.", wraplength=280).pack(pady=5)

        tk.Label(about_win, text="Author: Joa98", font=("Arial", 10)).pack(pady=(5,0))
        tk.Label(about_win, text="License: MIT", font=("Arial", 10)).pack(pady=(0,5))
        
        
        # Project's link
        link = tk.Label(about_win, text="GitHub Repository", fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Joa98Dev/pydf-merger"))  # Repository link

        tk.Button(about_win, text="Close", command=about_win.destroy).pack(pady=10)

    def add_files(self):
        # Open file dialog to select multiple PDF files
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file)

    def merge(self):
        # If listbox empty it will show an error.
        if not self.pdf_files:
            messagebox.showerror("Error", "You have not added PDF files.")
            return

        # Verify that there are at lest two PDF files selected before merging
        if len(self.pdf_files) < 2:
            messagebox.showwarning("Warning", "Select at least two PDF files.")
            return

        # Ask where to save the merged PDF
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
        if output_file:
            try:
                # Call the merging logic from merger.py
                merge_pdfs(self.pdf_files, output_file)
                messagebox.showinfo("Done!", f"PDF Merged: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def remove_selected(self):
        # Get selected listbox entries
        selected_index = self.listbox.curselection()

        # If nothing is selected, do nothing
        if not selected_index:
            return

        # Delete selected PDF from listbox
        for index in reversed(selected_index):
            self.listbox.delete(index)
            del self.pdf_files[index]
