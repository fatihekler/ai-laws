from pathlib import Path
import csv
import hashlib
import subprocess
import tempfile
import re

DATE = "2026-09-14"
BASE_HEAD = "7215486927a66ef8c5c1ded0877b3df2b76140d1"
OFFICIAL_INC001_URL = "https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf"
INC001_PATH = Path("86_NOTEBOOKLM/downloads/INC-001 [US_GLOBAL] [OpenAI] [COMPANY-INCIDENT-DISCLOSURE] [2026-08-26-PARTIAL] — OpenAI-Hugging-Face Incident-Technical-Report.pdf")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def add_note(old: str, new: str) -> str:
    old = (old or "").strip()
    return f"{old} | {new}" if old else new


assert INC001_PATH.exists(), f"Missing existing INC-001 repository PDF: {INC001_PATH}"
repo_sha = sha256(INC001_PATH)
repo_size = INC001_PATH.stat().st_size

with tempfile.TemporaryDirectory() as td:
    official = Path(td) / "inc001-official.pdf"
    cmd = [
        "curl", "-L", "--fail", "--silent", "--show-error", "--retry", "2",
        "--user-agent", "Mozilla/5.0 (AI-LAWS source verification)",
        OFFICIAL_INC001_URL, "-o", str(official),
    ]
    subprocess.run(cmd, check=True)
    data = official.read_bytes()
    assert data.startswith(b"%PDF"), "Official INC-001 download is not a PDF body"
    official_sha = sha256(official)
    official_size = official.stat().st_size

if official_sha != repo_sha:
    raise SystemExit(f"INC-001 exact-byte mismatch: official={official_sha} repo={repo_sha}")

# 1) Reconcile manual download/action list.
manual_path = Path("86_NOTEBOOKLM/downloads/MANUAL_DOWNLOAD_AND_UPLOAD_REQUESTS.csv")
manual_fields, manual_rows = read_csv(manual_path)
for row in manual_rows:
    sid = row["source_id"]
    if sid in {f"TR-{i:03d}" for i in range(1, 9)}:
        row["current_acquisition_method"] = "ALREADY_PRESENT_NO_REDOWNLOAD"
        row["request_class"] = "CURRENTNESS_RECHECK_ONLY"
        row["notebook_upload_blocker"] = "NO"
        row["suggested_user_action"] = "No download required for Notebook ingestion. Existing verified repository snapshot may be used with currentness warning; recheck the live official source only before a material current-law conclusion."
        row["state"] = "RESOLVED_FOR_INGESTION_RECHECK_OPEN"
        row["notes"] = add_note(row.get("notes", ""), "R035: user confirmed repository file already downloaded; duplicate download request removed.")
    elif sid == "INC-001":
        row["current_acquisition_method"] = "ALREADY_PRESENT_OFFICIAL_EXACT_BYTE_MATCH"
        row["request_class"] = "RESOLVED_OFFICIAL_EXACT_BYTE_MATCH"
        row["notebook_upload_blocker"] = "NO"
        row["suggested_user_action"] = "No redownload required. Existing repository PDF exactly matches the official OpenAI CDN PDF verified by R035."
        row["state"] = "RESOLVED_FOR_INGESTION"
        row["notes"] = add_note(row.get("notes", ""), f"R035 official OpenAI CDN exact-byte match; SHA-256 {official_sha}; bytes {official_size}.")
    elif sid == "INT-004":
        row["current_acquisition_method"] = "URL_PRIMARY_NO_DOWNLOAD_REQUIRED"
        row["request_class"] = "SUPERSEDED_LOCAL_PDF_EXCLUDED"
        row["notebook_upload_blocker"] = "NO"
        row["suggested_user_action"] = "Use the UNESCO certified-copy official URL as primary. Do not upload the legacy 43GC repository PDF as the current primary source."
        row["state"] = "RESOLVED_URL_PRIMARY"
        row["notes"] = add_note(row.get("notes", ""), "R035: legacy repository file already exists but remains SUPERSEDED; no duplicate download requested.")
    elif sid == "CL-002":
        row["current_acquisition_method"] = "OFFICIAL_FULLTEXT_BLOCKED"
        row["request_class"] = "FULLTEXT_HOLD"
        row["notebook_upload_blocker"] = "YES_FOR_CL002_CASE_LAYER"
        row["suggested_user_action"] = "No repeated download attempt required now. Keep the official full-text case layer on HOLD until the Poder Judicial source becomes accessible; do not substitute a secondary copy as canonical primary full text."
        row["state"] = "HOLD_OFFICIAL_FULLTEXT"
        row["notes"] = add_note(row.get("notes", ""), "R035: official institutional case identity remains supported; official full judgment binary remains inaccessible.")
    elif sid == "TR-009":
        row["current_acquisition_method"] = "URL_PRIMARY_NO_DOWNLOAD_REQUIRED"
        row["request_class"] = "OPTIONAL_POLICY_PDF_CAPTURE"
        row["notebook_upload_blocker"] = "NO"
        row["suggested_user_action"] = "No download required for core ingestion. Preserve the official Ministry URL; capture an original PDF only if the Ministry exposes one directly."
        row["state"] = "OPTIONAL_NO_BLOCK"
        row["notes"] = add_note(row.get("notes", ""), "R035: nonbinding policy source remains optional and does not block Notebook ingestion.")
