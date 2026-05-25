import pdfplumber
from pathlib import Path

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract raw text from a PDF file using pdfplumber.
    Returns all text as a single string.
    Churned => cancelled
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a .pdf file, got: {path.suffix}")

    full_text = ""

    with pdfplumber.open(file_path) as pdf:
        print(f"PDF has {len(pdf.pages)} page(s)")

        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text += f"\n--- Page {i+1} ---\n{text}"

            tables = page.extract_tables()
            if tables:
                print(f"Found {len(tables)} table(s) on page {i+1}")
                for table in tables:
                    for row in table:
                        row_text = " | ".join([str(cell) if cell else "" for cell in row])
                        full_text += f"\n{row_text}"

    if not full_text.strip():
        raise ValueError("Could not extract any text from PDF — might be a scanned image")

    print(f"Extracted {len(full_text)} characters from PDF")
    return full_text