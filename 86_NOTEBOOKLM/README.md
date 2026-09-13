# AI-LAWS — NotebookLM / Gemini Notebook Workspace

**STATE:** RESEARCH_SUPPORT_INFRASTRUCTURE  
**DATE:** 2026-09-13  
**CANONICAL_LEGAL_AUTHORITY:** NO

This directory defines how AI-LAWS may use NotebookLM / Gemini Notebook as a source-grounded synthesis workspace.

## Core rule

```text
NOTEBOOK_OUTPUT != LEGAL_AUTHORITY
NOTEBOOK_CITATION != SOURCE_VERIFICATION
MODEL_GENERATED_SOURCE != PRIMARY_SOURCE
```

Notebook is used to compare, synthesize and question a curated source pack. AI-LAWS GitHub remains the durable project record; official/current legal sources remain the legal evidence base.

## Current Google product constraints

Google's current help documentation states that Gemini Notebook supports sources including PDF, DOCX, TXT, Markdown, CSV, PPTX, Google Docs/Slides/Sheets, web URLs, ePub, public YouTube, audio and images. Standard/free access currently allows up to 50 sources per notebook. Each source may contain up to 500,000 words; local uploads may be up to 200 MB. Product limits may change and must be rechecked before a major corpus build.

Do not upload documents you do not have rights to use.

## Recommended workspace model

Do not create one undifferentiated global notebook.

Use separate packs:

- `NB00_AI_LAWS_CONTROL_AND_METHOD`
- `NB01_GLOBAL_AI_GOVERNANCE`
- `NB02_EU_AI_LAW`
- `NB03_US_AI_LAW`
- `NB04_TR_AI_LAW`
- `NB05_ASIA_AND_COMPARATIVE`
- `NB06_HUMAN_SOVEREIGNTY_NEUROTECH`
- `NB07_LIABILITY_EVIDENCE_FINANCE`
- `NB08_FRONTIER_AI_INCIDENTS`
- `NB09_CROSS_REPO_REQUIREMENTS`

Each notebook should normally remain below the product source limit with headroom for future amendments and case law.

## Files in this directory

- `NOTEBOOKLM_CORPUS_ARCHITECTURE.md`
- `NOTEBOOKLM_SOURCE_ACQUISITION_POLICY.md`
- `NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv`
- `NOTEBOOKLM_SOURCE_PACK_ASSIGNMENTS.csv`
- `NOTEBOOKLM_UPLOAD_AND_REFRESH_CHECKLIST.md`
- `NOTEBOOKLM_RESEARCH_QUESTION_CATALOG.md`
- `NOTEBOOKLM_READY_TO_PASTE_MASTER_INSTRUCTION.txt`

## Privacy and confidentiality boundary

Do not upload by default:

- privileged attorney-client material;
- litigation work product;
- personal data not necessary for research;
- API keys or credentials;
- private repository secrets;
- unreleased incident logs;
- classified/restricted material;
- contract-confidential documents;
- copyrighted/paywalled standards without a valid right to use them.

A public AI-LAWS source pack and a confidential legal-work notebook must never be silently merged.

## Freshness

Notebook sources are snapshots for research. Before relying on a legal proposition, re-check the current official source and effective/application date.

```text
NOTEBOOK_SNAPSHOT != CURRENT_LAW
```

## Output state

All Notebook-derived outputs enter AI-LAWS as:

```text
SOURCE_CLASS = NOTEBOOK_SYNTHESIS
CANONICAL = FALSE
LEGAL_ADVICE = NO
```
