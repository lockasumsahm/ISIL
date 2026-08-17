001.029 Purpose
CONTAINMENT-001 defines the architecture for limiting the scope, propagation, persistence, and impact of an incident.
Core principle:
DETECT
↓
ASSESS
↓
CONTAIN
↓
LIMIT BLAST RADIUS
↓
PRESERVE SAFE OPERATION
↓
INVESTIGATE
↓
RECOVER
↓
RELEASE
Containment is therefore not destruction.
Its purpose is to create a controlled boundary around an unsafe or compromised condition.

001.030 Containment Objectives
1. STOP PROPAGATION
2. LIMIT BLAST RADIUS
3. PROTECT TRUSTED COMPONENTS
4. PRESERVE EVIDENCE
5. MAINTAIN SAFE SERVICES
6. ENABLE INVESTIGATION
7. ENABLE RECOVERY
8. CONTROL RELEASE

001.031 Containment Boundary
INCIDENT
│
┌─────────┴─────────┐
│   CONTAINMENT     │
│      BOUNDARY     │
└─────────┬─────────┘
│
┌───────────┼───────────┐
↓           ↓           ↓
QUARANTINE  RESTRICT    ISOLATE
│           │           │
└───────────┼───────────┘
↓
SAFE SYSTEM CORE
The boundary should be as narrow as reasonably possible.

001.032 Containment ≠ Shutdown
A containment action may restrict only the affected component.
COMPONENT-A  ← INCIDENT
COMPONENT-B  ← SAFE
COMPONENT-C  ← SAFE
COMPONENT-D  ← SAFE
Preferred:
ISOLATE A
KEEP B/C/D OPERATING
rather than:
SHUT DOWN EVERYTHING
unless broader shutdown is necessary.

001.033 Blast Radius
Blast radius represents the set of entities potentially affected by an incident.
DIRECTLY AFFECTED
↓
DEPENDENCIES
↓
DEPENDENTS
↓
CONNECTED SYSTEMS
↓
POTENTIAL PROPAGATION

001.034 Blast-Radius Graph
A
/ | \
B  C  D
/ \    |
E   F   G
If A is compromised, containment must evaluate:
A → B
A → C
A → D
B → E
B → F
D → G
Containment should not assume that only A is relevant.

001.035 Containment Scope
A containment scope should identify:
COMPONENTS
IDENTITIES
CAPABILITIES
TOOLS
DATA
NETWORK PATHS
PROCESSES
SESSIONS
TASKS
PLANS
DEPENDENCIES

001.036 Containment Record
ContainmentRecord
{
containment_id

    incident_id
    threat_id

    trigger
    confidence
    severity

    affected_scope
    containment_scope

    actions
    restrictions

    preserved_resources
    blocked_resources

    start_time
    current_state

    release_conditions
}

001.037 Containment States
NORMAL
↓
SUSPECTED
↓
CONTAINMENT_PENDING
↓
CONTAINED
↓
INVESTIGATING
↓
CLEARED
↓
RELEASE_PENDING
↓
RELEASED
Critical path:
SUSPECTED
↓
CRITICAL
↓
EMERGENCY_CONTAINMENT

001.038 Containment Modes
OBSERVATIONAL
RESTRICTIVE
ISOLATION
QUARANTINE
EMERGENCY
Observational
Monitor without materially changing operation.
Restrictive
Reduce capabilities or access.
Isolation
Separate the affected component from selected dependencies.
Quarantine
Place the component into a controlled environment.
Emergency
Immediately prevent propagation when delay creates unacceptable risk.

001.039 Containment Decision
CONTAIN(signal):

    determine confidence

    determine severity

    identify affected component

    identify propagation paths

    calculate potential blast radius

    identify safe containment boundary

    preserve critical evidence

    select minimum effective containment

    verify containment capability

    execute containment

    verify resulting boundary

    monitor containment integrity

001.040 Minimum Effective Containment
The system should choose:
SMALLEST CONTAINMENT SCOPE
THAT
SUFFICIENTLY REDUCES
UNACCEPTABLE RISK
Example:
COMPONENT-A
├── read capability
├── write capability
└── network capability
If only network behavior is compromised:
BLOCK NETWORK
KEEP SAFE LOCAL OPERATIONS
rather than disabling all capabilities.

001.041 Compartmentalization
The architecture should divide sensitive operations into independent compartments.
┌──────────┐   ┌──────────┐
│ DOMAIN A │   │ DOMAIN B │
└──────────┘   └──────────┘
│              │
└──────┬───────┘
│
CONTROLLED GATE
A compromise in A should not automatically compromise B.

001.042 Trust Compartments
Components should not automatically inherit trust from neighboring components.
COMPARTMENT-A
trust(A)

COMPARTMENT-B
trust(B)

A compromise
≠
B compromise
Cross-compartment access requires explicit control.

