# AI-LAWS — CETS No. 225 Current Treaty-Status / Declaration / Implementation Map

**WORK_ITEM:** `AI-LAWS-R004`
**RESEARCH_DATE:** 2026-09-14
**OFFICIAL_TREATY_OFFICE_STATUS_AS_OF:** 2026-09-12
**JURISDICTION:** Council of Europe treaty system
**LEVEL:** L1/L2 treaty-status baseline
**LEGAL_ADVICE:** NO
**AUTO_ADVANCE:** NO

## 1. Controlled source set

Primary official sources for this bounded unit:

- Treaty detail: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225
- Signature/ratification chart: https://www.coe.int/en/web/conventions/full-list?module=signatures-by-treaty&treatynum=225
- Reservations/declarations page: https://www.coe.int/en-GB/web/conventions/full-list?codeNature=0&module=declarations-by-treaty&numSte=225
- Council of Europe AI Convention overview: https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence
- Official treaty text: https://rm.coe.int/1680afae3c
- Official Explanatory Report: https://rm.coe.int/1680afae67

Repository source `INT-001` remains a verified 12-page treaty-text snapshot. It is **not** a current party-status snapshot. Dynamic signature, ratification, declaration, reservation and entry-into-force claims must use the live Treaty Office layer.

```text
REPOSITORY_TREATY_TEXT != LIVE_TREATY_STATUS
SIGNATURE != RATIFICATION_OR_APPROVAL
RATIFICATION_BY_ONE_ENTITY != TREATY_ENTRY_INTO_FORCE
LEGALLY_BINDING_TREATY_FORM != CURRENTLY_IN_FORCE
DECLARATION_AT_SIGNATURE != DOMESTIC_IMPLEMENTATION_VERIFIED
```

## 2. Instrument identity and entry-into-force rule

CETS No. 225 is the **Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law**. It was adopted by the Committee of Ministers on 17 May 2024 and opened for signature in Vilnius on 5 September 2024.

Article 30 makes the Convention subject to ratification, acceptance or approval. Under Article 30(3), treaty-wide entry into force requires five Signatories to express consent to be bound, including at least three Council of Europe member States; entry into force then occurs on the first day of the month after expiry of three months from the fifth qualifying consent.

As of the official Treaty Office status snapshot `2026-09-12`:

```text
TOTAL_SIGNATORIES = 21
SIGNATURES_NOT_FOLLOWED_BY_RATIFICATION_OR_APPROVAL = 20
RATIFICATIONS_OR_APPROVALS = 1
QUALIFYING_COE_MEMBER_RATIFICATIONS = 0
ONLY_APPROVAL_DEPOSITED = EUROPEAN_UNION_2026-05-15
ENTRY_INTO_FORCE_THRESHOLD_MET = NO
TREATY_WIDE_ENTRY_INTO_FORCE = NOT_YET
```

The current Council of Europe AI overview separately lists the European Union under “Parties” and lists the 21 signatories. R004 preserves the controlling Article 30 threshold and Treaty Office status: one deposited approval does not satisfy the five-consent / three-member-State threshold.

## 3. Current signatory set

The exact 21-row status matrix is stored in `CETS_225_SIGNATURE_RATIFICATION_MATRIX.csv`.

Council of Europe member-State signatories (15): Albania, Andorra, Armenia, Bosnia and Herzegovina, Georgia, Iceland, Liechtenstein, Montenegro, North Macedonia, Norway, Republic of Moldova, San Marino, Switzerland, Ukraine and the United Kingdom.

Non-member participants that have signed (5): Canada, Israel, Japan, United States of America and Uruguay.

International organisation signatory/approver (1): European Union.

No Council of Europe member State has deposited ratification/acceptance/approval in the current Treaty Office snapshot.

## 4. Reservations and declarations

The current Treaty Office reservations/declarations page displays declarations for three entities and no reservation entries for CETS No. 225 in the retrieved current result.

### European Union

On 15 May 2026, with its instrument of approval, the European Union deposited:

- an Article 3(1)(b) declaration stating that, for relevant private-actor activities, it will apply Chapters II to VI through implementation of Regulation (EU) 2024/1689 (the EU AI Act), with other relevant Union acquis potentially also contributing; and
- an Article 32(1) territorial-scope declaration tying application, within Union competence, to the territories in which the EU Treaties apply under the stated EU Treaty rules.

