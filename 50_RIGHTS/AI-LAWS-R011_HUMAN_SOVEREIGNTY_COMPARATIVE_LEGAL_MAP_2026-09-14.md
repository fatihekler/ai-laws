# AI-LAWS-R011 — Human Sovereignty Comparative Legal Map

**UNIT_ID:** `AI-LAWS-R011`  
**RESEARCH_DATE:** 2026-09-14  
**STATE:** `COMPLETE_RESEARCH_BASELINE_L1_L2_RIGHTS_MAP_SCOPE_LIMITS_OPEN`  
**LEGAL_ADVICE:** NO  
**AUTO_ADVANCE:** NO

## 1. Scope

This bounded unit maps selected verified legal protections relevant to human sovereignty: dignity, physical and mental integrity, privacy, personal-data protection, manipulation and vulnerability exploitation, biometric/emotion inference, automated-decision safeguards, contestability, remedy, children/vulnerable persons, and Chile-specific brain-activity protections.

It does **not** declare a universal named right of `cognitive liberty`, does not admit blocked case law, and does not convert soft law or a treaty instrument that is not yet treaty-wide in force into currently binding universal law.

## 2. Controlled source set

| Source | Authority state | R011 use | Critical limit |
|---|---|---|---|
| `EU-004` Charter of Fundamental Rights | binding EU primary law within its field of application | dignity; mental integrity; private life; data protection; non-discrimination; children; remedy | Article 51 scope controls; not a universal/global source |
| `EU-005` GDPR | binding EU regulation | consent withdrawal; special-category data; information/access/rectification/erasure/restriction/objection; Article 22 automated-decision safeguards | rights are conditional and provision-specific; no general AI opt-out inferred |
| `EU-001` AI Act consolidated 2026-07-27 | binding EU regulation with phased application | manipulation/vulnerability exploitation; emotion recognition; biometric categorisation; AI-interaction/transparency duties | provision/date/scope/exceptions must be preserved; new 2026/1744 Article 5(ba)/(bb) provisions are not treated as already applicable on 2026-09-14 |
| `INT-001` CETS No. 225 | legally binding treaty form, but treaty-wide entry into force not achieved in R004 status snapshot | dignity/autonomy; transparency; accountability; equality; remedies; contestability/procedural safeguards | R004 status as of 2026-09-12: Article 30 threshold unmet; no current treaty-wide duty inferred |
| `INT-003` UNESCO AI Ethics Recommendation | nonbinding soft law | dignity, agency/autonomy, vulnerable persons, human-rights ethics framing | recommendation is not statute/treaty/court holding |
| `INT-004` UNESCO Neurotechnology Recommendation | nonbinding soft law; certified-copy identity pinned | neurotechnology ethics/mental privacy research framing | R011 live ARK body extraction returned shell-only; clause-level claims are not newly asserted here |
| `CL-001` Chile Ley 21.383 | Chile-specific constitutional amendment anchor | physical/psychological integrity; special safeguarding of brain activity and information derived from it | current constitutional text still requires recheck before broad jurisdiction-wide conclusions |
| `CL-002` Girardi / Emotiv, Corte Suprema Rol 105.065-2023 | official docket identity pinned; official full text unavailable | blocker/evidence-gap only | `CASE_LAW_ADMISSION = BLOCKED`; no holding is imported into this map |

## 3. Comparative findings

### Dignity and integrity

`EU-004` expressly protects human dignity (Article 1) and physical and mental integrity (Article 3), but Charter Article 51 limits its field of application. `INT-001` Article 7 places human dignity and individual autonomy in the treaty text, while the R004 entry-into-force gate remains controlling. `INT-003` reinforces dignity as nonbinding international soft law.

### Brain activity / neurotechnology versus ordinary inference

`CL-001` is a narrow positive-law anchor concerning technology used on persons and special safeguarding of brain activity and information derived from it. That is not interchangeable with ordinary behavioural profiling or AI emotion inference. R011 therefore preserves:

```text
DIRECT_NEURAL_OR_BRAIN_ACTIVITY_DATA != ORDINARY_BEHAVIOURAL_INFERENCE
CHILE_NEURORIGHTS_ANCHOR != UNIVERSAL_COGNITIVE_LIBERTY_RIGHT
```

