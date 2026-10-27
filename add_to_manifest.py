
import csv
import hashlib
from pathlib import Path
from datetime import date

pdf_path = Path("data/raw/Handbook_for_Presiding_Officer_2023.pdf")
manifest = Path("data/manifest.csv")

if not pdf_path.exists():
    raise FileNotFoundError(pdf_path)

file_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

with manifest.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

if any(row["sha256"] == file_hash for row in rows):
    print("This PDF is already recorded in the manifest.")
else:
    rows.append({
        "file": pdf_path.as_posix(),
        "source_url": "https://www.eci.gov.in/handbooks-manuals-modelchecklist",
        "downloaded_on": date.today().isoformat(),
        "bytes": str(pdf_path.stat().st_size),
        "sha256": file_hash,
    })

    with manifest.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "file", "source_url", "downloaded_on",
                "bytes", "sha256"
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print("Handbook added to manifest successfully.")
