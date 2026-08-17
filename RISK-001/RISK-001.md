RISK-001 — Step 1
Risk Assessment Framework — Metadata, Purpose, Scope & Dependencies
Document Metadata
Document ID
RISK-001

Document Name
Risk Assessment Framework

Document Type
Engineering Specification

Tier
Tier 0 (Foundational Governance)

Status
Draft

Architecture Stage
Architecture Candidate v1.0

Version
1.0.0

Owner
ISIL Core Architecture

Review Standard
REVIEW-000

Registry
SPEC-000

Constitution
CASG-001

Canonical Terminology
CORE-000

Purpose
RISK-001 defines the canonical framework for identifying, evaluating, classifying, mitigating, and monitoring risk throughout ISIL.
Its purpose is to provide a consistent and deterministic method for understanding risk before and during system operations.
Risk assessment informs governance and operational decisions but does not independently create authority.

Scope
RISK-001 defines:
Risk Object architecture
Risk identification
Risk classification
Risk assessment
Risk scoring
Risk thresholds
Risk mitigation
Risk acceptance
Risk escalation
Risk monitoring
Risk lifecycle
Risk reporting

Out of Scope
RISK-001 does not define:
Constitutional Rules — RULE-001
Policy management — POLICY-001
Permission authorization — PERM-001
Identity management — IDENTITY-001
Autonomous planning — PLANNING-001
Runtime execution — EXEC-001
Safety controls — SAFETY-001
Those capabilities remain owned by their respective specifications.

Dependencies
Mandatory dependencies:
CASG-001
DOC-000
SPEC-000
REVIEW-000
CORE-000
RULE-001
POLICY-001
PERM-001
IDENTITY-001

Produced Concepts
RISK-001 becomes the canonical owner of:
Risk
Risk Object
Risk Event
Risk Level
Risk Score
Risk Threshold
Risk Factor
Risk Assessment
Risk Mitigation
Risk Acceptance
Risk Escalation
Residual Risk
These concepts shall subsequently be registered in CORE-000.

Consumers
Expected consumers include:
EXEC-001
DECISION-001
TRUST-001
SAFETY-001
AUTO-001
TOOL-001
GOVERNANCE-001
COMPLIANCE-001
RECOVERY-001

Foundational Principle
RISK-001 answers:
What could go wrong, how significant could the consequence be, how likely is it to occur, and what controls are required?

Risk Authority Boundary
Risk assessment may:
Identify risk.
Classify risk.
Recommend mitigation.
Trigger escalation.
Restrict operation when explicitly required by a higher-level Policy or Constitutional Rule.
Risk assessment shall not independently create authorization authority.

Constitutional Rule
ISIL shall identify and evaluate material risks before permitting risk-sensitive operations. Risk assessments shall be explicit, traceable, and subordinate to Constitutional Rules and Policies. Risk information shall never be converted into authority without an explicit governing mechanism.
RISK-001 — Step 2
Canonical Risk Object & Assessment Model
This section defines the canonical representation of risk used throughout ISIL.
A Risk represents a potential adverse outcome that may affect an entity, resource, operation, objective, or system.

Canonical Risk Object
Every Risk Object shall contain:
Field
Description
Risk ID
Permanent unique identifier
Risk Name
Canonical risk name
Risk Category
Primary risk classification
Target
Entity, resource, operation, or objective affected
Risk Factors
Conditions contributing to risk
Likelihood
Estimated probability of occurrence
Impact
Potential consequence magnitude
Risk Score
Derived risk measurement
Risk Level
Classified severity
Controls
Existing protective measures
Mitigations
Proposed or active responses
Owner
Responsible authority
Status
Current lifecycle state
Version
Risk model version
Created At
Creation timestamp
Updated At
Last modification timestamp


Risk Categories
Canonical categories include:
Security Risk
Operational Risk
Safety Risk
Privacy Risk
Integrity Risk
Reliability Risk
Compliance Risk
Governance Risk
Financial Risk
Strategic Risk
Additional categories require architectural approval.

