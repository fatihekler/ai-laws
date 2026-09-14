# AI-LAWS — Existing Downloaded PDFs / NotebookLM Upload Plan

**STATE:** CONTROLLED_UPLOAD_PLAN  
**SOURCE DIRECTORY:** `86_NOTEBOOKLM/downloads/`  
**AUTO_ADVANCE:** NO

## Decision

Do not upload every PDF in this directory to one Notebook.

Use pack-by-pack ingestion after content-identity verification.

## NB01 — Global AI Governance

R027 inspected all eight core `INT-001..INT-008` repository PDFs entirely inside GitHub. No artifact/ZIP was created.

```text
NB01_CORE_REPOSITORY_PDFS_INSPECTED = 8 / 8
NATIVE_SEARCHABLE_TEXT_LAYER = 8 / 8
CONTENT_IDENTITY_VERIFIED = 6
CONTENT_IDENTITY_PARTIAL = 1  # INT-007 outcome bundle, not exact A/RES/79/1 file
SUPERSEDED_SOURCE = 1         # INT-004 legacy 43GC volume
DERIVED_MARKDOWN_REQUIRED = 0
NOTEBOOK_UPLOADS = 0
INT007_EXACT_OFFICIAL_A_RES_79_1_SOURCE = VERIFIED_R032
INT004_CERTIFIED_COPY_R032_ACCESS = BLOCKED_403_PRIOR_PIN_PRESERVED
```

Key corrections: `INT-001` repository PDF is the 12-page **CETS 225 treaty text**, not a treaty-status-page snapshot; live Treaty Office status remains mandatory for signatures/ratifications/reservations/declarations. `INT-005` is an OECD Council Recommendation PDF, not a webpage print. `INT-007` is a 64-page Summit of the Future outcome-document bundle containing the Pact and Global Digital Compact, but the extracted PDF does not carry the exact `A/RES/79/1` identifier; use the official adopted source for primary resolution identity. `INT-004` is verified as the legacy 43GC resolutions volume and remains superseded for current primary use by the certified-copy UNESCO URL.

### Prefer official URL over repository PDF

- `INT-001` CETS 225 — repository PDF verified as treaty text; use the live Treaty Office URL for current party/status data.
- `INT-002` CETS 225 Explanatory Report — URL preferred; PDF fallback after content check.
- `INT-005` OECD AI Principles — live official page preferred.
- `INT-006` A/RES/78/265 — UN URL preferred.
- `INT-007` Pact for the Future / Global Digital Compact — repository PDF remains a verified supporting outcome-document bundle, but R032 resolved the exact adopted source at `https://docs.un.org/en/A/RES/79/1` and official 56-page PDF `https://documents.un.org/doc/undoc/gen/n24/272/22/pdf/n2427222.pdf` (SHA-256 `0c3968d0ce8d55cf107309794adea6879d70f9aea60e6d6d64e3a8da4b028336`). Use the official source for primary resolution identity.
- `INT-008` Governing AI for Humanity — UN official URL preferred; repository binary not preferred due reproduction/right-state concerns.
- `US-007` NIST AI RMF and `US-008` NIST GenAI Profile may be used as supporting framework sources where assigned, but are not binding law.

### PDF eligible after content check

- `INT-003` UNESCO AI Ethics Recommendation.

### Do not upload as current primary source

- repository `INT-004` legacy 43rd General Conference resolutions PDF. Replace the primary Notebook source with the current certified-copy UNESCO source recorded in the manifest. R032 GitHub-runner access to the certified-copy URL returned HTTP 403; preserve the prior pin and do not infer source invalidity from the runner access block.

## NB02 — European Union AI Law

R030 validated all ten `EU-001..EU-010` repository PDFs inside GitHub against official EUR-Lex PDF endpoints. No ZIP/artifact, derived Markdown or Notebook upload was created.

```text
NB02_REPOSITORY_PDFS_INSPECTED = 10 / 10
NB02_NATIVE_SEARCHABLE_TEXT_LAYER = 10 / 10
NB02_CONTENT_IDENTITY_VERIFIED = 10 / 10
NB02_OFFICIAL_EUR_LEX_EXACT_BYTE_MATCH = 10 / 10
NB02_DERIVED_MARKDOWN_REQUIRED = 0
NB02_NOTEBOOK_UPLOADS = 0
```

`EU-001` exactly matches the current consolidated EUR-Lex PDF `CELEX:02024R1689-20260727` dated `2026-07-27`. `EU-002..EU-010` exactly match their corresponding official EUR-Lex CELEX PDFs.

The repository PDFs are therefore eligible as **verified official snapshots**, but official EUR-Lex URLs remain required for temporal currentness and legal-effect checks.

Special labels remain mandatory:

- `EU-001` is a consolidated temporal snapshot; a newer consolidation supersedes it for current-law use.
- `EU-003` and `EU-009` are directives; national transposition must be checked for Member-State-specific duties.
- `EU-010` has phased application: Chapter IV from `2026-06-11`, Article 14 from `2026-09-11`, general application from `2027-12-11`.
- `EU-007` generally applies from `2025-09-12`, with provision-specific dates.

```text
EXACT_OFFICIAL_PDF_BYTES != PERMANENT_CURRENT_LAW
DIRECTIVE_TEXT_VERIFIED != NATIONAL_IMPLEMENTATION_VERIFIED
CONSOLIDATED_SNAPSHOT_VERIFIED != FUTURE_CURRENTNESS_GUARANTEED
```

