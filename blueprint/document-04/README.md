docs/engineering/04_DECISION_ARCHITECTURE.md
markdown
# ISIL Decision Architecture & Reasoning Pipeline

## The 26-Layer Decision Engine

Every decision passes through 26 independent layers.
No layer may bypass any remaining layer.

1.  Rules Intelligence
2.  Pattern Intelligence
3.  Heuristic Intelligence
4.  Provider Intelligence
5.  Semantic Understanding
6.  Context Understanding
7.  Intent Understanding
8.  Behavioral Intelligence
9.  Graph Intelligence
10. Relationship Intelligence
11. Reputation Intelligence
12. Campaign Intelligence
13. Infrastructure Intelligence
14. Device Intelligence
15. Jurisdiction Intelligence
16. Confidence Calibration
17. Uncertainty Estimation
18. Evidence Quality Scoring
19. Provider Agreement Analysis
20. Adversarial Analysis
21. Counterfactual Analysis
22. Decision Challenge Analysis
23. Explainability Generation
24. Decision Fusion
25. Escalation Logic
26. Final Policy Decision

Additional layers may be introduced provided they
preserve compatibility, explainability, auditability,
calibration, and uncertainty estimation.

## Self-Challenge Engine

Before high-impact decisions ISIL challenges itself.

Decision Agent: Why should enforcement occur?
Defense Agent: Why might this decision be wrong?
Counterfactual Agent: What happens if content is allowed?
Risk Agent: What happens if content is blocked?
Evidence Agent: What evidence is missing?
Alternative Agent: What other explanations exist?

Major decisions must survive adversarial internal review.

If the Self-Challenge Engine cannot answer these
questions satisfactorily, enforcement severity must
be reduced or the decision escalated for human review.

## Enforcement Ladder

Enforcement progresses from least to most restrictive.
ALLOW
 ALLOW_WITH_MONITORING
 WARN
 RATE_LIMIT
 FEATURE_RESTRICT
 TEMP_RESTRICT
 REVIEW
 BLOCK
 PERMANENT_ACTION

Permanent actions require:
- exceptional evidence quality
- extremely high confidence
- explicit policy authorization
- human review where applicable

## Decision Output Schema

Every decision must return all of the following:

```json
{
  "trace_id": "string — unique decision identifier",
  "decision": "allow|allow_with_monitoring|warn|rate_limit|
               feature_restrict|temp_restrict|review|block|
               permanent_action",
  "confidence": "float 0.0-1.0",
  "uncertainty": "float 0.0-1.0",
  "risk_breakdown": {
    "toxicity": "float 0.0-100.0",
    "scam": "float 0.0-100.0",
    "cyberbullying": "float 0.0-100.0",
    "hate": "float 0.0-100.0",
    "ai_generated": "float 0.0-100.0",
    "spam": "float 0.0-100.0",
    "threat": "float 0.0-100.0"
  },
  "contributing_signals": ["list of signal names"],
  "contributing_models": ["list of model names"],
  "jurisdiction_notes": ["list of jurisdiction observations"],
  "explanation": {
    "summary": "string — one sentence plain language",
    "signals": ["list of signal objects"],
    "context_notes": ["list of context observations"],
    "memory_notes": ["list of behavioral history notes"]
  },
  "latency_ms": "float",
  "enforcement_ladder_position": "integer 0-8",
  "self_challenge_summary": {
    "challenged": "boolean",
    "outcome": "string",
    "uncertainty_change": "float"
  }
}
```

## The ISIL Reasoning Loop

Every request follows this immutable lifecycle.
No decision may skip a stage.

### Stage 1 — OBSERVE
Collect all available inputs without drawing conclusions.

Inputs:
- request content and conversation context
- behavioral signals and historical patterns
- reputation and graph relationships
- infrastructure signals and device metadata
- provider intelligence and jurisdiction rules
- policy configuration and external intelligence

All observations are timestamped, normalized,
and assigned provenance.
No enforcement decisions are made during observation.

### Stage 2 — UNDERSTAND
Transform raw observations into structured meaning.

Identify:
- intent, entities, relationships
- semantic and contextual meaning
- ambiguity, potential deception
- uncertainty sources

Understanding is descriptive, not prescriptive.

### Stage 3 — GENERATE HYPOTHESES
Generate multiple competing hypotheses:

- legitimate conversation
- educational discussion
- satire or humor
- scam attempt
- phishing or fraud
- impersonation
- coordinated abuse
- manipulation
- uncertain — insufficient evidence

Each hypothesis receives independent supporting
and conflicting evidence.

### Stage 4 — CHALLENGE
Every hypothesis must survive adversarial reasoning.

Questions:
- What evidence contradicts this?
- What assumptions are being made?
- What alternative explanations remain possible?
- What additional evidence would change the outcome?
- What is the cost of being wrong in each direction?

If uncertainty remains high, confidence must decrease.

### Stage 5 — FUSE
Independent intelligence modules contribute
calibrated evidence.

Fusion considers:
- evidence quality and independence
- model and provider agreement
- historical reliability
- uncertainty and calibration
- policy constraints

Fusion never averages opinions.
Fusion evaluates evidence.

### Stage 6 — DECIDE
Select the least restrictive action justified
by available evidence.

Decision authority is proportional to:
- confidence and evidence quality
- uncertainty and reversibility
- potential harm in each direction

Higher uncertainty always reduces enforcement authority.

### Stage 7 — EXPLAIN
Every decision is explainable.

Explanation traces:
Observed Facts
 ↓
 Derived Evidence
 ↓
 Reasoning
 ↓
 Policy Interpretation
 ↓
 Final Decision

The explanation must never invent reasoning
that did not occur.

### Stage 8 — LEARN
Learning occurs only from verified outcomes:
- successful appeals
- confirmed abuse
- confirmed false positives
- confirmed false negatives
- expert review
- validated datasets
- offline evaluation

Production behavior updated only after validation.

### Stage 8.5 — VALIDATE
Before any learning:
- validate outcome quality
- validate human review where available
- validate evaluation metrics
- validate calibration
- validate policy compliance

Only validated outcomes may influence future learning.

### Stage 9 — MEASURE
Every completed decision updates:
- correctness and calibration
- uncertainty and evidence quality
- latency and explainability quality
- consistency and appeal rate
- false positives and false negatives
- provider and model reliability
- infrastructure health

### Stage 10 — IMPROVE
No component is permanently trusted.
Every subsystem is continuously evaluated.
Continuous improvement is mandatory.
Architectural stability is preserved.

## Self-Critique Protocol

For every high-impact decision:

Q1: What evidence supports this decision?
Q2: What evidence contradicts it?
Q3: What assumptions were made?
Q4: Which assumptions are weakest?
Q5: What alternative explanations remain plausible?
Q6: What additional evidence would reduce uncertainty?
Q7: Is the proposed action proportional to the evidence?

If unanswerable, reduce enforcement or escalate.
