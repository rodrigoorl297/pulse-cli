from __future__ import annotations

import hashlib
import json
from pathlib import Path


def hash_file(path: Path, algo: str = "sha256") -> str:
    digest = hashlib.new(algo)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def summarize_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return {"type": "array", "count": len(data)}
    if isinstance(data, dict):
        return {"type": "object", "keys": sorted(data.keys())}
    return {"type": type(data).__name__}
