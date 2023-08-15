# PDF parsing and text extraction functionality
# PDF parsing is the process of extracting and interpreting the contents of a PDF

import PyPDF2


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = " "
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Enter your pdf_path
    text = extract_text_from_pdf(pdf_path)
    print(text)