write_csv(manual_path, manual_fields, manual_rows)

# 2) Promote INC-001 exact-byte identity in manifest.
manifest_path = Path("86_NOTEBOOKLM/NOTEBOOKLM_SOURCE_ACQUISITION_MANIFEST.csv")
manifest_fields, manifest_rows = read_csv(manifest_path)
inc_manifest = None
for row in manifest_rows:
    if row["source_id"] == "INC-001":
        inc_manifest = row
        row["verification_state"] = "VERIFIED_OFFICIAL_EXACT_BYTE_MATCH_R035"
        row["last_verified"] = DATE
        row["preferred_ingest"] = "PDF_DOWNLOAD_ALLOWED"
        row["notes"] = add_note(row.get("notes", ""), f"R035: existing repository PDF exact-byte matches current official OpenAI CDN technical report; SHA-256 {official_sha}; {official_size} bytes; official landing page links the report.")
assert inc_manifest is not None, "INC-001 missing from acquisition manifest"
write_csv(manifest_path, manifest_fields, manifest_rows)

# 3) Promote INC-001 in acquisition ledger.
ledger_path = Path("86_NOTEBOOKLM/NOTEBOOKLM_ACQUISITION_AND_VALIDATION_LEDGER.csv")
ledger_fields, ledger_rows = read_csv(ledger_path)
ledger_hits = 0
for row in ledger_rows:
    if row["source_id"] == "INC-001":
        ledger_hits += 1
        row["retrieval_date"] = DATE
        row["acquisition_method"] = "PDF_DOWNLOAD_ALLOWED"
        row["local_filename_or_url"] = str(INC001_PATH)
        row["sha256"] = official_sha
        row["byte_size"] = str(official_size)
        row["content_type"] = "application/pdf"
        row["content_identity_checked"] = "OFFICIAL_EXACT_BYTE_MATCH_R035"
        row["notebook_ingest_state"] = "NOT_RUN"
        row["notes"] = add_note(row.get("notes", ""), "R035: exact official OpenAI CDN bytes equal the existing repository PDF; company incident disclosure label remains mandatory; incident != liability.")
assert ledger_hits >= 1, "INC-001 missing from acquisition ledger"
write_csv(ledger_path, ledger_fields, ledger_rows)

# 4) Promote INC-001 in downloads registry; preserve filename to avoid unnecessary namespace churn.
registry_path = Path("86_NOTEBOOKLM/downloads/DOWNLOADS_REGISTRY.csv")
registry_fields, registry_rows = read_csv(registry_path)
registry_map = {}
for row in registry_rows:
    registry_map[row["manifest_source_id"]] = row
    if row["manifest_source_id"] == "INC-001":
        row["content_identity_state"] = "CONTENT_IDENTITY_VERIFIED"
        row["currentness_state"] = "OFFICIAL_OPENAI_PDF_EXACT_BYTE_MATCH_2026-09-14"
        row["notebook_ingest_mode"] = "VERIFIED_OFFICIAL_PDF_ELIGIBLE; COMPANY_INCIDENT_DISCLOSURE_LABEL_REQUIRED"
        row["action"] = add_note(row.get("action", ""), f"R035 exact-byte match to official OpenAI CDN PDF; SHA256 {official_sha}; retain company-disclosure evidentiary label.")
