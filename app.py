import PyPDF2
from collections import Counter
from tkinter import Tk, filedialog

def extract_lines_from_pdf(pdf_path):
    lines = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text()
            if text:
                lines.extend(text.splitlines())
    return lines

def get_most_common_lines(lines, num_common=10):
    line_counter = Counter(lines)
    return [line for line, count in line_counter.items() if count > 1][:num_common]

def analyze_pdfs():
    root = Tk()
    root.withdraw() 
    pdf_paths = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])

    if not pdf_paths:
        print("No PDF files selected.")
        return

    all_lines = []
    for pdf_path in pdf_paths:
        all_lines.extend(extract_lines_from_pdf(pdf_path))

    common_lines = get_most_common_lines(all_lines, num_common=10)
    
    if common_lines:
        print("Most common lines in the selected PDFs:")
        for line in common_lines:
            print(f"'{line}'")
    else:
        print("No common lines found.")

if __name__ == "__main__":
    analyze_pdfs()
