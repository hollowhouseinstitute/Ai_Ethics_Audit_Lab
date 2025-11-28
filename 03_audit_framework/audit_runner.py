import json
from fairness_checks import run_fairness_audit
from privacy_checks import run_privacy_audit
from explainability_tests import test_feature_transparency
from compliance_engine import run_compliance_audit


def run_full_audit(input_file):
    return {
        "fairness": run_fairness_audit(input_file),
        "privacy": run_privacy_audit(input_file),
        "compliance": run_compliance_audit(input_file),
        "explainability": test_feature_transparency(
            {
                "input_features": ["text", "age", "gender"],
                "target": "prediction",
                "preprocessing": "standard",
            }
        ),
    }


if __name__ == "__main__":
    result = run_full_audit("02_processing/normalized_sample.json")
    print(json.dumps(result, indent=2))
