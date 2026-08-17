docs/engineering/05_PRODUCTION_ENGINEERING.md
markdown
# ISIL Production Engineering Standards

## Repository-First Workflow

Never begin implementation immediately.

Always execute this exact sequence:

1. Scan every file in the repository
2. Understand the full architecture
3. Build complete dependency maps
4. Identify all existing adapters, pipelines, engines
5. Identify all protected production components
6. Identify genuine architectural gaps
7. Produce a detailed implementation plan
8. STOP and wait for explicit approval
9. Implement incrementally after approval
10. Run tests continuously during implementation
11. Verify correctness, calibration, traceability
12. Deliver architecture summary and tradeoffs

## Engineering Execution Contract

### UNDERSTAND
- Never modify code before understanding architecture
- Reuse existing abstractions whenever practical
- Prefer extension over replacement
- Do not invent new patterns when established ones exist

### DESIGN
- State assumptions explicitly
- Identify constraints and tradeoffs
- Evaluate at least one alternative design
- Explain why the chosen design is preferred

### IMPLEMENT
- Make the smallest safe change that achieves
  the objective
- Preserve backward compatibility unless explicitly
  approved
- Avoid duplicate logic
- Keep responsibilities isolated
- Use configuration instead of hard-coded behavior

### VERIFY
- Validate correctness before optimization
- Run relevant tests after every meaningful change
- Confirm existing functionality continues to work
- Verify logging, metrics, tracing, error handling

### DOCUMENT
- Record architectural decisions
- Explain non-obvious implementation choices
- Identify limitations and future extension points

### SAFETY
- Never sacrifice correctness for speed
- Never sacrifice maintainability for convenience
- Never sacrifice explainability for automation
- Never sacrifice reliability for novelty

### FINAL CHECK
Before presenting work, confirm:
✓ The repository was understood
✓ Existing systems were preserved
✓ No unnecessary files were created
✓ No existing functionality was duplicated
✓ Compatibility was maintained
✓ Tests passed
✓ Risks are documented
✓ Tradeoffs are explained
✓ The implementation is production-ready

If any item cannot be verified, explicitly state why.

## Execution Rules

### 1. Think Before Coding
Never immediately write code.
Always read, understand, trace, identify, plan first.
Only then implement.

### 2. One Phase at a Time
Never modify multiple major systems simultaneously.
Complete one phase. Validate. Test. Document. Stop.
Wait for approval. Then continue.

### 3. Phase Completion Requirements
A phase is complete only when:
✓ Architecture validated
✓ Code implemented
✓ Tests passing
✓ Integration verified
✓ Logging verified
✓ Metrics verified
✓ Documentation updated
✓ Security reviewed
✓ Backward compatibility preserved
If any item cannot be verified, stop.

### 4. Small Safe Changes
Prefer: extend, compose, adapt, configure, version
Avoid: rewrite, replace, duplicate, remove, redesign
unless explicitly approved.

### 5. Continuous Validation
After every meaningful change verify:
tests, architecture, integration, explainability,
observability, calibration, uncertainty, compatibility.
Never assume correctness.

### 6. Engineering Discipline
Before every implementation ask:
- What problem exists?
- Why does it exist?
- Can existing code solve it?
- Is there a simpler solution?
- What are the tradeoffs?
- How will this affect future maintenance?
- How can this fail?
- How will it be tested?

### 7. Output Format
Every completed phase ends with:
1. Completed work
2. Architecture impact
3. Risks
4. Tradeoffs
5. Tests performed
6. Remaining work
7. Recommended next phase
Then STOP. Never automatically continue.

### 8. Quality Standard
Every implementation must be:
deterministic, testable, observable, documented,
maintainable, modular, configurable, auditable,
explainable, provider-independent, backward-compatible.

### 9. Safety Override
If uncertainty exists: STOP. Ask for clarification.
Incorrect implementation is worse than delayed.

### 10. Final Law
Think deeper. Code less. Measure more. Verify everything.
Every change must leave ISIL objectively better than before.

## System Evolution & Change Management

Every architectural modification follows:

1. Proposal
2. Architecture Review
3. Risk Analysis
4. Threat Modeling
5. Prototype
6. Offline Evaluation
7. Benchmark Comparison
8. Security Review
9. Privacy Review
10. Performance Review
11. Controlled Rollout
12. Production Monitoring
13. Post-Deployment Evaluation

Every stage possesses veto authority.
Rejected changes shall never enter production.

## Versioned Reasoning

Every decision records:
- reasoning version
- policy version
- model version
- configuration version
- feature flags
- jurisdiction version
- deployment version
- evidence schema version

Future upgrades shall never invalidate historical
reasoning.

## Reliability Engineering

ISIL continuously measures:
availability, uptime, latency, throughput, queue depth,
dependency health, timeout rate, retry rate,
overload conditions, degraded-mode activation.

Failures shall degrade gracefully.
Safety shall never depend upon a single component.

## Resilience

Every subsystem shall tolerate:
provider failures, model failures, cloud failures,
regional outages, network partitions, corrupted inputs,
malformed requests, unavailable intelligence providers,
partial infrastructure loss.

Degrade safely rather than fail catastrophically.

## Privacy Engineering

ISIL implements:
- data minimization
- configurable retention
- encryption in transit and at rest
- jurisdiction-aware retention policies
- audited access to sensitive data
- least-privilege access

Personal information shall never be retained longer
than operationally necessary.

## Security Engineering

Zero Trust on every interface.

Requires:
- authentication and authorization
- validated configuration
- verified dependencies
- secret management
- secure defaults
- hostile-input assumptions
- mandatory security review before production

Security is an architectural requirement — not optional.

## Observability

Every subsystem shall emit:
- structured logs
- distributed traces
- metrics
- health signals
- dependency status
- calibration metrics
- uncertainty metrics
- performance metrics

If a system cannot be observed, it cannot be trusted.

## Human Governance

ISIL augments human judgment.
ISIL does not replace organizational accountability.

Human oversight remains available whenever:
- uncertainty exceeds approved thresholds
- legal significance exists
- irreversible actions are considered
- policy requires review

Authority remains with people.
ISIL provides evidence, reasoning, calibration,
and explanation — not autonomous governance.

This section overrides all implementation behavior.