Risk Factors
Risk Factors represent conditions that influence the likelihood or impact of a Risk.
Examples:
Threat exposure
System vulnerability
Uncertainty
Dependency failure
Resource limitation
Human error
Model uncertainty
Environmental conditions
Risk Factors shall be explicitly recorded where material.

Likelihood
Likelihood represents the estimated probability that a Risk Event will occur.
Canonical scale:
Level
Meaning
1
Rare
2
Unlikely
3
Possible
4
Likely
5
Almost Certain

Likelihood assessments shall include sufficient evidence or rationale to support the assigned level.

Impact
Impact represents the magnitude of potential consequences.
Canonical scale:
Level
Meaning
1
Negligible
2
Minor
3
Moderate
4
Major
5
Severe

Impact shall consider relevant consequences to:
People
Systems
Data
Operations
Security
Governance
Objectives

Risk Score
The baseline Risk Score shall be:
R=L×I
where:
R = Risk Score
L = Likelihood
I = Impact
The resulting score ranges from 1–25.

Risk Levels
Score
Level
1–4
Low
5–9
Moderate
10–16
High
17–25
Critical

These thresholds are the baseline classification model and may be refined through approved Policy.

Inherent Risk
Inherent Risk represents risk before considering mitigating controls.
It shall be calculated using the baseline likelihood and impact assessment.

Residual Risk
Residual Risk represents the remaining risk after applicable controls and mitigations are considered.
Residual Risk shall never be assumed to be zero merely because controls exist.

Assessment Structure
Each Risk Assessment shall contain:
Risk
↓
Risk Factors
↓
Likelihood Assessment
↓
Impact Assessment
↓
Inherent Risk
↓
Controls / Mitigations
↓
Residual Risk
↓
Risk Level
↓
Required Action

Determinism
For the same:
Risk Factors
Likelihood
Impact
Assessment Model Version
the same Risk Score and baseline Risk Level shall be produced.

Constitutional Rule
Every material Risk shall be represented explicitly with identifiable factors, likelihood, impact, score, controls, and residual risk. Risk classification shall use a documented and deterministic assessment model.
RISK-001 — Step 3
Risk Lifecycle, Mitigation, Acceptance, Escalation & Monitoring
Canonical Risk Lifecycle
Identified
↓
Assessed
↓
Classified
↓
Mitigation Planned
↓
Mitigated / Accepted
↓
Monitored
↓
Closed / Retired
A Risk shall not be considered closed without an explicit closure decision.

Lifecycle States
Identified
A potential Risk has been recorded but not fully assessed.
Assessed
Likelihood, impact, and relevant factors have been evaluated.
Classified
The Risk has received a formal Risk Score and Risk Level.
Mitigation Planned
Required controls or mitigations have been defined.
Mitigated
Controls have reduced the Risk to an acceptable residual level.
Accepted
An authorized authority has explicitly accepted the remaining Risk.
Monitored
The Risk remains active and is periodically reassessed.
Closed
The Risk is no longer materially applicable and has been formally closed.
Retired
Historical Risk information is preserved but no longer actively assessed.

Risk Mitigation
Mitigation may include:
Reducing likelihood.
Reducing impact.
Increasing detection.
Adding safeguards.
Restricting operation.
Removing the risky activity.
Adding human oversight.
Adding recovery mechanisms.
Every mitigation shall identify:
Responsible owner
Target Risk
Required action
Expected effect
Status
Review date

Risk Acceptance
Residual Risk may only be accepted by an explicitly authorized authority.
Risk acceptance shall record:
Risk ID
Residual Risk
Accepting authority
Acceptance reason
Acceptance date
Expiration/review date
Risk assessment itself does not grant acceptance authority.

Risk Escalation
Escalation shall occur when:
Risk reaches a Critical level.
Risk exceeds an approved threshold.
Required mitigation is unavailable.
Risk cannot be reliably evaluated.
Risk affects protected or safety-sensitive operations.
Conflicting assessments cannot be resolved.
Escalation shall produce an auditable escalation record.

Risk Monitoring
Active Risks shall be monitored according to their Risk Level.
Higher-risk items require more frequent reassessment.
Monitoring may consider:
New Risk Factors
Incident history
Control effectiveness
Environmental changes
System changes
Model changes
Policy changes
A significant change shall trigger reassessment.