This declaration records the EU's implementation route. It does not convert the CETS 225 treaty into an already-entered-into-force instrument.

### Norway

At signature on 5 September 2024, Norway declared under Article 3(1)(b) that it shall apply the principles and obligations in Chapters II to VI to private-actor activities.

Norway remains signed but not ratified in the current Treaty Office status. R004 therefore treats this as a recorded prospective treaty-scope declaration, not proof that CETS 225 is already in force domestically for Norway.

### Ukraine

At signature on 15 May 2025, Ukraine deposited:

- an Article 3(1)(b) declaration choosing the “other appropriate measures” route for private entities not covered by Article 3(1)(a); and
- an Article 32(1) territorial declaration concerning territory temporarily occupied by the Russian Federation, under the conditions stated in the declaration.

Ukraine remains signed but not ratified in the current Treaty Office status. Domestic implementation and legal effect are not inferred by R004.

### Reservation state

Article 34 allows only the reservation contemplated by Article 33(1) and excludes reservations to other provisions. The current Treaty Office result retrieved for CETS 225 displays no reservation entries. Because the Treaty Office is dynamic, this is recorded as a dated current-source state, not an immutable proposition.

## 5. Implementation-status boundary

R004 maps **treaty participation and declared implementation route**, not national implementing law.

- European Union: approval deposited; Article 3 private-actor route declared through the AI Act and relevant Union acquis; CETS 225 itself has not yet entered into force.
- Norway: signature only; Article 3 declaration selects direct application of Chapters II–VI to private actors if/when treaty obligations become operative; domestic implementation not verified here.
- Ukraine: signature only; Article 3 declaration selects other appropriate measures; territorial declaration recorded; domestic implementation not verified here.
- Remaining signatories: signature dates verified; no current CETS 225 declaration displayed for them in the Treaty Office result used by R004; domestic implementation not researched.

The EU AI Act and other domestic/regional laws may already create independent obligations. Their independent legal force must not be attributed to CETS 225 while the Framework Convention remains not yet in force.

```text
EU_AI_ACT_APPLICABLE != CETS225_IN_FORCE
NATIONAL_AI_LAW_OR_POLICY != CETS225_IMPLEMENTATION_PROVEN
SIGNATORY_STATUS != DOMESTIC_DIRECT_EFFECT
NO_DECLARATION_DISPLAYED != NO_DOMESTIC_MEASURES
```

## 6. Monitoring / follow-up state

The Convention provides a follow-up mechanism in Chapter VII, but the Conference of the Parties cannot be treated as an already-operational treaty body before the Convention enters into force. The current Council of Europe digital-governance layer identifies CDNET as custodian of the Framework Convention until the Conference of the Parties is established.

R004 does not infer enforcement powers, individual complaint rights or civil-liability consequences from the Convention.

## 7. R004 stop boundary

R004 does **not** determine:

- the domestic legal effect of signature under each signatory's constitutional/treaty law;
- general international-law consequences of signature pending entry into force;
- national ratification procedures currently underway but not deposited with the Treaty Office;
- national implementing legislation, regulations, administrative measures or voluntary measures;
- ECHR case-law implications or interaction with existing Council of Europe instruments;
- concrete actor classification, breach, causation, damages, sanctions or remedies;
- whether any State will ratify in the future or when the Article 30 threshold will be met.

```text
R004_CETS225_L1_L2_STATUS_BASELINE = COMPLETE
TREATY_WIDE_ENTRY_INTO_FORCE = NO
DOMESTIC_IMPLEMENTATION_MAP = NOT_ATTEMPTED_BEYOND_OFFICIAL_DECLARED_ROUTE
CASE_LAW = NOT_ATTEMPTED
LIABILITY_CONCLUSION = NOT_ATTEMPTED
NEW_BINARY_DOWNLOADS = 0
NOTEBOOK_UPLOADS = 0
DERIVED_MARKDOWN_CREATED = 0
ZIP_OR_ARTIFACT_CREATED = NO
AUTO_ADVANCE = NO
```
