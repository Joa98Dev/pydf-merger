# Import the PdfWriter feature from pydf library
from pypdf import PdfWriter

'''
Merges multiple PDF files into a single file.
'''
def merge_pdfs(pdf_path, output_path):
    merger = PdfWriter() # Create a merger object

    # Add each PDF to the merger
    for pdf in pdf_path:
        merger.append(pdf)

    # Write the merged content to the specified output path
    merger.write(output_path)

    # Always close the merger to free system resources
    merger.close()
