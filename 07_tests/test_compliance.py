import json
from pathlib import Path

from compliance_engine import run_compliance_audit

def test_compliance_missing_consent():
    sample = {
        "user_id": 22,
        "consent": False
    }

    Path("07_tests/compliance.json").write_text(json.dumps(sample))

    result = run_compliance_audit("07_tests/compliance.json")
    assert "NO_CONSENT" in result["compliance_issues"]
