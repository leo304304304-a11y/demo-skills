---
name: audit-logger
display_name: Audit & Compliance Logger
description: Generates structured compliance and security audit trail reports for automated agent actions
version: 1.0.0
---

# Audit & Compliance Logger

Ensures all agentic operations conform to enterprise audit standards and SOC2/ISO requirements.

## Guidelines
- Check all operations against `references/compliance-checklist.md`.
- Validate audit payloads using `scripts/validate_audit.py`.
- Ensure PII masking is applied before emitting logs.
