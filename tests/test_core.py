import json
from pathlib import Path

from pulse_cli.core import hash_file, summarize_json
from pulse_cli.cli import main


def test_hash_and_json(tmp_path: Path):
    payload = tmp_path / "data.json"
    payload.write_text(json.dumps({"ok": True, "n": 1}), encoding="utf-8")
    digest = hash_file(payload)
    assert len(digest) == 64
    summary = summarize_json(payload)
    assert summary["type"] == "object"
    assert main(["json", str(payload)]) == 0