Risk Thresholds
Baseline thresholds:
LOW        → Routine monitoring
MODERATE   → Managed mitigation
HIGH       → Active mitigation + escalation review
CRITICAL   → Immediate escalation and controlled response
Threshold behavior may be strengthened by POLICY-001.

Control Effectiveness
Controls shall be evaluated for:
Existence
Correct implementation
Effectiveness
Coverage
Failure conditions
A control shall not automatically be considered effective merely because it exists.

Risk Reassessment
Reassessment is mandatory when material changes occur to:
System architecture
Threat environment
Identity
Permissions
Policies
Operating context
Risk controls
Previous assessments shall remain historically preserved.

Risk Closure
A Risk may be closed only when:
The triggering condition no longer exists, or
The risky activity has been removed, or
The Risk has been formally superseded by an approved replacement assessment.
Closure shall preserve the complete historical record.

Constitutional Rule
Material Risks shall remain visible throughout their lifecycle. High and Critical Risks shall receive proportionate mitigation and escalation, while residual Risk may be accepted only by explicitly authorized governance.
RISK-001 — Step 4
Risk Evaluation Engine & Internal Architecture
This section defines the logical components responsible for identifying, assessing, classifying, mitigating, and monitoring Risk.

Architectural Principles
The Risk Framework shall be:
Deterministic
Evidence-based
Auditable
Version-aware
Fault-isolated
Technology-independent
Proportionate to Risk severity
Risk evaluation shall not silently alter governance authority.

Core Components
1. Risk Repository
   Maintains:
   Risk Objects
   Risk Assessments
   Risk versions
   Lifecycle state
   Historical records
   It is the authoritative source for registered Risks.

2. Risk Assessment Engine
   Processes:
   Risk Factors
   Likelihood
   Impact
   Assessment Model Version
   It produces:
   Risk Score
   Risk Level
   Assessment Evidence

3. Control Evaluator
   Evaluates the effectiveness and applicability of:
   Existing controls
   Mitigations
   Safeguards
   Operational restrictions
   It contributes to the Residual Risk assessment.

4. Threshold Engine
   Compares Risk Levels against approved thresholds.
   It identifies when:
   Routine monitoring is sufficient.
   Mitigation is required.
   Escalation is required.
   Immediate controlled response is required.

5. Mitigation Manager
   Maintains:
   Mitigation plans
   Responsible owners
   Mitigation status
   Expected effects
   Review dates
   It does not independently authorize mitigation actions outside approved governance.

6. Escalation Manager
   Responsible for:
   Detecting escalation conditions.
   Creating escalation records.
   Routing Risks to authorized authorities.
   Tracking escalation status.
   It shall never convert an escalation into an authorization decision.

7. Risk Monitoring Service
   Tracks active Risks and detects material changes requiring reassessment.
   Monitoring inputs may include:
   System changes
   Incidents
   Threat changes
   Control failures
   Policy changes
   Environmental changes

8. Audit Interface
   Records:
   Risk creation
   Assessments
   Score changes
   Mitigations
   Acceptance
   Escalations
   Reassessments
   Closure
   Every material Risk operation shall have an audit reference.

Component Flow
Risk / Assessment Request
│
▼
Risk Repository
│
▼
Assessment Engine
│
▼
Control Evaluator
│
▼
Threshold Engine
│       │
│       └────────► Escalation Manager
│
▼
Mitigation Manager
│
▼
Risk Monitoring Service
│
▼
Audit Interface

Component Boundaries
Component
Must Not Do
Risk Repository
Evaluate or approve Risk
Assessment Engine
Grant authorization
Control Evaluator
Invent controls
Threshold Engine
Override Constitutional Rules
Mitigation Manager
Self-authorize restricted actions
Escalation Manager
Convert escalation into approval
Monitoring Service
Modify historical assessments
Audit Interface
Alter Risk outcomes


Failure Isolation
If a required Risk component cannot provide trustworthy information:
The Risk assessment shall not be treated as complete.
The failure shall be recorded.
Risk-sensitive operations shall follow applicable Policy-defined fail-safe behavior.
No Risk result shall be silently fabricated.

