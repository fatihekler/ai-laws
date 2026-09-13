# AI-LAWS — AI LIABILITY, CAUSATION AND REMEDY TAXONOMY

## Purpose

Provide a jurisdiction-neutral research grammar. It does not assert that any jurisdiction recognizes every category below.

## Actor taxonomy

Potentially relevant actors may include:

- model developer;
- model/provider platform;
- fine-tuner/customizer;
- deployer/integrator;
- AI agent/harness operator;
- tool/API/MCP provider;
- cloud/compute provider;
- data provider/broker;
- application publisher;
- employer/institution;
- professional user;
- end user;
- auditor/certifier;
- distributor/intermediary;
- government/public authority;
- contractor/subcontractor;
- board/officer/manager where local law makes role material.

Actor presence does not imply liability.

## Core legal-element graph

```text
ACTOR_ROLE
-> APPLICABLE_LAW
-> DUTY_OR_PROHIBITION
-> FACTS
-> STANDARD_OF_CARE / REQUIRED_CONDUCT
-> ALLEGED_BREACH
-> CAUSATION
-> LEGALLY_RECOGNIZED_DAMAGE_OR_RIGHTS_IMPACT
-> DEFENCES / EXEMPTIONS / IMMUNITIES
-> ALLOCATION_AMONG_ACTORS
-> REMEDY / SANCTION
```

Every arrow may be UNKNOWN.

## Duty research classes

- statutory/regulatory duty;
- contractual duty;
- professional duty;
- product/safety duty;
- data/privacy duty;
- cybersecurity duty;
- duty to warn/disclose;
- duty to monitor/maintain/update;
- incident-reporting duty;
- evidence/log-preservation duty;
- organizational/oversight duty;
- duty arising from control/undertaking/reliance where recognized;
- public-law duty;
- fiduciary/officer duty where applicable;
- no verified duty found / UNKNOWN.

## Breach research classes

Potential factual patterns to test against applicable law:

- unsafe release/deployment;
- excessive capability/permission grant;
- failure to constrain agent action;
- inadequate security;
- inadequate evaluation/monitoring;
- known-risk non-mitigation;
- misleading capability/safety statements;
- failure to warn;
- failure to provide human review/appeal where required;
- failure to preserve logs/evidence;
- unauthorized data/biometric/mental inference;
- failure to update/patch;
- inadequate vendor/supply-chain governance;
- organizational failure;
- prohibited practice.

These are research hypotheses, not findings of breach.

## Knowledge and foreseeability

Keep separate:

```text
PUBLIC_RISK_INFORMATION
ACTOR_SPECIFIC_NOTICE
ACTUAL_KNOWLEDGE
CONSTRUCTIVE_KNOWLEDGE / SHOULD_HAVE_KNOWN
TECHNICAL_FORESEEABILITY
LEGAL_FORESEEABILITY
```

Do not infer the legal standard from public discussion alone.

## Causation dimensions

Research, where recognized:

- factual/but-for causation;
- substantial-factor/material-contribution theories;
- proximate/legal causation;
- intervening/superseding acts;
- third-party misuse;
- user/operator contribution;
- multiple sufficient causes;
- probabilistic or evidentiary uncertainty;
- systemic/organizational causation;
- loss of chance or risk-increase theories where applicable.

## Damage / protected-interest classes

- physical injury/death;
- property loss;
- economic loss;
- privacy/data harm;
- discrimination/equality harm;
- reputational/personality harm;
- emotional/psychological harm;
- loss of autonomy/decision rights where legally recognized;
- employment/education/credit opportunity harm;
- democratic/public harm;
- environmental harm;
- security/system compromise;
- collective/systemic harm;
- legally unrecognized or disputed harm.

## Multi-actor allocation

Research whether local law recognizes:

- several liability;
- joint liability;
- joint and several liability;
- contribution/indemnity;
- vicarious liability;
- agency;
- organizational liability;
- product-chain liability;
- state liability;
- immunities/safe harbours;
- contractual allocation limits.

## Remedies

Potential remedies to research:

- injunctive/cessation orders;
- damages;
- restitution;
- correction/deletion/access rights;
- administrative orders/fines;
- product recall/withdrawal;
- licence/authorization restrictions;
- collective redress;
- criminal sanctions;
- public-law annulment/review;
- mandated audit/monitoring;
- compensation funds/insurance proceeds where legally available.

## Critical non-equivalence

```text
BAD_OUTCOME != NEGLIGENCE
NEGLIGENCE != CAUSATION
CAUSATION != COMPENSABLE_DAMAGE
VIOLATION != PRIVATE_RIGHT_OF_ACTION
REGULATORY_BREACH != AUTOMATIC_CIVIL_LIABILITY
STANDARD_NONCOMPLIANCE != AUTOMATIC_LEGAL_BREACH
STANDARD_COMPLIANCE != AUTOMATIC_DEFENCE
```
