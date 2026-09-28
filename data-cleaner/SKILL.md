---
name: data-cleaner
display_name: Data Cleaning & Normalizer
description: Sanitizes CSV, JSON, and TSV datasets by removing null bytes, normalizing headers, and detecting anomalies
version: 1.0.0
---

# Data Cleaning & Normalizer

Provides utilities and rules for preparing tabular datasets before analysis or embedding generation.

## Capabilities
- Normalizes column names to snake_case.
- Strips null characters and invalid Unicode sequences.
- Validates data against `references/schema-rules.json`.
- Runs sanitation via `scripts/clean_csv.py`.
