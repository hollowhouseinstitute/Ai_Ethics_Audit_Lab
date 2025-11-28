import json
from pathlib import Path

from privacy_checks import run_privacy_audit

def test_privacy_detection():
    sample = {
        "text": "Contact me at jane@example.com"
    }
    Path("07_tests/privacy.json").write_text(json.dumps(sample))

    result = run_privacy_audit("07_tests/privacy.json")
    assert "email" in result.get("pii_detected", {})
