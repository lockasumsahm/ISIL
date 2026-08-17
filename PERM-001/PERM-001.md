PERM-001 — Step 1
Document Metadata
Document ID
PERM-001


Document Name
Permission & Authorization Framework


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
PERM-001 defines the canonical Permission & Authorization Framework used throughout the ISIL ecosystem.
Its purpose is to determine what actions an identity, agent, service, or system is authorized to perform after Constitutional Rules (RULE-001) and applicable Policies (POLICY-001) have been successfully evaluated.
Permissions define granted capabilities—they do not create new authority.

Scope
PERM-001 defines:
Permission Object architecture
Permission assignment
Authorization model
Permission inheritance
Permission evaluation
Permission lifecycle
Permission hierarchy
Permission versioning
Authorization contracts
Runtime authorization behavior

Out of Scope
PERM-001 does not define:
Constitutional Rules (RULE-001)
Policy evaluation (POLICY-001)
Identity management (IDENTITY-001)
Risk scoring (RISK-001)
Runtime execution
AI decision making
These are specified in their respective engineering documents.

Dependencies
Mandatory dependencies:
CASG-001
DOC-000
SPEC-000
REVIEW-000
CORE-000
RULE-001
POLICY-001
PERM-001 shall not introduce concepts outside these dependencies.

Produced Concepts
PERM-001 becomes the canonical owner of:
Permission
Authorization
Permission Set
Permission Scope
Permission Assignment
Permission Grant
Permission Revocation
Authorization Decision
Permission Repository
Effective Permission Set
These concepts shall later be registered in CORE-000.

Consumers
Expected downstream consumers include:
EXEC-001
DECISION-001
RUNTIME-001
AUTO-001
TOOL-001
TRUST-001
DEFENSE-001
GOVERNANCE-001

Constitutional Rule
Permissions shall grant only capabilities that remain fully consistent with Constitutional Rules and applicable Policies. No Permission may authorize an action prohibited by RULE-001 or restricted by POLICY-001.

Status
Document Status
Draft


Engineering Readiness
Structure Creation


Review
Pending
PERM-001 — Step 2
Permission Architecture & Canonical Permission Object
This section defines the canonical Permission architecture used throughout ISIL.
A Permission represents an explicitly authorized capability that may be exercised by an Identity, Agent, Service, or System only after successful Constitutional Rule and Policy evaluation.
Permissions define allowed capabilities, not governance authority.

Engineering Objectives
The Permission architecture shall:
Standardize authorization.
Support fine-grained access control.
Preserve deterministic authorization decisions.
Enable inheritance and grouping.
Support versioning.
Maintain auditability.
Prevent unauthorized privilege escalation.

Canonical Permission Object
Every Permission shall be represented by a canonical Permission Object.
Each Permission Object shall contain:
Field
Description
Permission ID
Globally unique identifier
Permission Name
Canonical permission name
Permission Version
Semantic version
Permission Category
Authorization domain
Permission Scope
Area where the permission applies
Owner
Responsible authority
Status
Lifecycle state
Priority
Evaluation precedence
Dependencies
Required Policies and Rules
Constitutional References
Referenced RULE-001 rules
Policy References
Required POLICY-001 policies
Metadata
Descriptive information


Mandatory Characteristics
Every Permission shall be:
Unique
Explicit
Immutable once approved
Version controlled
Auditable
Deterministic
Independently identifiable
Implicit permissions are prohibited.

Permission Identity
Every Permission receives one permanent Permission ID.
Example:
PERM-000001
The Permission ID never changes across revisions.

Permission Categories
Permissions shall belong to one primary category.
Examples include:
Read
Write
Execute
Modify
Delete
Approve
Administrative
Runtime Control
System Management
AI Capability
Additional categories require architectural approval.

Permission Scope
Every Permission shall explicitly define where it is valid.
Possible scopes include:
Global
Organization
Service
Agent
User
Resource
Session
Permissions without an explicit scope are invalid.

Authorization Authority
A Permission derives its authority from:
Constitutional Rules (RULE-001)
Applicable Policies (POLICY-001)
A Permission may:
Grant an allowed capability.
Restrict an allowed capability.
Define operational access.
A Permission shall never:
Override Constitutional Rules.
Override Policies.
Grant prohibited capabilities.

