from extractors.pdf_extractor import extract_text_from_pdf
from extractors.ai_extractor import extract_with_ai
import json

#step1 : pdf_extractor.py
print("*** Step 1: Extract text from PDF ***")
text = extract_text_from_pdf("sample_files/invoice.pdf")
print(text[:500])

#step2: ai_extractor.py
print("\n*** Step 2: AI extraction ***")
customers = extract_with_ai(text)
print(json.dumps(customers, indent=2))