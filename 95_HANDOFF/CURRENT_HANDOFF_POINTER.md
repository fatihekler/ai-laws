# AI-LAWS — CURRENT HANDOFF POINTER

**STATE:** ACTIVE
**DATE:** 2026-09-14
**REPOSITORY:** `fatihekler/ai-laws`
**BRANCH:** `main`
**AUTO_ADVANCE:** NO

## Current continuity files

```text
CURRENT_MASTER = 95_HANDOFF/AI_LAWS_NEW_CHAT_CONTINUITY_MASTER_2026-09-14.md
CURRENT_CHECKLIST = 95_HANDOFF/AI_LAWS_NEW_CHAT_BOOTSTRAP_CHECKLIST_2026-09-14.md
CURRENT_STATUS_FORMAT = 95_HANDOFF/AI_LAWS_NEW_CHAT_STATUS_FORMAT_2026-09-14.md
CURRENT_READY_TO_PASTE = 95_HANDOFF/READY_TO_PASTE_NEW_CHAT_PROMPT.txt
CURRENT_CONTEXT = 00_CONTROL/CURRENT_CONTEXT_AND_NEXT_ACTION.md
CURRENT_QUEUE = 90_RESEARCH_QUEUE/INITIAL_RESEARCH_QUEUE.csv
```

## Handoff baseline

```text
HANDOFF_BASE_HEAD = 4e23cbfa8448f3316ab44f82c809ccf448bdd7aa
HANDOFF_BASE_TREE = dd85468d005a5bf7cf7addb282719e712ef811a8
HANDOFF_BASE_COMMIT_MESSAGE = chore(r011): remove temporary human-sovereignty workflows
R011_STATE = COMPLETE_RESEARCH_BASELINE_L1_L2_RIGHTS_MAP_SCOPE_LIMITS_OPEN
```

The current branch HEAD after this handoff package is committed will be newer than `HANDOFF_BASE_HEAD`. A new chat must always fresh-read `main` HEAD/TREE and must not treat the baseline SHA above as a permanent current pointer.

## Mandatory new-chat order

1. Fresh-read `main` HEAD/TREE.
2. Read `README_START_HERE.md`.
3. Read `00_CONTROL/NEW_CHAT_BOOTSTRAP.md`.
4. Read this pointer.
5. Read `CURRENT_MASTER`.
6. Read `CURRENT_CHECKLIST`.
7. Read `CURRENT_STATUS_FORMAT`.
8. Read `00_CONTROL/AI_LAWS_MASTER_RESEARCH_NOTEBOOK_ORCHESTRATION.md`.
9. Continue the mandatory control/taxonomy/jurisdiction/Notebook/queue order defined by the bootstrap and master.
10. Read exact files relevant to the selected bounded unit.
11. Before mutation/download/upload, fresh-read HEAD/TREE again and stop on unexplained overlapping drift.

## Control rule

```text
CURRENT_GITHUB_STATE > HANDOFF_BASELINE > CHAT_EXPORT > MODEL_MEMORY
USER_SAYS_CONTINUE != UNLIMITED_AUTO_ADVANCE
AUTO_ADVANCE = NO
```

If this pointer conflicts with fresher current GitHub control files, the fresher current GitHub state controls and the conflict must be reported rather than silently repaired.