Permission Metadata
Metadata may include:
Description
Purpose
Author
Creation Date
Review Date
Tags
Documentation References
Metadata shall not affect authorization decisions.

Constitutional Rule
Every Permission within ISIL shall be represented as a canonical Permission Object with a unique identity, explicit scope, declared dependencies, and immutable constitutional and policy relationships. Permissions authorize capabilities but never create governance authority.

Engineering Summary
This section defines:
Canonical Permission Object
Mandatory fields
Permission identity
Categories
Scope
Authorization authority
Metadata
PERM-001 — Step 3
Permission Lifecycle, Assignment, Revocation & Versioning
This section defines how Permissions are created, assigned, activated, suspended, revoked, and retired.
Permission state changes shall be controlled, auditable, and deterministic.

Engineering Objectives
The Permission lifecycle shall:
Prevent unauthorized grants.
Support explicit assignment.
Enable immediate revocation.
Preserve historical records.
Prevent stale authorization.
Maintain version traceability.

Canonical Permission Lifecycle
Proposed
│
▼
Draft
│
▼
Engineering Review
│
▼
Approved
│
▼
Active
│
├──────────► Suspended
│                │
│                ▼
│             Active
│
▼
Revoked
│
▼
Archived
A Permission shall not become Active without completing the required approval process.

Lifecycle States
Proposed
Permission concept under consideration.
It has no authorization effect.
Draft
Permission is being defined.
It cannot be assigned or evaluated as active authorization.
Engineering Review
The Permission is validated against:
RULE-001
POLICY-001
CORE-000
REVIEW-000
Approved
The Permission has passed required review and is eligible for activation.
Active
The Permission may participate in authorization evaluation.
Suspended
The Permission is temporarily disabled.
Existing assignments remain recorded, but authorization shall fail while the Permission is suspended.
Revoked
The Permission is permanently withdrawn from authorization use.
Revocation shall take effect according to the authorization consistency requirements defined by the implementation.
Archived
The Permission is retained for historical traceability and cannot be newly assigned.

Permission Assignment
A Permission shall never become available merely because it exists.
It must be explicitly assigned to an authorized subject.
A Permission Assignment shall associate:
Subject
+
Permission
+
Scope
+
Assignment Constraints
The subject may be:
Human Identity
AI Agent
Service
System Component

Assignment Requirements
Every assignment shall:
Reference a valid Identity.
Reference an Active Permission.
Define applicable scope.
Respect Constitutional Rules.
Respect applicable Policies.
Be auditable.
Have a unique Assignment ID.

Revocation
A Permission shall be revocable independently of its original assignment.
Revocation may occur because of:
Security concerns.
Policy changes.
Identity changes.
Risk changes.
Administrative action.
Permission expiration.
System integrity failures.
Revoked permissions shall not be silently restored.

Suspension vs Revocation
Suspension is temporary.
Revocation is permanent unless a new authorization process creates a new valid assignment.
This distinction must remain explicit.

Versioning
Permissions use Semantic Versioning:
Major.Minor.Patch
Patch
Documentation or non-behavioral correction.
Minor
Backward-compatible authorization behavior.
Major
Breaking authorization semantics.
Major changes require architectural review.

Immutable History
The system shall preserve:
Permission versions.
Assignment history.
Activation history.
Suspension history.
Revocation history.
Approval records.
Historical records shall not be deleted.

Constitutional Rule
Authorization shall depend on explicit, valid, and currently Active Permission assignments. Permission lifecycle transitions shall be controlled and auditable, and revocation shall take precedence over previously granted authorization.

Engineering Summary
This section defines:
Permission lifecycle
Permission assignment
Assignment requirements
Suspension
Revocation
Versioning
Immutable history
PERM-001 — Step 4
Authorization Evaluation Model
This section defines how ISIL determines whether a subject is authorized to perform a requested action on a specified resource.
Authorization shall be deterministic and shall never grant authority that is prohibited by RULE-001 or POLICY-001.

