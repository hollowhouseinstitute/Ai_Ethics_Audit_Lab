import json


def normalize_demographics(record):
    """Normalize demographic categories."""
    demo = record.get("demographics", {})

    if "gender" in demo:
        demo["gender"] = demo["gender"].lower()

    if "age" in demo:
        demo["age"] = int(demo["age"])

    record["demographics"] = demo
    return record


def normalize_file(input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)

    normalized = normalize_demographics(data)

    with open(output_path, "w") as f:
        json.dump(normalized, f, indent=2)


if __name__ == "__main__":
    normalize_file(
        "02_processing/cleaned_sample.json", "02_processing/normalized_sample.json"
    )
