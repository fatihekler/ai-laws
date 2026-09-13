# AI-LAWS — NotebookLM Source Acquisition Policy

**DOCUMENT_ID:** AI-LAWS-R021-NB-SOURCE-ACQUISITION-1.0  
**STATE:** ACTIVE_RESEARCH_SUPPORT_POLICY  
**DATE:** 2026-09-13

## 1. Default policy

AI-LAWS does **not** vendor every third-party PDF into GitHub by default.

The preferred durable record is:

```text
OFFICIAL_SOURCE_URL
+ DOCUMENT_ID
+ VERSION / EFFECTIVE DATE
+ RETRIEVAL DATE
+ AUTHORITY CLASS
+ LICENSE / USE STATE
+ EXPECTED FILENAME
+ OPTIONAL SHA-256 AFTER DOWNLOAD
```

Reasons:

- legal texts change;
- consolidated texts may be updated;
- some standards are copyrighted/paywalled;
- a repository binary may become stale without warning;
- NotebookLM can accept URLs or local files;
- currentness is more important than local duplication.

## 2. Acquisition states

Use one of:

- `URL_DIRECT_PREFERRED`
- `PDF_DOWNLOAD_ALLOWED`
- `HTML_SNAPSHOT_ALLOWED`
- `MANUAL_DOWNLOAD_REQUIRED`
- `LICENSE_CHECK_REQUIRED`
- `PAYWALLED_DO_NOT_VENDOR`
- `OFFICIAL_SOURCE_NEEDS_VERIFICATION`
- `SOURCE_UNAVAILABLE`

## 3. Vendoring rule

Commit a third-party source file to GitHub only when all are true:

```text
SOURCE_IDENTITY_VERIFIED = YES
LEGAL_RESEARCH_NEEDS_PINNED_COPY = YES
LICENSE_OR_USE_RIGHT = CONFIRMED
SENSITIVE_DATA = NO
REPOSITORY_POLICY_ALLOWS = YES
```

Otherwise store only the source manifest and obtain a local copy for Notebook use where lawful.

## 4. Copyright / standards rule

Do not upload or commit paid/proprietary standards merely because they are relevant.

Examples requiring rights verification may include ISO/IEC standards and commercial legal databases.

For such materials AI-LAWS should store:

- citation;
- standard/document number;
- issuer;
- official purchase/access page;
- abstract/scope if lawfully available;
- relationship to research questions;
- `FULL_TEXT_NOT_STORED`.

## 5. Primary legal texts

For official legal texts:

- prefer official gazette / official legislation portal / treaty office / court / regulator;
- retain document/CELEX/treaty/case identifiers;
- where a current consolidated version exists, record both current consolidated source and authentic original/amending instruments when legally material;
- for multilingual law, record authentic-language status;
- translations must not silently replace authentic text.

## 6. Dynamic sources

For dynamic pages (treaty status, consolidated law, regulator guidance, implementation trackers):

```text
URL_IS_STABLE_REFERENCE
CONTENT_IS_TEMPORAL_SNAPSHOT
```

Record retrieval date. Recheck before a legal conclusion.

## 7. Notebook URL imports

URL import is preferred when:

- the official page is stable;
- text extraction works;
- no exact historical snapshot is required.

PDF/local upload is preferred when:

- exact pagination/locator matters;
- the official version is a PDF or gazette document;
- temporal version pinning matters;
- URL extraction omits legally relevant annexes/tables.

## 8. Hashing after download

If a file is downloaded for a research pack, calculate SHA-256 and record:

```text
SOURCE_ID
DOWNLOADED_AT_UTC
ORIGINAL_URL
LOCAL_FILENAME
SHA256
BYTE_SIZE
CONTENT_TYPE
```

A hash proves file identity, not legal correctness or authenticity by itself.

## 9. Sensitive material

Never put these in a public Notebook or public GitHub repo by default:

- privileged legal communications;
- personal identifiers and unnecessary personal data;
- private incident logs;
- customer data;
- credentials;
- security secrets;
- confidential contracts;
- classified/restricted government information;
- sealed court material.

## 10. Source refresh

Refresh windows are risk-based:

- current AI statutes/regulations: check before each material legal analysis;
- consolidated EU law: check current version date each time;
- treaty status: check before country-effect statements;
- current guidance/policy: check within 30 days for fast-moving topics;
- case law: verify official docket/full text before admission;
- technical frameworks: check for superseding versions before use.

## 11. Model-generated documents

ChatGPT, Grok, NotebookLM/Gemini Notebook and YargıGPT outputs may be stored in GitHub as supporting research but should not be uploaded into a primary-law Notebook as if they were legal sources.

If used for adversarial critique:

```text
PREFIX = MODEL_SUPPORTING_ONLY__
AUTHORITY_CLASS = MODEL_GENERATED_RESEARCH
CANONICAL = FALSE
```

## 12. Exact policy state

```text
BLIND_BINARY_VENDORING = NO
OFFICIAL_URL_MANIFEST = PRIMARY_ACQUISITION_RECORD
RIGHTS_CHECK_REQUIRED = YES
HASH_AFTER_DOWNLOAD = RECOMMENDED
CURRENTNESS_RECHECK = REQUIRED
MODEL_OUTPUT_AS_PRIMARY_SOURCE = PROHIBITED
```