### Emotion recognition and biometric categorisation

The controlled `EU-001` snapshot defines emotion-recognition systems through inference of emotions or intentions from biometric data. Article 5 prohibits specified workplace/education emotion inference subject to the medical/safety exception, and prohibits specified sensitive-attribute biometric categorisation. Article 50 separately requires transparency for permitted emotion-recognition/biometric-categorisation uses within its scope. These rules are narrower than a generalized mental-privacy prohibition.

### Manipulation and vulnerability

AI Act Article 5(1)(a) and (b) regulate defined manipulative/deceptive techniques and exploitation of specified vulnerabilities. R011 does not convert these provisions into a general autonomy tort: the statutory elements, including material distortion and the significant-harm condition, remain necessary.

### Automated decisions, human intervention and contestability

GDPR Article 22(1) concerns decisions based solely on automated processing that produce legal effects or similarly significant effects. Article 22(2) contains exceptions. Under Article 22(3), specified exception routes require safeguards including human intervention, expression of the data subject's point of view, and contestability. This is not a general right to human review of every AI output.

CETS 225 Articles 14–15 contain remedy, contestability and procedural-safeguard language in the treaty text, but R004's treaty-status gate prevents treating those provisions as treaty-wide in-force obligations on 2026-09-14.

### Correction, deletion, restriction and objection

GDPR Articles 16–18 and 21 create specific rectification, erasure, restriction and objection rights under their own conditions and exceptions. R011 does not rename these collectively as a universal legal right of “reversibility”.

### Children and vulnerable persons

EU Charter Article 24 protects children's interests within Charter scope. AI Act Article 5 includes a vulnerability-exploitation prohibition keyed to age, disability or specific social/economic situation and defined effects/harms. UNESCO AI Ethics provides additional nonbinding ethical framing for vulnerable persons.

## 4. Cognitive-liberty terminology result

The exact phrase `cognitive liberty` was not found in the selected controlled binding EU texts (`EU-001`, `EU-004`, `EU-005`) during the R011 GitHub probe.

This result is deliberately narrow:

```text
SELECTED_SOURCE_TERM_NOT_FOUND != UNIVERSAL_RIGHT_DOES_NOT_EXIST
SCHOLARLY_OR_POLICY_LABEL != AUTOMATIC_POSITIVE_LAW_RIGHT
```

R011 therefore treats `cognitive liberty` as a comparative research label unless and until a specific jurisdiction/source expressly supplies a legally recognized right or an accepted doctrinal equivalent.

## 5. Currentness and access limits

- R011 live EUR-Lex ELI requests returned HTTP 202 with empty bodies in the GitHub runner. Previously verified exact official EUR-Lex snapshots/currentness pins therefore remain the controlled basis; currentness remains temporal.
- `CL-001` returned an official BCN page shell, but the targeted constitutional text was not extractable in this run. The prior exact source pin is preserved without broadening it.
- `CL-002` returned an anti-bot/human-challenge page rather than official judgment full text. Full-text admission remains blocked.
- UNESCO ARK pages returned shell-only HTML in this run. Existing verified source identities are preserved; no new clause-level certified-copy claims are inferred.
- Live Council of Europe Treaty Office access returned HTTP 403 in this run. R004's dated 2026-09-12 treaty-status snapshot remains controlling.

## 6. No liability conclusion

This unit does not determine breach, causation, damage, remedy entitlement or liability for any actor. It creates a rights/protection research baseline only.

```text
RIGHT_OR_PROTECTION_IDENTIFIED != BREACH_PROVEN
BREACH != CAUSATION
CAUSATION != COMPENSABLE_DAMAGE
```

## 7. Stop

```text
CASE_LAW_ADMITTED = 0
LIABILITY_CONCLUSION = NOT_ATTEMPTED
UNIVERSAL_COGNITIVE_LIBERTY_RIGHT = NOT_INFERRED
NOTEBOOK_UPLOADS = 0
NEW_SOURCE_BINARY_DOWNLOADS = 0
ZIP_OR_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
STOP = YES
```
