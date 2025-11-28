import json
import re


def clean_text(text):
    """Basic text cleaning."""
    text = text.replace("\n", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def clean_record(record):
    """Clean individual data record."""
    if "text" in record:
        record["text"] = clean_text(record["text"])
    return record


def clean_file(input_path, output_path):
    print(f"Cleaning: {input_path}")
    with open(input_path, "r") as f:
        data = json.load(f)

    cleaned = clean_record(data)

    with open(output_path, "w") as f:
        json.dump(cleaned, f, indent=2)

    print(f"Saved cleaned file → {output_path}")


if __name__ == "__main__":
    clean_file("01_raw/sample_input.json", "02_processing/cleaned_sample.json")