001.043 Capability Compartmentalization
Capabilities should be partitioned.
COMPARTMENT-A
├── READ
└── ANALYZE

COMPARTMENT-B
├── MODIFY
└── WRITE

COMPARTMENT-C
└── EXTERNAL ACTION
A compromised analytical capability should not automatically obtain modification authority.

001.044 Data Compartmentalization
Data should be separated by:
sensitivity
purpose
tenant
environment
authorization domain
retention requirement
A containment event should be able to isolate a specific data domain without necessarily disabling unrelated data.

001.045 Identity Containment
A compromised identity may be:
ACTIVE
↓
SUSPECTED
↓
RESTRICTED
↓
QUARANTINED
Identity containment should be coordinated with IDENTITY-001 and PERM-001.

001.046 Session Containment
A suspicious session may be isolated independently.
IDENTITY
│
├── SESSION-A ← suspicious
├── SESSION-B ← safe
└── SESSION-C ← safe
Preferred:
CONTAIN SESSION-A
rather than automatically disabling the entire identity.

001.047 Tool Containment
A tool may be restricted at:
TOOL LEVEL
CAPABILITY LEVEL
INVOCATION LEVEL
INSTANCE LEVEL
DEPENDENCY LEVEL
Example:
TOOL-X
├── instance-1 ← contained
├── instance-2 ← safe
└── instance-3 ← safe

001.048 Model Containment
A suspicious model may be:
removed from production inference
↓
retained for forensic analysis
↓
isolated from update pipeline
The model artifact should not automatically be destroyed because evidence may be required.

001.049 Memory Containment
Memory systems may contain compromised or unverified information.
Containment may therefore mark:
MEMORY ENTRY
↓
QUARANTINED
↓
NOT AVAILABLE TO NORMAL RETRIEVAL
until validation is complete.
This is particularly important for preventing a corrupted memory entry from influencing future planning or decisions.

001.050 Memory Trust Boundary
QUARANTINED MEMORY
↓
VALIDATION
↓
┌───────────────┐
│ TRUSTED       │ → restore
│ REJECTED      │ → isolate
│ UNKNOWN       │ → retain quarantine
└───────────────┘

001.051 Plan Containment
If a threat affects an active plan:
PLAN
├── TASK-A ✓
├── TASK-B ✓
├── TASK-C ← affected
└── TASK-D pending
The system should isolate the affected branch rather than automatically invalidate every safe task.

001.052 Objective Protection
Containment must not silently change the objective.
OBJECTIVE
↓
CONTAINMENT
↓
SAFE EXECUTION BOUNDARY
The objective remains unchanged unless OBJECTIVE-001 or authorized governance explicitly changes it.

001.053 Dependency Isolation
If:
A → B → C
and B becomes compromised:
A
│
X
│
B ← QUARANTINED
│
X
│
C
The architecture should prevent B from continuing to propagate effects through A or C.

001.054 Propagation Control
Containment must identify propagation channels:
NETWORK
DATA
IDENTITY
CREDENTIALS
TOOLS
MODELS
MEMORY
SHARED STORAGE
DEPENDENCIES
AUTOMATED TASKS
Each channel should be evaluated independently.

001.055 Propagation Gate
CONTAINED COMPONENT
↓
PROPAGATION GATE
↓
ALLOW / BLOCK
No containment state is useful if the affected component can freely communicate through an uncontrolled channel.

001.056 Network Containment
Network containment may include:
destination blocking
connection termination
segmentation
rate limiting
protocol restriction
egress restriction
ingress restriction
Detailed network security architecture belongs to the later NETWORK-001.

001.057 Credential Containment
If a credential is suspected compromised:
CREDENTIAL
↓
RESTRICT
↓
REVOKE / ROTATE
↓
REVALIDATE DEPENDENCIES
Containment must account for services that may still possess the old credential.

001.058 Secret Propagation
Secrets may propagate through:
logs
memory
tool inputs
tool outputs
files
network requests
caches
Containment should identify and limit these propagation paths.

001.059 Quarantine
Quarantine creates a controlled environment:
SUSPICIOUS COMPONENT
↓
QUARANTINE
↓
┌─────────────────────────┐
│ LIMITED RESOURCES       │
│ LIMITED NETWORK         │
│ LIMITED DATA            │
│ NO UNCONTROLLED EFFECTS │
└─────────────────────────┘

001.060 Quarantine Requirements
A quarantine environment should define:
allowed inputs
allowed outputs
resource limits
network policy
data visibility
execution duration
monitoring
evidence preservation
release conditions

001.061 Quarantine ≠ Sandbox
They overlap but serve different purposes.
QUARANTINE
=
response to a suspicious/affected component

SANDBOX
=
controlled environment for executing untrusted or experimental code
Detailed sandbox architecture belongs to SANDBOX-001.