Deterministic Evaluation
For identical:
Risk Object
Assessment inputs
Control state
Threshold configuration
Assessment Model Version
the Risk Assessment Engine shall produce the same baseline result.

Constitutional Rule
Risk evaluation shall be performed through separated, auditable components. No Risk component may independently create authorization, override Constitutional Rules, or conceal an unresolved Risk.
RISK-001 — Step 5
External Interfaces, Risk APIs, Events & Integration Contracts
This section defines how downstream ISIL systems consume Risk information.

Integration Principles
Risk interfaces shall be:
Explicit
Authenticated
Versioned
Deterministic
Auditable
Fail-safe
Technology-independent
Undocumented Risk integration paths are prohibited.

Canonical Operations
1. Create Risk
   Input:
   Risk Object
   Output:
   Risk ID
   Risk Status
   Audit Reference

2. Assess Risk
   Input:
   Risk ID
   Assessment Inputs
   Assessment Model Version
   Output:
   Likelihood
   Impact
   Risk Score
   Risk Level
   Assessment Evidence
   Audit Reference

3. Reassess Risk
   Input:
   Risk ID
   Updated Factors
   Updated Controls
   Output:
   Updated Risk Assessment
   Residual Risk
   New Risk Level
   Audit Reference

4. Retrieve Risk
   Input:
   Risk ID
   Requested Version
   Output:
   Risk Object
   Current Assessment
   Lifecycle Status

5. Escalate Risk
   Input:
   Risk ID
   Escalation Reason
   Output:
   Escalation ID
   Escalation Status
   Audit Reference

6. Close Risk
   Input:
   Risk ID
   Closure Reason
   Output:
   Closure Status
   Audit Reference

Canonical Risk Response
A Risk assessment response shall contain:
Field
Description
Request ID
Operation identifier
Risk ID
Canonical Risk
Likelihood
Current likelihood
Impact
Current impact
Risk Score
Calculated score
Risk Level
Current classification
Inherent Risk
Risk before controls
Residual Risk
Risk after controls
Assessment Version
Model version
Timestamp
Assessment time
Audit Reference
Associated audit record


Canonical Events
RISK-001 defines:
Risk Created
Risk Updated
Risk Assessed
Risk Reassessed
Risk Level Changed
Mitigation Created
Mitigation Updated
Mitigation Completed
Risk Accepted
Risk Escalated
Risk Monitoring Started
Risk Monitoring Triggered
Risk Closed
Risk Retired
Risk Assessment Failed
Events shall be immutable after publication.

Error Model
Every Risk operation failure shall include:
Error ID
Error Category
Severity
Source Component
Description
Timestamp
Recovery Guidance
Audit Reference

Canonical Error Categories
Invalid Risk Object
Risk Not Found
Invalid Assessment
Invalid Risk Factor
Invalid Threshold
Control Evaluation Failure
Mitigation Failure
Escalation Failure
Repository Failure
Security Failure
Assessment Engine Failure

Consumer Responsibilities
Consumers shall:
Use canonical Risk IDs.
Respect Risk Level semantics.
Preserve assessment versions.
Preserve audit references.
Trigger reassessment when required.
Never modify Risk results outside approved interfaces.
Consumers shall not treat Risk information as authorization unless explicitly required by RULE-001 or POLICY-001.

Integration With Other Tier 0 Systems
RULE-001
Defines Constitutional constraints governing Risk behavior.
POLICY-001
Defines operational policies that may establish Risk thresholds or required responses.
PERM-001
Controls authorization to perform Risk-related administrative actions.
IDENTITY-001
Provides authoritative identities for Risk owners, assessors, and actors.

Version Compatibility
Risk interfaces shall follow Semantic Versioning.
Breaking changes require:
Major version increment
Architecture review
SPEC-000 update
Migration guidance
Backward-compatible changes use Minor versions.

Constitutional Rule
Risk information shall be exchanged through canonical, versioned, and auditable interfaces. Downstream systems may consume Risk results but shall not redefine or silently alter the canonical Risk assessment.
