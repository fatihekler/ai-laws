# AI-LAWS — Existing Downloaded PDFs / NotebookLM Upload Plan

**STATE:** CONTROLLED_UPLOAD_PLAN  
**SOURCE DIRECTORY:** `86_NOTEBOOKLM/downloads/`  
**AUTO_ADVANCE:** NO

## Decision

Do not upload every PDF in this directory to one Notebook.

Use pack-by-pack ingestion after content-identity verification.

## NB01 — Global AI Governance

### Prefer official URL over repository PDF

- `INT-001` CETS 225 treaty status page — dynamic status; PDF only historical snapshot.
- `INT-002` CETS 225 Explanatory Report — URL preferred; PDF fallback after content check.
- `INT-005` OECD AI Principles — live official page preferred.
- `INT-006` A/RES/78/265 — UN URL preferred.
- `INT-007` Pact for the Future / Global Digital Compact — UN official URL preferred.
- `INT-008` Governing AI for Humanity — UN official URL preferred; repository binary not preferred due reproduction/right-state concerns.
- `US-007` NIST AI RMF and `US-008` NIST GenAI Profile may be used as supporting framework sources where assigned, but are not binding law.

### PDF eligible after content check

- `INT-003` UNESCO AI Ethics Recommendation.

### Do not upload as current primary source

- repository `INT-004` legacy 43rd General Conference resolutions PDF. Replace the primary Notebook source with the current certified-copy UNESCO source recorded in the manifest.

## NB02 — European Union AI Law

Use official EUR-Lex URLs as the preferred current-law sources:

- `EU-001` AI Act current consolidated text;
- `EU-002` Regulation (EU) 2026/1744;
- `EU-003` Product Liability Directive;
- `EU-004` Charter;
- `EU-005` GDPR;
- `EU-006` DSA;
- `EU-007` Data Act;
- `EU-008` DGA;
- `EU-009` NIS2;
- `EU-010` Cyber Resilience Act.

R024 and R025 together rechecked the official source/currentness layer for `EU-001` through `EU-010` on 2026-09-14. The controlled NB02 official-URL source set is therefore ready for Notebook ingestion. The repository PDF bodies are still not directly inspectable through the current GitHub connector, so the corresponding repository snapshots remain `CONTENT_IDENTITY_PARTIAL` and are not the preferred Notebook baseline.

Special currentness/application labels must remain visible:

- `EU-003` and `EU-009` are directives; national transposition must be checked for Member-State-specific duties.
- `EU-010` has phased application: Chapter IV from 2026-06-11, Article 14 from 2026-09-11, and general application from 2027-12-11.
- `EU-007` generally applies from 2025-09-12, with additional provision-specific dates.

Repository PDFs may be uploaded only as versioned snapshots after content identity is checked.

Important:

```text
CONSOLIDATED_PDF_SNAPSHOT != PERMANENT_CURRENT_LAW
DIRECTIVE != IDENTICAL_NATIONAL_IMPLEMENTATION
OFFICIAL_URL_SOURCE_VERIFIED != REPOSITORY_PDF_BODY_VERIFIED
```

## NB03 — United States

### PDF candidates after content check

- `US-002` America's AI Action Plan;
- `US-003` OMB M-25-21;
- `US-004` OMB M-25-22;
- `US-006` OMB M-26-04.

### URL/current-status preferred

- `US-001` EO 14179;
- `US-005` EO 14365;
- `US-007` NIST AI RMF;
- `US-008` NIST GenAI Profile.

Do not label executive orders or OMB memoranda as Acts of Congress.

## NB04 — Türkiye

Current repository PDFs:

- `TR-001` Constitution;
- `TR-002` Law 6698;
- `TR-003` Law 6098;
- `TR-004` Law 4721;
- `TR-005` Law 5237;
- `TR-006` Law 6502;
- `TR-007` Law 5651;
- `TR-008` Law 7545.

All are currently:

```text
REPOSITORY_BINARY_PRESENT
CONTENT_IDENTITY_UNVERIFIED
CURRENT_CONSOLIDATED_TEXT_RECHECK_REQUIRED
```

Therefore do **not** upload these eight PDFs as the legal baseline yet.

Process each PDF using `PDF_CONTENT_IDENTITY_AND_DERIVED_TEXT_PROTOCOL.md` and the official source-pin records.

For `TR-008`, verify that Law No. 7590 amendments effective 2026-07-31 are incorporated before Notebook use.

## NB06 — Human Sovereignty / Neurotechnology

Use:

- `INT-003` UNESCO AI Ethics;
- current certified-copy `INT-004` UNESCO Neurotechnology source via official URL, not the legacy downloaded 43GC PDF as primary;
- `EU-004` Charter via official URL;
- `EU-005` GDPR via official URL;
- Chile sources only after the relevant official-source/full-text gates.

## NB07 — Liability / Evidence / Financial Responsibility

Reuse already validated source identities rather than making duplicate content copies:

- `EU-003` Product Liability Directive;
- `EU-001` AI Act relevant logging/incident provisions;
- `EU-005` GDPR where relevant;
- `US-003` and `US-004` public-sector governance/procurement examples;
- NIST sources as nonbinding comparison.

The pack must preserve:

```text
CURRENT LAW
COMMERCIAL PRACTICE
REGULATORY GUIDANCE
ACADEMIC PROPOSAL
POLICY PROPOSAL
```

as separate classes.

## NB08 — Frontier AI Incidents

Recommended core pair:

1. `INC-001` — OpenAI company incident disclosure;
2. `INC-002` — Redwood/METR independent investigation.

Additional:

- `INC-003` — Anthropic vendor threat-intelligence report;
- `INC-004` — optional policy/forecast context only.

Mandatory labels:

```text
INC-001 = COMPANY_INCIDENT_DISCLOSURE
INC-002 = INDEPENDENT_INVESTIGATION
INC-003 = VENDOR_THREAT_INTELLIGENCE
INC-004 = POLICY_FORECAST_CONTEXT
```

Do not ask Notebook to synthesize these as if they were equal authority.

## Upload workflow

For each pack:

1. select sources using `DOWNLOADS_REGISTRY.csv`;
2. run content-identity checks;
3. rename only the **local Notebook-upload copy** using `recommended_canonical_filename` if useful;
4. upload/add URL;
5. record Notebook source title using `recommended_notebook_label`;
6. run source-identity/locator test;
7. run authority-separation test;
8. only then ask substantive questions;
9. primary-source recheck all material findings;
10. record results in the acquisition/validation ledger.

## Direct answer to the conversion question

Do **not** convert the whole directory to Markdown before Notebook upload.

Use direct PDFs/official URLs first. Create Markdown derivatives only for PDFs that fail text extraction, need controlled diffing, or need page-preserving retrieval support.

A derived Markdown document must remain `NONCANONICAL_DERIVATIVE` and may not replace the primary PDF/official URL in provenance.

`AUTO_ADVANCE = NO`
