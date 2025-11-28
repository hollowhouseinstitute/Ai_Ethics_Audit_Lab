import json
from collections import Counter


def demographic_distribution(records, attribute="gender"):
    """
    Returns a Counter of demographic values from the dataset.
    """
    values = [
        r.get("demographics", {}).get(attribute)
        for r in records
        if r.get("demographics", {}).get(attribute) is not None
    ]
    return Counter(values)


def check_imbalance(records, threshold=0.7):
    """
    Detects demographic imbalance.
    Example:
        If one demographic group makes up more than 70% of total.
    """
    dist = demographic_distribution(records)
    total = sum(dist.values())
    issues = []

    for group, count in dist.items():
        ratio = count / total if total > 0 else 0

        if ratio > threshold:
            issues.append(
                {
                    "group": group,
                    "ratio": ratio,
                    "issue": "OVER_REPRESENTATION",
                }
            )

    return issues


def run_fairness_checks(input_path, output_path):
    """
    Runs fairness checks end-to-end:
    - Loads dataset
    - Runs imbalance detection
    - Saves results
    """
    with open(input_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    results = {
        "fairness_issues": check_imbalance(records),
        "total_records": len(records),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    return results


if __name__ == "__main__":
    # Example local run (used for testing)
    run_fairness_checks(
        input_path="data/raw/sample_dataset.json",
        output_path="04_results/metrics/fairness_report.json",
    )
