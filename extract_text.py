
from pathlib import Path

from pypdf import PdfReader

# Input PDF
pdf_path = Path(
    "data/raw/Handbook_for_Presiding_Officer_2023.pdf"
)

# Output text file
output_path = Path(
    "data/processed/handbook_presiding_officer.txt"
)

if not pdf_path.exists():
    raise FileNotFoundError(f"PDF not found: {pdf_path}")

reader = PdfReader(str(pdf_path))

output_path.parent.mkdir(parents=True, exist_ok=True)

extracted_pages = []
empty_pages = 0

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""

    if not text.strip():
        empty_pages += 1

    extracted_pages.append(
        f"\n--- Page {page_number} ---\n{text}"
    )

full_text = "\n".join(extracted_pages)

output_path.write_text(full_text, encoding="utf-8")

print("PDF:", pdf_path.name)
print("Total pages:", len(reader.pages))
print("Pages with no extractable text:", empty_pages)
print("Check these pages for scanned or visual content:")
for page_number, page in enumerate(reader.pages, start=1):
    if not (page.extract_text() or "").strip():
        print(page_number, end=" ")
print()
print("Extracted characters:", len(full_text))
print("Saved to:", output_path)

print("\n--- TEXT PREVIEW (first 1500 characters) ---\n")
print(full_text[:1500])
