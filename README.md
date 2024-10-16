# PDF TEXT ANALYZER

This project allows you to upload multiple PDF files, extract text from them, and identify the most common or repeated lines across the PDFs. It helps in finding similarities between PDF documents, especially useful when comparing reports, documents, or any large text data stored in PDFs.

## Features

- Upload multiple PDFs using a graphical file dialog.
- Extract and process text from all the selected PDFs.
- Identify and display the most common lines across all PDFs.
- Works on PDFs with multi-page documents.

## Requirements

Before running the project, ensure you have the following Python libraries installed:

- `PyPDF2` – To extract text from PDFs.
- `tkinter` – For file selection dialog.
- `collections.Counter` – To count the occurrences of lines.

You can install the necessary libraries with the following command:

```bash
pip install PyPDF2

pdf-common-lines-finder/
│
├── README.md                   # Project documentation
├── requirements.txt             # Dependencies file (optional)
├── app.py   # Main script to run the project