write_csv(registry_path, registry_fields, registry_rows)

# 5) Update NB08 readiness.
readiness_path = Path("86_NOTEBOOKLM/NOTEBOOK_READINESS_MATRIX.csv")
readiness_fields, readiness_rows = read_csv(readiness_path)
for row in readiness_rows:
    if row["pack"] == "NB08":
        row["readiness"] = "READY_MIXED_WITH_SOURCE_CLASS_LABELS"
        row["mode"] = "INC-001/002/003 READY; INC-004 POLICY CONTEXT OPTIONAL"
        row["blockers"] = "NONE_FOR_CORE_INGESTION"
        row["notes"] = "R035 resolved INC-001 exact-byte identity. Keep company disclosure, independent investigation, vendor threat intelligence and policy essay as distinct source classes."
write_csv(readiness_path, readiness_fields, readiness_rows)

# 6) Update human catalog INC-001 section only.
catalog_path = Path("86_NOTEBOOKLM/SOURCE_CATALOG.md")
catalog = catalog_path.read_text(encoding="utf-8")
marker = "### INC-001"
start = catalog.find(marker)
if start != -1:
    end = catalog.find("\n### ", start + len(marker))
    if end == -1:
        end = len(catalog)
    section = catalog[start:end]
    section = re.sub(r"- \*\*Verification state:\*\* `[^`]*`", "- **Verification state:** `CONTENT_IDENTITY_VERIFIED_OFFICIAL_EXACT_BYTE_MATCH_R035`", section)
    section = re.sub(r"- \*\*Readiness:\*\* `[^`]*`", "- **Readiness:** `READY_PDF`", section)
    if f"SHA-256 {official_sha}" not in section:
        section += f"\n- **R035 exact-byte verification:** Official OpenAI CDN PDF matches repository bytes; SHA-256 `{official_sha}`; `{official_size}` bytes. Source remains a company incident disclosure, not an independent investigation or legal finding.\n"
    catalog = catalog[:start] + section + catalog[end:]
    catalog_path.write_text(catalog.rstrip() + "\n", encoding="utf-8")

