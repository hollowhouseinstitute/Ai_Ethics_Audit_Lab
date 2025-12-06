import json
from pathlib import Path

from audit_runner import run_full_audit # pyright: ignore[reportMissingImports]


def test_full_audit_pipeline():
    sample = {
        "user_id": 10,
        "text": "This is a test.",
        "demographics": {"gender": "female", "age": 30},
        "consent": True,
    }

    Path("07_tests/full.json").write_text(json.dumps(sample))

    result = run_full_audit("07_tests/full.json")

    assert "fairness" in result
    assert "privacy" in result
    assert "compliance" in result
    assert "explainability" in result