Authorization Request
Every authorization evaluation shall use a canonical Authorization Request containing:
Field
Description
Request ID
Unique authorization request
Subject ID
Identity requesting access
Action
Requested operation
Resource ID
Target resource
Context
Relevant runtime information
Requested Scope
Scope of requested capability
Timestamp
Evaluation time


Authorization Evaluation Pipeline
Authorization Request
│
▼
Identity Validation
│
▼
RULE-001 Evaluation
│
▼
POLICY-001 Evaluation
│
▼
Permission Retrieval
│
▼
Scope Validation
│
▼
Assignment Validation
│
▼
Permission Matching
│
▼
Conflict Resolution
│
▼
Authorization Decision
No authorization decision may bypass the Constitutional Rule or Policy stages.

Permission Matching
A Permission matches an Authorization Request only when:
Subject is valid.
Permission is Active.
Assignment is valid.
Action is authorized.
Resource is within scope.
Required constraints are satisfied.
RULE-001 permits the action.
POLICY-001 permits the action.
A partial match is insufficient for authorization.

Deny Precedence
Authorization follows a strict deny-precedence model.
Constitutional Deny
↓
Policy Deny
↓
Permission Deny
↓
Authorization Grant
If any higher-level governance layer denies the request, authorization shall fail.
No lower-level Permission may override a higher-level denial.

Effective Permission Set
The engine shall compute an Effective Permission Set containing only permissions that are:
Active
Validly assigned
In scope
Constitutionally permitted
Policy-compliant
Applicable to the current request
The Effective Permission Set shall be immutable for the duration of the authorization evaluation.

Authorization Decision
The canonical decision shall be one of:
ALLOW
DENY
ESCALATE
ALLOW
All authorization requirements are satisfied.
DENY
At least one mandatory authorization requirement fails.
ESCALATE
The system cannot deterministically resolve the request under the defined authorization rules.
The system shall never convert uncertainty into an automatic ALLOW.

Decision Evidence
Every authorization decision shall contain sufficient evidence to explain:
Subject
Requested action
Resource
Applicable Permissions
Applicable Policies
Constitutional result
Final decision
Reason
Audit Reference
Sensitive information shall be protected according to applicable security requirements.

Determinism
For identical:
Subject
Resource
Action
Context
Active Permissions
Policy versions
Rule versions
the Authorization Engine shall produce the same decision.

Failure-Safe Behavior
If required authorization information cannot be reliably established, the default outcome shall be:
DENY
unless RULE-001 explicitly defines an approved escalation path.
Authorization infrastructure failures shall never silently become permission grants.

Constitutional Rule
ISIL shall authorize an action only when Constitutional Rules, applicable Policies, and explicit Permission assignments all permit that action. Any unresolved authorization state shall fail safely or escalate through an explicitly defined governance path.

Engineering Summary
This section defines:
Authorization Request
Evaluation pipeline
Permission matching
Deny precedence
Effective Permission Set
Authorization decisions
Decision evidence
Determinism
Fail-safe behavior
PERM-001 — Step 5
Internal Authorization Architecture & Component Model
This section defines the logical components responsible for processing authorization requests.
The architecture separates permission storage, assignment management, evaluation, decision generation, and audit functions.

Architectural Principles
The authorization subsystem shall be:
Deterministic
Modular
Auditable
Fail-safe
Version-aware
Horizontally scalable
Technology-independent
No component may silently assume authority belonging to another component.

Core Components
1. Permission Repository
   Maintains:
   Canonical Permission Objects
   Permission versions
   Lifecycle state
   Permission metadata
   Historical records
   It is the authoritative source for Permission definitions.

2. Assignment Manager
   Maintains:
   Permission assignments
   Assignment scope
   Assignment constraints
   Assignment lifecycle
   Revocation state
   It shall reject assignments referencing invalid or inactive Permissions.

3. Authorization Request Validator
   Validates:
   Request structure
   Subject identity
   Requested action
   Resource
   Context
   Required identifiers
   Invalid requests shall not proceed.

4. Governance Gateway
   Obtains and validates results from:
   RULE-001
   POLICY-001
   The Gateway ensures authorization cannot bypass higher-level governance.