# 7) Build pack/source Notebook upload selection from manifest + registry routing.
selection_fields = [
    "notebook_pack", "source_id", "source_type", "repository_path_or_url", "ingestion_mode",
    "readiness", "authority_label", "currentness_warning", "upload_now", "hold_reason", "notes"
]
selection = []
seen = set()
for m in manifest_rows:
    sid = m["source_id"]
    packs = {m["primary_pack"]}
    rr = registry_map.get(sid)
    if rr:
        if rr.get("primary_pack"):
            packs.add(rr["primary_pack"])
        if rr.get("secondary_pack"):
            for p in re.split(r"[;,]", rr["secondary_pack"]):
                if p.strip():
                    packs.add(p.strip())
    for pack in sorted(packs):
        if not pack:
            continue
        key = (pack, sid)
        if key in seen:
            continue
        seen.add(key)
        official_url = m.get("official_url", "")
        repo_path = ""
        if rr and rr.get("repo_filename"):
            repo_path = f"86_NOTEBOOKLM/downloads/{rr['repo_filename']}"
        source_type = m.get("authority_class", "")
        readiness = "READY_URL"
        mode = "URL"
        path_or_url = official_url
        upload_now = "YES"
        hold = ""
        currentness = m.get("verification_state", "")
        notes = m.get("notes", "")

        if sid == "CL-002":
            readiness, mode, upload_now = "HOLD", "HOLD", "NO"
            hold = "OFFICIAL_FULLTEXT_BLOCKED"
        elif sid == "INT-004":
            readiness, mode, path_or_url = "READY_URL", "URL_PRIMARY", official_url
            notes = add_note(notes, "Do not upload the legacy 43GC repository PDF as the current primary source.")
        elif sid == "US-001":
            readiness, mode, path_or_url = "READY_URL", "URL_PRIMARY", official_url
            notes = add_note(notes, "Repository webpage-print remains supporting-only.")
        elif sid == "INC-001":
            readiness, mode, path_or_url = "READY_PDF", "PDF", str(INC001_PATH)
            notes = add_note(notes, "R035 official exact-byte match verified.")
        elif sid == "INC-004":
            readiness, mode, path_or_url, upload_now = "SUPPORTING_ONLY", "URL_CONTEXT", official_url, "OPTIONAL"
            hold = "POLICY_ESSAY_NOT_INCIDENT_EVIDENCE"
        elif sid in {f"TR-{i:03d}" for i in range(1, 9)} and repo_path:
            readiness, mode, path_or_url = "READY_WITH_CURRENTNESS_WARNING", "PDF", repo_path
            currentness = "LIVE_OFFICIAL_CURRENTNESS_RECHECK_REQUIRED_BEFORE_MATERIAL_LEGAL_CONCLUSION"
        elif pack == "NB02" and sid.startswith("EU-") and repo_path:
            readiness, mode, path_or_url = "READY_PDF", "PDF", repo_path
        elif pack == "NB03" and sid in {f"US-{i:03d}" for i in range(2, 9)} and repo_path:
            readiness, mode, path_or_url = "READY_PDF", "PDF", repo_path
        elif rr and rr.get("content_identity_state") == "CONTENT_IDENTITY_VERIFIED" and repo_path and m.get("preferred_ingest") == "PDF_DOWNLOAD_ALLOWED":
            readiness, mode, path_or_url = "READY_PDF", "PDF", repo_path
        elif m.get("preferred_ingest") == "URL_DIRECT_PREFERRED" and official_url:
            readiness, mode, path_or_url = "READY_URL", "URL", official_url
        elif repo_path and rr and rr.get("content_identity_state") == "CONTENT_IDENTITY_VERIFIED":
            readiness, mode, path_or_url = "READY_PDF", "PDF", repo_path
        elif official_url:
            readiness, mode, path_or_url = "READY_URL", "URL", official_url
        else:
            readiness, mode, upload_now = "HOLD", "HOLD", "NO"
            hold = "NO_INGESTIBLE_SOURCE_PINNED"

        selection.append({
            "notebook_pack": pack,
            "source_id": sid,
            "source_type": source_type,
            "repository_path_or_url": path_or_url,
            "ingestion_mode": mode,
            "readiness": readiness,
            "authority_label": m.get("authority_class", ""),
            "currentness_warning": currentness,
            "upload_now": upload_now,
            "hold_reason": hold,
            "notes": notes,
        })
selection.sort(key=lambda r: (r["notebook_pack"], r["source_id"]))
write_csv(Path("86_NOTEBOOKLM/NOTEBOOK_UPLOAD_SELECTION.csv"), selection_fields, selection)

# 8) Pre-ingestion verification matrix.
ver_fields = ["source_id", "check", "repository_sha256", "official_sha256", "exact_byte_match", "notebook_effect", "final_state", "notes"]
ver_rows = []
for sid in [f"TR-{i:03d}" for i in range(1, 9)]:
    rr = registry_map.get(sid, {})
    ver_rows.append({
        "source_id": sid,
        "check": "EXISTING_REPOSITORY_FILE_NO_REDOWNLOAD",
        "repository_sha256": "",
        "official_sha256": "",
        "exact_byte_match": "NOT_RECHECKED_R035",
        "notebook_effect": "READY_WITH_CURRENTNESS_WARNING",
        "final_state": "ALREADY_PRESENT_NO_REDOWNLOAD",
        "notes": rr.get("currentness_state", "Live currentness remains a separate legal-conclusion gate."),
    })
