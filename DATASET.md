
# VoteReady Dataset

## Purpose
This dataset contains official voter-service forms collected for the VoteReady civic information assistant.

## Dataset Files

| File | Source URL | Pages | Licence / Terms | Downloaded On |
|---|---|---:|---|---|
| Form_6_English.pdf | https://voters.eci.gov.in/formspdf/Form_6_English.pdf | 2 | Official ECI source; verify applicable reuse terms | 2026-10-23 |
| Form_8_English.pdf | https://voters.eci.gov.in/formspdf/Form_8_English.pdf | 2 | Official ECI source; verify applicable reuse terms | 2026-10-23 |

## Storage
- Original documents: `data/raw/`
- Download manifest: `data/manifest.csv`
- Sample documents: `data/sample/`

Original PDFs are excluded from Git commits to avoid committing the full dataset.

## Data Collection
Documents were downloaded from official Election Commission of India URLs using `tools/download.py`. The manifest records the source URL, download date, file size, and SHA-256 hash.

## Current Coverage
- Documents collected: 2
- Total pages verified: 4
- Target: 50+ relevant pages

## Limitations
The dataset is incomplete and requires additional official voter-service guidance. Page counts and source reuse terms must be verified for every new document.


## Sample Files

| File | Pages | Purpose |
|---|---:|---|
| Form-6_data.pdf | 1 | Existing Form 6 sample |
| Form-8_sample.pdf | 2 | Form 8 sample copied from the raw dataset |

The sample folder currently contains 2 PDF files.