5. Permission Matcher
   Determines which active Permission assignments apply to the request.
   Matching considers:
   Subject
   Action
   Resource
   Scope
   Constraints

6. Constraint Evaluator
   Evaluates authorization constraints attached to applicable Permissions.
   Examples include:
   Resource restrictions
   Time restrictions
   Context requirements
   Operational boundaries
   An unsatisfied mandatory constraint prevents authorization.

7. Decision Generator
   Produces the canonical:
   ALLOW
   DENY
   ESCALATE
   decision.
   It also generates decision evidence and reason information.

8. Audit Interface
   Records:
   Authorization requests
   Permission matches
   Governance results
   Decisions
   Failures
   Revocations
   Escalations
   Every authorization evaluation shall have an audit reference.

Component Flow
Authorization Request
│
▼
Request Validator
│
▼
Governance Gateway
│
▼
Permission Repository
│
▼
Assignment Manager
│
▼
Permission Matcher
│
▼
Constraint Evaluator
│
▼
Decision Generator
│
▼
Audit Interface

Separation of Responsibilities
The following separation is mandatory:
Component
Must Not Do
Permission Repository
Make authorization decisions
Assignment Manager
Modify Constitutional Rules
Governance Gateway
Create Permissions
Permission Matcher
Override Policy decisions
Constraint Evaluator
Grant missing Permissions
Decision Generator
Bypass governance results
Audit Interface
Modify authorization outcomes


Failure Isolation
A component failure shall not corrupt:
Permission definitions
Assignment records
Governance results
Authorization history
If a required component cannot provide trustworthy information, authorization shall fail safely or escalate.

Constitutional Rule
Authorization responsibilities shall be separated across independently defined components. No component may create, elevate, or bypass authority outside its declared responsibility.
PERM-001 — Step 6
External APIs, Integration Contracts, Events & Error Model
This section defines the canonical interfaces through which downstream ISIL components consume the Permission & Authorization Framework.

Integration Principles
All authorization interfaces shall be:
Explicit
Authenticated
Versioned
Deterministic
Auditable
Fail-safe
Technology-independent
Undocumented authorization paths are prohibited.

Canonical Operations
1. Evaluate Authorization
   Purpose: Determine whether a subject may perform an action.
   Input:
   Authorization Request
   Output:
   Authorization Decision
   Decision Evidence
   Audit Reference

2. Retrieve Permission
   Purpose: Retrieve a specific Permission definition.
   Input:
   Permission ID
   Requested version
   Output:
   Permission Object

3. Assign Permission
   Purpose: Create an explicit Permission Assignment.
   Input:
   Subject ID
   Permission ID
   Scope
   Constraints
   Output:
   Assignment ID
   Assignment Status
   Assignment shall succeed only when all governance requirements are satisfied.

4. Revoke Permission
   Purpose: Remove an active Permission Assignment.
   Input:
   Assignment ID
   Revocation reason
   Output:
   Revocation Status
   Audit Reference

5. Validate Permission
   Purpose: Validate a Permission before approval or activation.
   Input:
   Permission Object
   Output:
   Validation Result
   Validation Findings

Canonical Authorization Response
Every authorization evaluation shall return:
Field
Description
Request ID
Original request identifier
Decision
ALLOW / DENY / ESCALATE
Matched Permissions
Applicable permissions
Governance Result
RULE/POLICY result
Reason
Decision explanation
Effective Scope
Scope applied
Evaluation Version
Authorization engine version
Timestamp
Evaluation time
Audit Reference
Associated audit record


Events
PERM-001 defines the following canonical events:
Permission Created
Permission Updated
Permission Approved
Permission Activated
Permission Suspended
Permission Revoked
Permission Archived
Permission Assigned
Permission Assignment Revoked
Authorization Evaluation Started
Authorization Evaluation Completed
Authorization Evaluation Failed
Authorization Escalated
Events shall be immutable after publication.

Error Model
Every failure shall contain:
Error ID
Error Category
Severity
Source Component
Description
Timestamp
Recovery Guidance
Audit Reference