001.062 Containment Integrity
A containment boundary must itself be monitored.
CONTAINED
↓
BOUNDARY MONITOR
↓
boundary intact?
├── YES → continue
└── NO  → escalate containment

001.063 Containment Escape
A containment escape occurs when:
CONTAINED COMPONENT
↓
CROSSES CONTROLLED BOUNDARY
↓
UNAUTHORIZED SCOPE
This is a critical defensive event.

001.064 Escape Response
ESCAPE DETECTED
↓
STOP PROPAGATION
↓
EXPAND CONTAINMENT
↓
PROTECT TRUSTED COMPONENTS
↓
PRESERVE EVIDENCE
↓
ESCALATE

001.065 Containment Expansion
Containment may need to expand when evidence indicates wider compromise.
BOUNDARY-A
↓
NEW EVIDENCE
↓
AFFECTED B
↓
EXPAND BOUNDARY
↓
BOUNDARY-A+B
Expansion must remain evidence-driven.

001.066 Containment Contraction
If investigation shows that part of the original boundary is safe:
BROAD CONTAINMENT
↓
VALIDATED SAFE REGION
↓
CONTAINMENT CONTRACTS
↓
SERVICE RESTORED
This prevents unnecessarily prolonged disruption.

001.067 Safe Service Preservation
During containment:
CRITICAL SAFE SERVICE
↓
PRESERVE
The architecture should identify essential operations that can continue independently.

001.068 Criticality Classification
Components may be classified:
CRITICAL
HIGH
NORMAL
LOW
Containment strategy should account for service criticality.

001.069 Containment Tradeoff
Containment has two competing risks:
UNDER-CONTAINMENT
↓
THREAT PROPAGATION

OVER-CONTAINMENT
↓
UNNECESSARY SERVICE DISRUPTION
The system must optimize for safe containment, not maximum shutdown.

001.070 Containment Priority
A conceptual priority ordering:
1. PREVENT IRREVERSIBLE HARM
2. STOP PROPAGATION
3. PROTECT CRITICAL TRUSTED SERVICES
4. PRESERVE EVIDENCE
5. MINIMIZE DISRUPTION
6. ENABLE INVESTIGATION
7. ENABLE RECOVERY

001.071 Incident Boundary
Each material containment event should receive an incident boundary.
IncidentBoundary
{
incident_id

    start_time

    affected_entities
    protected_entities

    contained_entities

    propagation_paths
    blocked_paths

    current_state
}

001.072 Containment Coordination
Containment interacts with:
DEFENSE-001
↓
CONTAINMENT-001
↓
├── TOOL-001
├── NETWORK-001
├── SANDBOX-001
├── KILLSWITCH-001
└── RECOVERY-001
Containment coordinates these layers; it does not replace them.

001.073 Containment + TOOL-001
TOOL-001 controls tool execution.
CONTAINMENT-001 can request:
restrict tool
isolate tool instance
block capability
quarantine provider
But the underlying authorization and execution mechanisms remain governed by TOOL-001.

001.074 Containment + NETWORK-001
Containment may request:
block destination
segment network
restrict route
limit communication
NETWORK-001 will define the actual network-control architecture.

001.075 Containment + SANDBOX-001
A suspicious component may be transferred into:
QUARANTINE
↓
SANDBOX
↓
CONTROLLED ANALYSIS
The two modules remain distinct.

001.076 Containment + KILLSWITCH-001
Containment should be attempted before total shutdown when feasible.
THREAT
↓
CONTAIN
↓
if insufficient
↓
KILLSWITCH
The killswitch remains the higher-impact emergency mechanism.

001.077 Evidence Preservation During Containment
Before destroying or resetting affected state where possible:
capture
↓
hash
↓
timestamp
↓
store securely
↓
contain
Evidence must remain associated with the incident.

001.078 Containment Audit
Every material containment action must record:
who/what initiated
why
what was contained
when
scope
authority
evidence
result
release conditions

001.079 Release Conditions
Containment cannot simply disappear because the system "looks fine."
Release requires explicit conditions.
THREAT ASSESSMENT COMPLETE
AND
BOUNDARY INTEGRITY CONFIRMED
AND
ROOT CONDITION ADDRESSED
AND
REQUIRED VALIDATION COMPLETE
AND
RELEASE AUTHORIZED

001.080 Controlled Release
QUARANTINED
↓
VALIDATION
↓
RELEASE REVIEW
↓
AUTHORIZED
↓
GRADUAL RELEASE
↓
MONITOR
↓
NORMAL

001.081 Graduated Release
Instead of:
QUARANTINE → FULL ACCESS
prefer:
QUARANTINE
↓
LIMITED ACCESS
↓
OBSERVED OPERATION
↓
EXPANDED ACCESS
↓
NORMAL