ver_rows.extend([
    {"source_id": "INC-001", "check": "OFFICIAL_CDN_EXACT_BYTE_COMPARE", "repository_sha256": repo_sha, "official_sha256": official_sha, "exact_byte_match": "YES", "notebook_effect": "READY_PDF", "final_state": "VERIFIED_OFFICIAL_EXACT_BYTE_MATCH", "notes": f"Official and repository bytes identical; {official_size} bytes."},
    {"source_id": "CL-002", "check": "OFFICIAL_FULLTEXT_GATE", "repository_sha256": "", "official_sha256": "", "exact_byte_match": "NOT_APPLICABLE", "notebook_effect": "NB06_CORE_PROCEED_CASE_LAYER_HOLD", "final_state": "HOLD_OFFICIAL_FULLTEXT", "notes": "Official full judgment binary not admitted; no secondary substitute promoted."},
    {"source_id": "INT-004", "check": "PRIMARY_ROUTE", "repository_sha256": "", "official_sha256": "", "exact_byte_match": "NOT_APPLICABLE", "notebook_effect": "READY_URL", "final_state": "URL_PRIMARY_LEGACY_SUPERSEDED", "notes": "Certified-copy URL primary; legacy 43GC local PDF excluded from current-primary ingestion."},
    {"source_id": "TR-009", "check": "OPTIONAL_POLICY_SOURCE", "repository_sha256": "", "official_sha256": "", "exact_byte_match": "NOT_APPLICABLE", "notebook_effect": "READY_URL_OPTIONAL", "final_state": "OPTIONAL_NO_BLOCK", "notes": "Nonbinding policy source; exact PDF body remains optional."},
])
write_csv(Path("86_NOTEBOOKLM/downloads/PRE_INGESTION_VERIFICATION.csv"), ver_fields, ver_rows)

# 9) Durable R035 log and closeout.
ready_now = sum(1 for r in selection if r["upload_now"] == "YES")
holds = sum(1 for r in selection if r["readiness"] == "HOLD")
log = f"""# AI-LAWS-R035 — Pre-Ingestion Reconciliation Log

**Date:** {DATE}
**Base head before helper commits:** `{BASE_HEAD}`
**Purpose:** reconcile already-present files, resolve INC-001 exact-byte identity, and generate a pack-aware Notebook upload selection without performing Notebook ingestion.

## Exact-byte verification

- Official OpenAI PDF: `{OFFICIAL_INC001_URL}`
- Repository INC-001: `{INC001_PATH}`
- Official SHA-256: `{official_sha}`
- Repository SHA-256: `{repo_sha}`
- Byte size: `{official_size}`
- Exact-byte match: `YES`

The existing repository PDF was not rewritten or replaced.

## Reconciliation result

- TR-001..TR-008: already present; duplicate download requests removed; currentness warning preserved.
- INC-001: official exact-byte match verified; `READY_PDF`.
- CL-002: official full-text case layer remains `HOLD`; NB06 core may proceed.
- INT-004: certified-copy URL remains primary; legacy 43GC PDF remains superseded.
- TR-009: optional nonbinding policy source; no ingestion blocker.
- Notebook upload selection rows: `{len(selection)}`.
- Rows marked upload now: `{ready_now}`.
- Hold rows: `{holds}`.

```text
EXISTING_PDFS_REDOWNLOADED = 0
PDF_CONTENT_CHANGED = 0
NOTEBOOK_INGESTION_PERFORMED = NO
LEGAL_CLAIMS_CREATED = 0
CORE_NOTEBOOK_INGESTION_READY = YES
R019_STARTED = NO
AUTO_ADVANCE = NO
```
"""
Path("86_NOTEBOOKLM/AI-LAWS-R035_PRE_INGESTION_RECONCILIATION_LOG.md").write_text(log, encoding="utf-8")

closeout_dir = Path("95_RESEARCH/NOTEBOOK_READINESS")
closeout_dir.mkdir(parents=True, exist_ok=True)
closeout = f"""# AI-LAWS-R035 — Pre-Ingestion Reconciliation Closeout

**UNIT_ID:** `AI-LAWS-R035`
**DATE:** {DATE}
**UNIT_TYPE:** `PRE_NOTEBOOK_INGESTION_RECONCILIATION`
**BASE_HEAD:** `{BASE_HEAD}`
**STATE:** `COMPLETE_PRE_INGESTION_RECONCILIATION_INC001_EXACT_MATCH`
**LEGAL_ADVICE:** NO
**MODEL_OUTPUT_CANONICAL:** NO
**NOTEBOOK_OUTPUT_CANONICAL:** NO
**AUTO_ADVANCE:** NO

```text
INC001_OFFICIAL_SHA256 = {official_sha}
INC001_REPOSITORY_SHA256 = {repo_sha}
INC001_EXACT_BYTE_MATCH = YES
INC001_BYTE_SIZE = {official_size}
CL002_FULLTEXT = HOLD
TR001_TR008_REDOWNLOAD = NO
INT004_LEGACY_PRIMARY = NO
NEW_FILES_DOWNLOADED_TO_REPOSITORY = 0
PDF_CONTENT_CHANGED = 0
CORE_NOTEBOOK_INGESTION_READY = YES
NOTEBOOK_INGESTION_PERFORMED = NO
R019_STARTED = NO
UNKNOWN_PRESERVED = YES
AUTO_ADVANCE = NO
STOP = YES
```

Generated durable outputs:

- `86_NOTEBOOKLM/NOTEBOOK_UPLOAD_SELECTION.csv`
- `86_NOTEBOOKLM/downloads/PRE_INGESTION_VERIFICATION.csv`
- reconciled `86_NOTEBOOKLM/downloads/MANUAL_DOWNLOAD_AND_UPLOAD_REQUESTS.csv`
- `86_NOTEBOOKLM/AI-LAWS-R035_PRE_INGESTION_RECONCILIATION_LOG.md`

No ZIP, GitHub Actions artifact, OCR, PDF rewrite, bulk PDF-to-Markdown conversion, Notebook ingestion, R019 incident-corpus analysis or new substantive legal conclusion was produced.
"""
(closeout_dir / "AI-LAWS-R035_CLOSEOUT_2026-09-14.md").write_text(closeout, encoding="utf-8")