Canonical Error Categories
Invalid Authorization Request
Identity Validation Failure
Governance Denial
Permission Not Found
Permission Inactive
Invalid Assignment
Scope Violation
Constraint Failure
Authorization Conflict
Repository Failure
Security Failure
Internal Authorization Failure

Fail-Safe Integration
If a downstream component cannot reliably determine authorization state, it shall treat the result as:
DENY
unless an explicitly authorized escalation path exists.
No consumer may reinterpret an authorization failure as an authorization grant.

Version Compatibility
Interface changes shall follow Semantic Versioning.
Breaking changes require:
Major version increment
Architecture review
SPEC-000 update
Migration guidance
Backward-compatible changes use a Minor version.
Non-behavioral corrections use a Patch version.

Consumer Responsibilities
Consumers of PERM-001 shall:
Provide valid authorization requests.
Verify response integrity.
Respect ALLOW/DENY/ESCALATE semantics.
Never bypass PERM-001 for protected actions.
Preserve required audit references.

Constitutional Rule
All authorization-dependent systems shall consume PERM-001 through its canonical interfaces and shall preserve the meaning of its authorization decisions. Consumers shall never convert DENY or unresolved authorization states into ALLOW.

PERM-001 — Step 7
Security, Non-Functional Requirements, Testing & Completion
Non-Functional Requirements
PERM-001 shall provide:
Deterministic authorization.
Fail-safe behavior.
High availability.
Horizontal scalability.
Low evaluation latency.
Complete auditability.
Version traceability.
Fault isolation.
Performance improvements shall never change authorization semantics.

Security Requirements
The framework shall:
Authenticate authorization requests.
Protect Permission Objects from unauthorized modification.
Prevent unauthorized Permission assignment.
Prevent privilege escalation.
Protect assignment and revocation operations.
Validate all authorization inputs.
Preserve immutable authorization history.
Prevent consumers from bypassing authorization controls.
Active Permissions shall not be modified during an authorization evaluation.

Testing Requirements
Functional Tests
Verify:
Permission creation.
Permission approval.
Permission activation.
Permission assignment.
Permission matching.
Permission revocation.
Permission suspension.
Authorization decisions.
Governance Tests
Verify:
Constitutional denial cannot be overridden.
Policy denial cannot be overridden.
Invalid Permissions cannot become Active.
Invalid assignments cannot authorize actions.
Security Tests
Verify protection against:
Privilege escalation.
Permission injection.
Assignment tampering.
Unauthorized revocation.
Identity substitution.
Authorization bypass.
Determinism Tests
Identical:
Subject
Action
Resource
Context
Rules
Policies
Permissions
Engine version
shall produce the same authorization decision.
Failure Tests
Verify safe behavior during:
Repository failure.
Governance service failure.
Identity validation failure.
Constraint evaluation failure.
Internal authorization failure.

Compliance Requirements
A PERM-001 implementation is compliant only if it:
Implements the canonical Permission Object.
Respects RULE-001.
Respects POLICY-001.
Uses CORE-000 terminology.
Follows SPEC-000 dependencies.
Implements the authorization decision model.
Preserves auditability.
Passes REVIEW-000.

Implementation Constraints
Implementations shall not:
Grant implicit permissions.
Override RULE-001.
Override POLICY-001.
Treat missing authorization as ALLOW.
Modify active authorization state without controlled lifecycle operations.
Introduce undocumented authorization interfaces.

Completion Criteria
PERM-001 is complete when:
Permission architecture is defined.
Permission lifecycle is defined.
Assignment and revocation are defined.
Authorization evaluation is defined.
Internal architecture is defined.
External interfaces are defined.
Security requirements are defined.
Testing requirements are defined.
Compliance requirements are defined.
REVIEW-000 approval is obtained.
SPEC-000 is updated.
Produced concepts are registered in CORE-000.

Status Declaration
Document ID
PERM-001

Version
1.0.0

Status
Implementation Ready

Architecture Stage
Architecture Candidate v1.0

Final Constitutional Rule
ISIL shall authorize capabilities only through explicit, valid, and governed Permission assignments. Authorization shall remain subordinate to Constitutional Rules and Policies, fail safely under uncertainty, and remain fully auditable.

