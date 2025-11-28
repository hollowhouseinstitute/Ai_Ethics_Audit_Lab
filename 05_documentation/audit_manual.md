# AI Ethics Audit Manual

This manual describes how to run, evaluate, and interpret AI Ethics Audits inside the Ai_Ethics_Audit_Lab.

---

## 1. Overview

This audit pipeline evaluates four major categories:

1. Fairness
2. Privacy & PII
3. Explainability
4. Regulatory & safety compliance

Outputs are generated into:

- 04_results/reports/
- 04_results/metrics/
- 04_results/flagged_items/
- 04_results/lineage_maps/

---

## 2. How to Run an Audit

You may run a full audit with:

    python 03_audit_framework/audit_runner.py

---

## 3. Interpretation of Scores

### Fairness
- OVER_REPRESENTATION → distribution-red flag
- UNDER_REPRESENTATION → distribution imbalance

### Privacy


cat > 05_documentation/data_handling_guidelines.md << 'EOF'
# Data Handling Guidelines

This document describes the standards for safe and ethical handling of datasets within the Ai_Ethics_Audit_Lab.

---

## 1. Raw Data Rules
- Raw data must never be edited.
- Sensitive data must be encrypted before upload.
- Remove direct identifiers unless explicitly needed.

---

## 2. Preprocessing Rules
- Use scripts inside /02_processing/
- All transformations must be logged.
- Normalization must preserve demographic granularity.

---

## 3. Storage Rules
- Raw → 01_raw/
- Processed → 02_processing/
- Results → 04_results/

---

## 4. Sensitive Attributes
Considered highly protected:
- Race / Ethnicity
- Sexual orientation
- Health status
- Disability markers

Strict review is required.

