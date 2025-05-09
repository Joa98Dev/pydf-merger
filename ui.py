# Import the Tkinter and merger libraries
import tkinter as tk
from tkinter import filedialog, messagebox
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