001.082 Release Failure
If suspicious behavior returns:
RELEASE
↓
NEW ANOMALY
↓
RECONTAIN
↓
REASSESS
The system must be capable of returning to containment.

001.083 Containment Expiration
Temporary containment should have explicit:
review_time
maximum_duration
renewal_condition
Expiration must not automatically equal release.
EXPIRATION
↓
REVIEW
↓
RELEASE / EXTEND / ESCALATE

001.084 Containment Failure
If containment cannot be established:
THREAT
↓
CONTAINMENT ATTEMPT
↓
FAIL
↓
ESCALATE
↓
BROADER CONTAINMENT / KILLSWITCH / OTHER RESPONSE
Failure must itself become a defensive signal.

001.085 Containment Verification
After containment:
ACTION EXECUTED
↓
VERIFY
├── boundary exists
├── propagation stopped
├── affected component restricted
├── trusted components protected
└── evidence preserved
A containment command returning "success" is not enough.

001.086 Containment Algorithm
CONTAIN_INCIDENT(incident):

    1. Identify incident.

    2. Validate incident evidence.

    3. Determine confidence.

    4. Determine severity.

    5. Identify affected entities.

    6. Map dependencies.

    7. Map propagation channels.

    8. Estimate blast radius.

    9. Identify critical trusted services.

10. Preserve relevant evidence.

11. Select minimum effective containment.

12. Validate required authority.

13. Execute containment.

14. Verify containment boundary.

15. Monitor boundary integrity.

16. Detect escape attempts.

17. Expand containment if evidence requires.

18. Contract containment when validated safe.

19. Investigate root condition.

20. Determine release conditions.

21. Obtain release authorization.

22. Gradually release.

23. Monitor post-release behavior.

24. Recontain if necessary.

25. Close incident only after verification.

26. Preserve complete provenance.

001.087 Core Containment Invariants
CON-INV-001
Containment limits impact; it does not redefine the objective.

CON-INV-002
Containment does not automatically imply total shutdown.

CON-INV-003
Containment scope must be explicitly defined.

CON-INV-004
Containment should prefer the minimum effective boundary.

CON-INV-005
Potential propagation paths must be evaluated.

CON-INV-006
Critical trusted services should be preserved where safely possible.

CON-INV-007
Containment boundaries must themselves be monitored.

CON-INV-008
Containment escape is a critical defensive event.

CON-INV-009
Containment may expand when evidence indicates wider compromise.

CON-INV-010
Containment may contract when affected regions are validated safe.

CON-INV-011
Quarantine must have explicit boundaries.

CON-INV-012
Quarantine is not equivalent to sandboxing.

CON-INV-013
Contained components cannot automatically regain previous authority.

CON-INV-014
Containment cannot bypass permission architecture.

CON-INV-015
Containment cannot silently modify objectives.

CON-INV-016
Evidence should be preserved before destructive remediation where possible.

CON-INV-017
Material containment actions are auditable.

CON-INV-018
Containment failure must become an observable event.

CON-INV-019
Release requires explicit validation.

CON-INV-020
Containment expiration does not automatically authorize release.

CON-INV-021
Release should be graduated where feasible.

CON-INV-022
Released components remain monitored.

CON-INV-023
Post-release anomalies can trigger recontainment.

CON-INV-024
Containment must remain compatible with recovery.

CON-INV-025
Containment state must survive system restarts where the incident remains active.

CON-INV-026
Containment provenance must remain reconstructable.

CON-INV-027
Containment must prevent uncontrolled propagation.

CON-INV-028
Containment must minimize unnecessary operational disruption.

CON-INV-029
Containment decisions must remain proportional to evidence and impact.

CON-INV-030
No containment mechanism is assumed infallible.

001.088 Final CONTAINMENT-001 Architecture
CONTAINMENT-001
│
├── INCIDENT IDENTIFICATION
│
├── THREAT / IMPACT ASSESSMENT
│
├── SCOPE MAPPING
│   ├── components
│   ├── identities
│   ├── tools
│   ├── data
│   ├── models
│   ├── tasks
│   └── dependencies
│
├── PROPAGATION ANALYSIS
│   ├── network
│   ├── data
│   ├── identity
│   ├── credentials
│   └── dependencies
│
├── CONTAINMENT
│   ├── restriction
│   ├── isolation
│   ├── quarantine
│   └── emergency containment
│
├── BOUNDARY CONTROL
│   ├── boundary verification
│   ├── escape detection
│   ├── expansion
│   └── contraction
│
├── SAFE OPERATION
│   ├── critical-service preservation
│   └── minimized disruption
│
├── INVESTIGATION
│   ├── evidence preservation
│   ├── root analysis
│   └── incident tracking
│
└── RELEASE
├── validation
├── authorization
├── graduated release
├── post-release monitoring
└── recontainment

