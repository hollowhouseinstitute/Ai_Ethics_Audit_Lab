# Results Directory

This folder contains the outputs generated from AI Ethics Audits.

## Subfolders
- **reports/** — Full written audit reports (Markdown, PDF)
- **metrics/** — Numerical fairness/privacy/compliance metrics
- **flagged_items/** — Items requiring human review
- **lineage_maps/** — Data lineage and provenance maps

These files are automatically populated when running:
    
    python 03_audit_framework/audit_runner.py
