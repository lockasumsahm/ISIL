docs/engineering/02_ENGINEERING_CONSTITUTION.md
markdown
# ISIL Engineering Constitution & Prime Directive

## Engineering Philosophy

Understand before changing.
Preserve before replacing.
Extend before rewriting.
Measure before optimizing.
Test before merging.
Explain before enforcing.

Do not guess. If information is missing, stop and ask.

When goals conflict, prioritize long-term correctness
over short-term speed.

## Foundational Principles

No single model may make a final decision.
No single signal may make a final decision.
No single provider may make a final decision.
No single rule may make a final decision.
No single dataset may make a final decision.

Final decisions emerge only through evidence convergence.

If evidence conflicts:
- increase uncertainty
- reduce confidence
- reduce enforcement severity
- prefer reversible actions
- prefer review over block

Uncertainty is preferable to incorrect certainty.

## The Prime Directive

ISIL is an evidence-driven trust infrastructure whose
purpose is to help digital systems make the most correct
decision that can be justified by available evidence
while explicitly representing uncertainty.

### The Prime Law

Every implementation must make ISIL objectively better
in at least one measurable dimension without making
another critical dimension worse.

If no measurable improvement can be demonstrated,
the change must not be implemented.

### Acceptable Improvements

- higher decision correctness
- lower false positives or false negatives
- better confidence calibration
- stronger evidence quality
- greater explainability
- stronger privacy guarantees
- improved resilience or lower latency
- better scalability or maintainability
- greater observability or auditability
- simpler architecture with equivalent capability

## Architectural Laws — Immutable

### LAW I — Architecture Before Implementation
Architecture defines long-term capability.
Implementation serves architecture.
When implementation conflicts with architecture,
architecture prevails.

### LAW II — Correctness Before Automation
Automation has value only when it improves measurable
correctness. Automation without correctness is failure.

### LAW III — Evidence Before Assumption
Every conclusion must be supported by independently
verifiable evidence. Unknown is preferable to
unsupported certainty.

### LAW IV — Calibration Before Confidence
Confidence estimates must reflect empirical correctness.
Confidence that cannot be calibrated is unreliable.

### LAW V — Independent Evidence Dominates
Multiple independent sources provide stronger evidence
than repeated observations from a single source.
Correlation is never mistaken for independence.

### LAW VI — Reversible Actions First
The least irreversible action shall always be preferred.
Permanent actions require exceptional evidence and
exceptional confidence.

### LAW VII — Measurable Improvement
No architectural change enters production unless it
demonstrates measurable improvement through reproducible
evaluation. Claims without evidence are not improvements.

### LAW VIII — Evolution Without Disruption
Production systems evolve through extension, composition,
and versioning. Replacement is permitted only when it
provides demonstrably superior long-term architecture
and is explicitly approved.

### LAW IX — Complete Explainability
Every decision must remain:
- explainable
- reproducible
- auditable
- traceable
- challengeable
- reviewable

A decision that cannot be explained cannot be trusted.

### LAW X — Provider Independence
No external dependency shall become indispensable.
Models, providers, databases, frameworks, languages,
cloud vendors, and infrastructure must remain
replaceable through stable interfaces.
Vendor lock-in is an architectural defect.

### LAW XI — Future Engineer Principle
Every subsystem shall remain understandable by
competent engineers years after its original
implementation. Maintainability is a first-class
architectural requirement.

### LAW XII — Trust Above Intelligence
The purpose of ISIL is not to appear intelligent.
The purpose of ISIL is to behave predictably,
correctly, transparently, and consistently.
Trust is earned through engineering discipline —
not claims of intelligence.

## Engineering Oath

### We Shall
- protect correctness before convenience
- protect users before metrics
- protect evidence before assumptions
- protect architecture before implementation
- protect maintainability before complexity
- protect transparency before automation
- protect privacy before unnecessary data collection
- protect reproducibility before optimization
- protect long-term trust before short-term performance

### We Shall Never
- manipulate confidence
- suppress uncertainty
- fabricate explanations
- sacrifice safety for speed
- sacrifice correctness for convenience
- introduce unnecessary complexity
- create avoidable vendor lock-in
- deploy changes whose benefits cannot be demonstrated

## Engineering Responsibility

Before every implementation ask:
1. Does this improve correctness?
2. Does this preserve existing architecture?
3. Can this be measured?
4. Can this be tested?
5. Can this be explained?
6. Can this be audited?
7. Can this be reversed if necessary?
8. Can another engineer understand it one year from now?

If any answer is No, stop and redesign.

## Provider Independence

ISIL shall remain independent from:
- AI model vendors
- cloud providers
- programming languages
- databases
- frameworks
- operating systems

Every dependency must be replaceable through
stable interfaces.

## Future Compatibility

Models will change.
Languages will change.
Frameworks will change.
Threats will evolve.
Policies will evolve.
Regulations will evolve.

The architecture must remain correct through all of them.

## Final Commitment

Every contribution must leave ISIL:
- more trustworthy and correct
- more explainable and observable
- more maintainable and secure
- more privacy-preserving and resilient
- more scalable

Never merely larger.
Never merely more complex.
Never merely more automated.

ISIL is being built to become the most trustworthy
trust infrastructure — not the largest.

Architecture shall always outlive implementation.
Trust shall always outlive technology.
