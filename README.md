# Test Marketplace Skills

Demonstration skills repository for Agentic Platform Gateways synchronization pipeline.

## Governance Architecture (PR 709)

This repository demonstrates the Enterprise Governance Schema v2.4 two-tier cascade:
- **Root Governance** (`/governance.yaml`): Declares organization-level defaults (`scope: global`, `domain: it4it`, `skill_type: Project`, `owner_group: DATA-GCP-BTAP_DEV@loreal.com`, `confidentiality: C2`, `personal_data: Aucun`).
- **Directory Governance** (`skills/*/governance.yaml`): Provides skill-level overrides without altering `SKILL.md`.
- **Clean Packages**: `SKILL.md` files are maintained strictly as instruction manifests; governance is never parsed from frontmatter, and `governance.yaml` files are excluded from the synced zip archive.

### Test Scenarios Matrix

| Skill | `skill_type` | Domain | Confidentiality | Personal Data | Owner Group | Backend Behavior | Scenario Verified |
|---|---|---|---|---|---|---|---|
| `echo-greeting` | `Personal` | `it4it` (root) | `C1` (override) | `Aucun` (root) | None (private) | `audience: private`, auto-approved post-scan | Personal skill auto-approved after SAFE security scan |
| `data-cleaner` | `Project` (root) | `it4it` (root) | `C2` (root) | `P1` (override) | Root group | `audience: shared`, normal approval queue | Shared project skill handling P1 personal data |
| `audit-logger` | `Business` (override) | `legal` (override) | `C3` (override) | `Aucun` (root) | Custom legal group | `audience: shared`, legal domain & C3 compliance | Enterprise business skill with legal compliance domain |