## NB03 — United States

R028 inspected all eight core `US-001..US-008` repository PDFs. R031 then closed the residual binary/source-routing question for `US-001` and `US-005` without starting substantive R007 research. No ZIP/artifact, derived Markdown or Notebook upload was created.

```text
NB03_CORE_REPOSITORY_PDFS_INSPECTED = 8 / 8
NB03_NATIVE_SEARCHABLE_TEXT_LAYER = 8 / 8
NB03_CONTENT_IDENTITY_VERIFIED = 7 / 8
NB03_CONTENT_IDENTITY_PARTIAL = 1 / 8   # US-001 webpage-print representation
NB03_OFFICIAL_EXACT_BYTE_MATCH = 7 / 8  # US-002/003/004/005/006/007/008
NB03_DERIVED_MARKDOWN_REQUIRED = 0
NB03_NOTEBOOK_UPLOADS = 0
```

R031 residual resolution:

- `US-001` remains a verified White House **webpage-print snapshot** and `CONTENT_IDENTITY_PARTIAL / SUPPORTING_ONLY`. This is intentional: the official source is HTML, so byte equality with a printed PDF is not a meaningful authenticity test. Use the live White House URL as the primary source.
- `US-005` is Federal Register document `2025-23092`, published `2025-12-16`. The repository PDF is an exact byte match to the official GovInfo PDF, SHA-256 `5a557f9a153f1f40c7bd885b660ed81f1b26d55a6363b778943dfaa65565e0cb`, 204,973 bytes. It is eligible as a verified official PDF snapshot.

Existing exact matches also remain: `US-002`, `US-003`, `US-004`, `US-006`, `US-007`, `US-008`.

Do not label executive orders or OMB memoranda as Acts of Congress. NIST sources are voluntary/nonbinding frameworks/profiles. A live White House page or exact Federal Register PDF snapshot does not, by itself, prove continuing legal effect, non-revocation, preemption, or the validity of any federal-state legal theory.

```text
EXACT_OFFICIAL_PDF_BYTES != PERMANENT_CURRENTNESS
WEBPAGE_PRINT_SNAPSHOT != LIVE_OFFICIAL_PAGE
EXECUTIVE_ORDER != ACT_OF_CONGRESS
SOURCE_IDENTITY_VERIFIED != LEGAL_EFFECT_CONCLUSION
```

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

R026 locally inspected all eight repository PDFs with `pdfinfo`, `pdftotext`, SHA-256 capture, and rendered first/last-page checks. Current repository-snapshot state is:

```text
REPOSITORY_BINARY_PRESENT = 8 / 8
CONTENT_IDENTITY_VERIFIED = 8 / 8
NATIVE_SEARCHABLE_TEXT_LAYER = 8 / 8
FIRST_LAST_PAGE_RENDER_CHECK = 8 / 8
OFFICIAL_MEVZUAT_LIVE_EXACT_BYTE_MATCH = NOT_RUN / PORTAL_BLOCKED
```

The PDFs may be used in NB04 as **verified repository snapshots** only when each source keeps its date/currentness label and `PRIMARY_SOURCE_RECHECK_REQUIRED` status. They are not asserted to be exact official Mevzuat bytes.

Special states:

- `TR-008` contains Law No. 7590 amendments, including Article 6/16 signals, `GEÇİCİ MADDE 2`, the attached list, and the effective-date table `31/7/2026`; the former 7590-incorporation blocker is resolved for this repository snapshot.
- `TR-007` contains Law No. 7590 changes effective `31/7/2026` and also records Law No. 7578 provisions with a future effective date of `1/11/2026`; Notebook use must preserve the applicable-date distinction.
- `TR-003`, `TR-005`, and `TR-006` contain 2026 amendment/effective-date signals in their closing tables.

Before any material legal conclusion, recheck the live official Mevzuat text when the portal becomes accessible.

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

R029 inspected all four repository PDFs and rechecked the directly corresponding original/source layer.

```text
NB08_REPOSITORY_PDFS_INSPECTED = 4 / 4
NB08_NATIVE_SEARCHABLE_TEXT_LAYER = 4 / 4
NB08_CONTENT_IDENTITY_VERIFIED = 2
NB08_CONTENT_IDENTITY_PARTIAL = 2
NB08_OFFICIAL_OR_ORIGINAL_EXACT_BYTE_MATCH = 2
NB08_DERIVED_MARKDOWN_REQUIRED = 0
NB08_NOTEBOOK_UPLOADS = 0
```

Controlled roles and routing:

- `INC-001` — `COMPANY_INCIDENT_DISCLOSURE`: repository OpenAI technical report is content-partial because both relevant OpenAI official URLs returned 403 to the GitHub runner; hold normal PDF ingestion pending official-source recheck.
- `INC-002` — `INDEPENDENT_INVESTIGATION`: exact byte match to the METR direct PDF; eligible as a verified official/original PDF while preserving stated investigation limitations.
- `INC-003` — `VENDOR_THREAT_INTELLIGENCE`: exact byte match to the official Anthropic CDN report; eligible with explicit vendor-attribution labeling.
- `INC-004` — `POLICY_FORECAST_CONTEXT`: live author page verified, repository file is a webpage-print snapshot; use live URL if needed and never treat it as incident fact.

```text
COMPANY_DISCLOSURE != INDEPENDENT_PROOF
VENDOR_ATTRIBUTION != COURT_FINDING
FORECAST != INCIDENT
INCIDENT != LIABILITY
```

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
