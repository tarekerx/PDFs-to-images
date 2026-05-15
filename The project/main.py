"""
PDF to PNG Converter
Reads all PDFs from the `input/` folder and saves each page as a PNG in `output/`.
Usage: python main.py
"""

import os
from pdf2image import convert_from_path

INPUT_DIR = "input"
OUTPUT_DIR = "output"
DPI = 200  # Increase for higher resolution (e.g. 300 for print quality)


def convert_pdfs_to_png():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in '{INPUT_DIR}/' folder.")
        return

    print(f"Found {len(pdf_files)} PDF(s). Converting...\n")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_DIR, pdf_file)
        base_name = os.path.splitext(pdf_file)[0]

        print(f"Processing: {pdf_file}")
        pages = convert_from_path(pdf_path, dpi=DPI)

        for i, page in enumerate(pages, start=1):
            if len(pages) == 1:
                out_filename = f"{base_name}.png"
            else:
                out_filename = f"{base_name}_page{i}.png"

            out_path = os.path.join(OUTPUT_DIR, out_filename)
            page.save(out_path, "PNG")
            print(f"  Saved: {out_path}")

    print(f"\nDone! All PNGs saved to '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    convert_pdfs_to_png()