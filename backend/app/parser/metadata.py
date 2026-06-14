import json
from pathlib import Path

METADATA_DIR = Path("metadata")
METADATA_DIR.mkdir(exist_ok=True)

def save_metadata(document_id, data):

    path = METADATA_DIR / f"{document_id}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )