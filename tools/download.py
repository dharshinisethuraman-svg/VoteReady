
"""
Polite PDF/document downloader.

Usage:
    python tools/download.py urls.txt

Reads one URL per line; skips blank lines and comments.
Saves downloaded files to data/raw/ and records them in
data/manifest.csv.
"""

import csv
import hashlib
import os
import sys
import time
from datetime import date
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests

RAW = "data/raw"
MANIFEST = "data/manifest.csv"
DELAY = 2

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/130.0.0.0 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8",
}

robots = {}


def allowed(url):
    """Check robots.txt before downloading."""
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        print("SKIP: unsupported URL:", url)
        return False

    root = f"{parsed.scheme}://{parsed.netloc}"

    if root not in robots:
        rp = RobotFileParser()
        rp.set_url(root + "/robots.txt")

        try:
            rp.read()
            robots[root] = rp
        except Exception as exc:
            print("Could not check robots.txt:", exc)
            robots[root] = None

    rp = robots[root]

    # If robots.txt could not be read, skip rather than
    # assuming that downloading is permitted.
    if rp is None:
        print("SKIP: unable to verify robots.txt:", url)
        return False

    return rp.can_fetch(HEADERS["User-Agent"], url)


def name_for(url):
    """Create a safe filename from the URL."""
    name = os.path.basename(urlparse(url).path) or "download.bin"
    return os.path.basename(name).replace(" ", "_")


def main(list_file):
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)

    new_manifest = (
        not os.path.exists(MANIFEST)
        or os.path.getsize(MANIFEST) == 0
    )

    with open(list_file, encoding="utf-8") as fh:
        urls = [line.strip() for line in fh]

    with requests.Session() as session:
        session.headers.update(HEADERS)

        with open(MANIFEST, "a", newline="", encoding="utf-8") as mf:
            log = csv.writer(mf)

            if new_manifest:
                log.writerow([
                    "file",
                    "source_url",
                    "downloaded_on",
                    "bytes",
                    "sha256",
                ])

            for url in urls:
                if not url or url.startswith("#"):
                    continue

                if not allowed(url):
                    print("SKIP: download not permitted:", url)
                    continue

                filename = name_for(url)
                path = os.path.join(RAW, filename)

                if os.path.exists(path):
                    print("SKIP: already exists:", path)
                    continue

                try:
                    response = session.get(
                        url,
                        timeout=30,
                        allow_redirects=True,
                    )

                    print(
                        "HTTP status:",
                        response.status_code,
                        "| Content-Type:",
                        response.headers.get("Content-Type"),
                        "| URL:",
                        url,
                    )

                    if response.status_code == 406:
                        print(
                            "406 Not Acceptable: the server rejected "
                            "the request. Open the URL in your browser "
                            "or use an official alternative download."
                        )
                        continue

                    response.raise_for_status()

                    content_type = response.headers.get(
                        "Content-Type", ""
                    ).lower()

                    if "text/html" in content_type:
                        print("SKIP: server returned HTML, not a PDF:", url)
                        continue

                    content = response.content

                    if not content:
                        print("SKIP: empty response:", url)
                        continue

                    # Avoid saving an HTML error page as a PDF.
                    if urlparse(url).path.lower().endswith(".pdf"):
                        if not content.startswith(b"%PDF-"):
                            print("SKIP: response is not a valid PDF:", url)
                            continue

                    with open(path, "wb") as f:
                        f.write(content)

                    digest = hashlib.sha256(content).hexdigest()

                    log.writerow([
                        path,
                        url,
                        date.today().isoformat(),
                        len(content),
                        digest,
                    ])
                    mf.flush()

                    print("SAVED:", path, len(content), "bytes")

                except requests.RequestException as exc:
                    print("REQUEST ERROR:", url, "-", exc)

                finally:
                    time.sleep(DELAY)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tools/download.py urls.txt")
        sys.exit(1)

    main(sys.argv[1])