# 10) Queue + current context control reconciliation.
queue_path = Path("90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv")
queue_text = queue_path.read_text(encoding="utf-8")
if "AI-LAWS-R035," not in queue_text:
    with queue_path.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow([
            "AI-LAWS-R035", "P0", "Notebook pre-ingestion reconciliation",
            "Resolve already-present manual-download entries, verify INC-001 official exact-byte identity and produce pack-aware upload selection without Notebook ingestion",
            "COMPLETE_PRE_INGESTION_RECONCILIATION_INC001_EXACT_MATCH",
            "R034 COMPLETE",
            "86_NOTEBOOKLM/NOTEBOOK_UPLOAD_SELECTION.csv; 86_NOTEBOOKLM/downloads/PRE_INGESTION_VERIFICATION.csv; reconciled manual request list; R035 log/closeout",
            "core Notebook ingestion ready; CL-002 official fulltext remains case-layer hold; stop before Notebook ingestion or R019",
        ])

context_path = Path("00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md")
context = context_path.read_text(encoding="utf-8")
if "R035_PRE_INGESTION_RECONCILIATION_COMPLETE" not in context:
    context = context.replace(" / LEGAL_RESEARCH_ACTIVE", " / R035_PRE_INGESTION_RECONCILIATION_COMPLETE / LEGAL_RESEARCH_ACTIVE", 1)
if "AI-LAWS-R035 = COMPLETE_PRE_INGESTION_RECONCILIATION_INC001_EXACT_MATCH" not in context:
    anchor = "AI-LAWS-R034 = COMPLETE_HUMAN_READABLE_NAMESPACE_AND_NOTEBOOK_READINESS\n"
    if anchor in context:
        context = context.replace(anchor, anchor + "AI-LAWS-R035 = COMPLETE_PRE_INGESTION_RECONCILIATION_INC001_EXACT_MATCH\n", 1)
    context += "\n### R035 — Pre-ingestion reconciliation\n\n```text\nSTATE = COMPLETE_PRE_INGESTION_RECONCILIATION_INC001_EXACT_MATCH\nINC001_EXACT_BYTE_MATCH = YES\nCL002_FULLTEXT = HOLD\nCORE_NOTEBOOK_INGESTION_READY = YES\nNOTEBOOK_INGESTION_PERFORMED = NO\nR019 = NOT_STARTED\nAUTO_ADVANCE = NO\n```\n"
context_path.write_text(context.rstrip() + "\n", encoding="utf-8")

print(f"INC001_OFFICIAL_SHA256={official_sha}")
print(f"INC001_REPOSITORY_SHA256={repo_sha}")
print("INC001_EXACT_BYTE_MATCH=YES")
print(f"INC001_BYTES={official_size}")
print(f"NOTEBOOK_UPLOAD_SELECTION_ROWS={len(selection)}")
print(f"NOTEBOOK_UPLOAD_NOW_ROWS={ready_now}")
print(f"NOTEBOOK_HOLD_ROWS={holds}")
print("CORE_NOTEBOOK_INGESTION_READY=YES")
print("PDF_CONTENT_CHANGED=0")
print("AUTO_ADVANCE=NO")
