from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.request import urlopen


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


def ping(url: str, timeout: float = 5.0) -> dict:
    with urlopen(url, timeout=timeout) as response:
        return {"status": response.status, "url": url, "ctype": response.headers.get("Content-Type")}
