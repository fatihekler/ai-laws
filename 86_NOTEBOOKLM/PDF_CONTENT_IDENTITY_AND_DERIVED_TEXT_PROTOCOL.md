# AI-LAWS — PDF Content Identity and Derived-Text Protocol

**STATE:** CONTROLLED_PROCESS  
**PURPOSE:** Decide when a downloaded PDF may be used directly in NotebookLM and when a noncanonical Markdown/text derivative is justified.

## 1. Default decision

Do **not** convert all PDFs to Markdown.

NotebookLM can ingest PDFs directly. Conversion is justified only when one of the following is true:

- PDF text extraction is materially broken;
- pages are scans/images with no usable text layer;
- tables/footnotes/columns cause material retrieval errors;
- a stable text derivative is needed for diffing/version comparison;
- source locator preservation requires a controlled page-marked derivative.

```text
PDF_PRESENT != PDF_CONTENT_VERIFIED
PDF_TO_MD != BETTER_SOURCE
DERIVED_MD != PRIMARY_SOURCE
```

## 2. Content-identity verification before Notebook upload

For every repository PDF candidate:

1. identify the `SOURCE_ID` using `downloads/DOWNLOADS_REGISTRY.csv`;
2. open the PDF;
3. verify title page/header;
4. verify issuing institution/authority;
5. verify document/law/regulation/memo number;
6. verify visible publication/version/consolidation date where applicable;
7. verify page count is plausible and file is not a partial print/export;
8. verify first substantive page and final page/annex/closing text;
9. test native text extraction/searchability;
10. compare identity/currentness to `NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv` and the official source;
11. classify the PDF as one of:

```text
CONTENT_IDENTITY_VERIFIED
CONTENT_IDENTITY_PARTIAL
CONTENT_MISMATCH
PARTIAL_DOCUMENT
WEBPAGE_PRINT_SNAPSHOT
SCANNED_NO_TEXT_LAYER
SUPERSEDED_SOURCE
UNKNOWN
```

Only `CONTENT_IDENTITY_VERIFIED` is eligible for normal PDF upload unless an explicit supporting/historical exception is recorded.

## 3. Text extraction hierarchy

Use the least-transformative method first:

```text
LEVEL_0 = direct PDF upload; no derivative
LEVEL_1 = native text extraction from embedded text layer
LEVEL_2 = layout-aware extraction for columns/tables
LEVEL_3 = OCR only for pages without usable text layer
LEVEL_4 = manual correction/reconciliation, human-reviewed
```

Do not OCR a clean born-digital legal PDF by default.

## 4. Derived Markdown location

Any generated text derivative must be stored outside `downloads/`:

```text
86_NOTEBOOKLM/derived_text/<SOURCE_ID>/
```

Recommended filename:

```text
SOURCE_ID__DERIVED-TEXT__<SOURCE_VERSION_OR_DATE>.md
```

## 5. Mandatory derived-text header

Every derived Markdown/text file must start with:

```yaml
source_id: EU-001
source_pdf_path: 86_NOTEBOOKLM/downloads/...
source_git_blob_sha: <git-blob-sha>
derived_text_state: NONCANONICAL_DERIVATIVE
canonical: false
extraction_method: NATIVE_TEXT | LAYOUT_AWARE | OCR | MANUAL_RECONCILIATION
extraction_tool: <tool/version>
extraction_date: YYYY-MM-DD
ocr_used: false
page_markers_preserved: true
content_corrections: NONE | DESCRIBE
primary_source_recheck_required: true
```

A derivative may never silently replace the PDF or official URL in provenance.

## 6. Page locator preservation

Where technically possible preserve page boundaries:

```text
<!-- PDF_PAGE: 001 -->
...
<!-- PDF_PAGE: 002 -->
```

For legal texts also preserve original article/section/annex headings exactly enough to allow return to the source.

Do not renumber provisions.

## 7. No silent correction

If extraction produces an obvious typo/OCR error:

- preserve the extracted form in the derivative or clearly mark a correction;
- record the source page;
- never silently rewrite statutory/court language;
- verify material quotations against the PDF/original official source.

## 8. Quality checks

Before using a derived text in Notebook:

- title/document ID match;
- no missing first/last pages;
- article/section count plausibility;
- random sample of at least 5 locations against PDF for long legal texts;
- all material tables/annexes accounted for or explicitly marked omitted;
- OCR pages identified;
- language/encoding preserved;
- page locator continuity checked.

## 9. Notebook source preference

Preference order:

```text
CURRENT OFFICIAL URL
>
VERIFIED OFFICIAL PDF
>
VERIFIED REPOSITORY PDF SNAPSHOT
>
NONCANONICAL DERIVED TEXT
>
MODEL SUMMARY
```

A derived Markdown copy is useful for retrieval/diffing but is lower authority than the verified PDF/original source.

## 10. Tool/plugin policy

Do not install a random PDF-to-Markdown plugin simply to normalize format.

If automated conversion is required, use a deterministic, version-recorded extraction tool that can:

- preserve Unicode;
- preserve page boundaries;
- avoid external upload of sensitive content;
- disclose OCR use;
- run reproducibly;
- produce inspectable output.

For ordinary born-digital PDFs, direct Notebook upload is preferred over conversion.

## 11. Special handling

### Dynamic/current-law pages

For treaty status, consolidated-law pages and living guidance, the local PDF is a snapshot. The official URL remains the currentness authority.

### Court decisions

Do not create a court-case corpus record from a derived text unless the case-law admission gate accepts the underlying full text.

### Incident reports

Keep vendor disclosure, independent investigation and forecast/policy essay as separate source classes even when they describe the same event.

### Türkiye manually downloaded law PDFs

Do not mark them current merely because title/law number matches. Confirm official consolidated/current text, especially amendments and effective dates.

## 12. Closeout fields

For each processed PDF record:

```text
SOURCE_ID
REPO_FILENAME
CONTENT_IDENTITY_STATE
TEXT_LAYER_STATE
DERIVATION_REQUIRED
DERIVED_FILE
PAGE_LOCATOR_STATE
OFFICIAL_CURRENTNESS_RECHECK
NOTEBOOK_UPLOAD_ELIGIBILITY
NOTES
```

`AUTO_ADVANCE = NO`
