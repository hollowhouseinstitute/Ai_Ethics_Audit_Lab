import json
from collections import Counter

def demographic_distribution(records, attribute="gender"):
    values = [r.get("demographics", {}).get(attribute) for r in records if r.get("demographics")]
    return Counter(values)

def check_imbalance(records, threshold=0.7):
    dist = demographic_distribution(records)
    total = sum(dist.values())
    issues = []

    for group, count in dist.items():
        ratio = count / total
        if ratio > threshold:
            issues.append({
                "group": group,
                "ratio": ratio,
                "issue": "OVER_REPRESENTATION"
            })

    return issues

def run_fairness_audit(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    imbalance = check_imbalance(data)
    return {"fairness_issues": imbalance}

if __name__ == "__main__":
    result = run_fairness_audit("02_processing/normalized_sample.json")


cat > 03_audit_framework/privacy_checks.py << 'EOF'
import json
import re

PII_PATTERNS = {
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    "credit_card": r"\b(?:\d[ -]*?){13,16}\b"
}

def detect_pii(text):
    found = {}
    for label, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            found[label] = matches
    return found

def run_privacy_audit(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    text = data.get("text", "")
    pii_hits = detect_pii(text)

    return {"pii_detected": pii_hits}

if __name__ == "__main__":
    print(run_privacy_audit("02_processing/normalized_sample.json"))
