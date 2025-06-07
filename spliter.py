# Import the PdfReader and PdfWriter feature.
from pypdf import PdfReader, PdfWriter
import os

def split_pdfs(input_path, output_folder):
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])

        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_filename = f"{base_name}_page_{i+1}.pdf"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, "wb") as out_file:
            writer.write(out_file)

    return total_pages



