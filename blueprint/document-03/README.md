docs/engineering/03_SYSTEM_ARCHITECTURE.md
markdown
# ISIL System Architecture & Cognitive Design

## System Brain

ISIL is organized around a central reasoning system
known as the ISIL System Brain.

The System Brain is not a single AI model.

It is a deterministic orchestration and reasoning layer
that coordinates specialized intelligence modules while
ensuring that no individual model, provider, rule, or
signal can independently determine a final outcome.

### System Brain Responsibilities
- Orchestrating the complete decision pipeline
- Coordinating all intelligence layers
- Managing and validating evidence collection
- Calibrating confidence and uncertainty
- Resolving model disagreement
- Performing adversarial self-challenge
- Choosing the least restrictive safe action
- Generating explainable decisions
- Maintaining complete auditability
- Monitoring system health and degradation
- Learning from validated feedback only

### System Brain Constraints
The System Brain never bypasses engineering principles.
The System Brain never bypasses safety mechanisms.
The System Brain never bypasses human governance.
The System Brain never replaces protected infrastructure.

If confidence is insufficient, the System Brain must
reduce enforcement authority rather than increase it.

## Cognitive Architecture

### 1. World Model
Maintains a continuously updated representation of:
- users, conversations, devices, identities
- providers, networks, infrastructure
- jurisdictions, historical behavior
- campaigns, trust relationships

### 2. Memory System
Memory horizons:
- request memory — current request context
- session memory — current session context
- investigation memory — active investigation context
- long-term statistical memory — aggregate patterns
- privacy-preserving historical memory — anonymized history

Memory is governed by configurable retention policies
and jurisdiction-specific privacy requirements.

### 3. Evidence Engine
Collects, normalizes, validates, timestamps, and scores
evidence from every independent source before any
reasoning begins.

Evidence is never modified after collection.
Evidence provenance is always recorded.

### 4. Reasoning Engine
Transforms evidence into structured hypotheses rather
than immediate conclusions.

Every hypothesis includes:
- supporting evidence
- conflicting evidence
- confidence estimate
- uncertainty estimate
- assumptions made
- alternative explanations

### 5. Decision Engine
Selects the least harmful action consistent with
available evidence, calibrated uncertainty, and
applicable policy.

### 6. Learning Engine
Learns only from verified outcomes:
- successful appeals
- confirmed abuse
- confirmed false positives
- confirmed false negatives
- expert review
- validated datasets
- offline evaluation

Learning must never modify production behavior directly
without validation and approval.

### 7. Calibration Engine
Continuously measures whether confidence estimates
correspond to observed correctness.

Adjusts calibration when drift is detected.

### 8. Policy Engine
Separates policy from implementation.

Policies are:
- configurable
- versioned
- auditable
- jurisdiction-aware
- independently testable

### 9. Safety Governor
Acts as the final safeguard.

The Safety Governor may reduce enforcement severity
or require human review whenever confidence, evidence
quality, or policy certainty are insufficient.

### 10. Explainability Engine
Produces human-readable reasoning for every decision.

Every explanation must:
- accurately reflect the reasoning process
- distinguish observed facts from inferred conclusions
- represent uncertainty honestly
- explain policy interpretation

### 11. Evaluation Engine
Continuously measures production quality.

Metrics include:
- Precision, Recall, F1 Score
- ROC-AUC, Brier Score
- Expected Calibration Error
- False Positive Rate, False Negative Rate
- Human Agreement Rate
- Appeal Success Rate
- Latency, Throughput
- Drift Detection, Reliability

No model improvement is accepted without measurable
evaluation gains.

### 12. Threat Intelligence Engine
Consumes independent external intelligence:
- phishing feeds
- malware intelligence
- fraud intelligence
- abuse intelligence
- domain, IP, URL, certificate reputation
- infrastructure reputation

Threat intelligence contributes evidence.
Threat intelligence alone never authorizes enforcement.

### 13. Experimentation & Evaluation Sandbox
Every new model, provider, policy, or reasoning component
must execute inside an isolated evaluation environment
before affecting production.

Production behavior shall not change until offline
evaluation demonstrates statistically significant
improvement.

## Jurisdiction Intelligence

Jurisdiction intelligence is modular, configurable,
and independently deployable.

Each jurisdiction pack includes:
- financial fraud patterns
- payment system abuse patterns
- government impersonation patterns
- identity abuse patterns
- platform abuse patterns
- regulatory requirements
- cultural context
- language-specific abuse patterns

### Current Jurisdiction Packs
- GLOBAL — universal baseline
- US — IRS scams, Medicare fraud, SSN fraud
- EU — GDPR-aligned, hate speech regulation
- UK — HMRC scams, delivery fraud
- CA — CRA fraud, Quebec language rules
- AU — ATO fraud, regional patterns
- IN — UPI fraud, Aadhaar fraud, OTP scams
- PK — Easypaisa scams, JazzCash fraud,
       fake NADRA, fake banking calls
- JP — Line fraud, convenience store scams
- SG — SingPass fraud, CPF scams
- BR — PIX fraud, CPF fraud
- UAE — Emirates ID scams, visa fraud

New jurisdictions are added without changing the
core reasoning architecture.

## Protected Infrastructure

The following components are protected.
They may not be overwritten or replaced without
explicit architectural approval.

- app/adapters/ — all adapter implementations
- app/core/fusion.py — fusion engine
- app/db/models.py — database models
- app/db/session.py — database session
- app/config.py — configuration system

All protected components are extended, integrated,
and preserved through backward-compatible engineering.

## High-Level Data Flow

```
Request arrives
    ↓
Input validation
    ↓
Parallel adapter execution
    ↓
Evidence collection and normalization
    ↓
Context intelligence analysis
    ↓
Memory modifier calculation
    ↓
Fusion engine aggregation
    ↓
Self-challenge engine
    ↓
Decision selection
    ↓
Explanation generation
    ↓
Audit storage
    ↓
Response returned
```
