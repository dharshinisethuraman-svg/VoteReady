
import csv
import hashlib
from pathlib import Path
from pypdf import PdfReader

manifest = Path("data/manifest.csv")
seen = set()
total_pages = 0

with manifest.open("r", encoding="utf-8", newline="") as f:
    rows = csv.DictReader(f)

    for row in rows:
        pdf_path = Path(row["file"])

        if not pdf_path.exists():
            print("MISSING:", pdf_path)
            continue

        file_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

        if file_hash in seen:
            print("DUPLICATE:", pdf_path.name)
            continue

        seen.add(file_hash)
        pages = len(PdfReader(str(pdf_path)).pages)
        total_pages += pages

        print(f"{pdf_path.name}: {pages} pages")

print("-" * 30)
print("TOTAL UNIQUE PAGES:", total_pages)
