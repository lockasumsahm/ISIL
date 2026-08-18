ISIL MVP — POST-DOCUMENT BUILD WORKFLOW
Website Security Guardian — Controlled Engineering Workflow
0. SOURCE OF TRUTH
   The MVP document is the single source of truth.
   AI coding agents MUST NOT:
   expand the product scope without approval
   invent major architecture
   create unnecessary services
   change security requirements
   add autonomous production actions
   scan targets without explicit authorization
   modify the MVP definition
   treat their own generated architecture as authoritative
   AI agents MAY:
   implement the approved specification
   create code, tests, schemas, APIs and UI
   identify implementation conflicts
   propose improvements
   report blockers
   request human approval for architectural changes

PHASE 1 — REPOSITORY AUDIT
Before writing new code:
Inspect the complete repository.
Read:
AGENTS.md
CLAUDE.md
MVP document
blueprint/index files
existing application code
configuration
tests
dependency files
Map the existing system.
Identify what already works.
Identify missing MVP components.
DO NOT rewrite working components unnecessarily.
Output:
CURRENT SYSTEM
EXISTING COMPONENTS
MISSING MVP COMPONENTS
SECURITY RISKS
DEPENDENCIES
IMPLEMENTATION PLAN

No coding begins until this audit is complete.

PHASE 2 — FREEZE THE MVP
Create:
MVP-SCOPE.md

It contains only:
Target user
Small companies, startups and developers who need practical website/application security visibility without maintaining a full security team.
Core workflow
Connect Website
↓
Verify Authorization
↓
Define Scope
↓
Run Safe Scan
↓
Collect Evidence
↓
Security Analysis
↓
Risk Classification
↓
AI Explanation
↓
Security Dashboard
↓
Remediation Guidance
↓
Rescan
↓
Verify Improvement

MVP does NOT automatically fix production systems.
The first version explains and guides.

PHASE 3 — BUILD THE SECURITY FOUNDATION FIRST
Before the scanner:
Authentication
Authorization
Tenant isolation
Input validation
Rate limiting
Secrets management
Audit logging
Error handling
Data protection
Scope enforcement

Critical rule:
NO AUTHORIZATION
=
NO SCAN

A user must prove they control or are authorized to test the target.

PHASE 4 — BUILD THE SCAN ORCHESTRATOR
The API receives:
target
scope
authorization
scan configuration

The orchestrator creates a scan job.
Example:
POST /scans

        ↓

Authorization Check

        ↓

Scope Validation

        ↓

Scan Job

        ↓

Sandboxed Scanner

        ↓

Evidence Store

        ↓

Finding Engine

Every scan receives a unique ID.

PHASE 5 — START WITH HIGH-VALUE SECURITY CHECKS
Do NOT attempt every cybersecurity vulnerability on day one.
Initial checks:
HTTPS/TLS
Security headers
Exposed secrets
Sensitive files/configuration exposure
Basic authentication/session weaknesses
Authorization/access-control indicators
API exposure/misconfiguration
Dependency vulnerabilities
Common security misconfiguration
Basic data-exposure indicators
Rate-limit indicators where safely testable
Input-validation indicators where safely testable
Every finding must contain:
Finding
Severity
Evidence
Affected target
Why it matters
Confidence
Recommended remediation
References
Timestamp
Scan ID


PHASE 6 — EVIDENCE BEFORE AI
This is one of ISIL's most important rules.
Website
↓
Deterministic security checks
↓
Evidence
↓
Finding
↓
AI

NOT:
Website
↓
AI guesses vulnerability

AI explains and prioritizes evidence.
AI does not manufacture evidence.
If evidence is insufficient:
STATUS = NEEDS VERIFICATION

not:
STATUS = VULNERABLE


PHASE 7 — SANDBOXED VALIDATION
Potentially dangerous validation runs inside an isolated environment.
The sandbox must have:
restricted permissions
restricted filesystem access
restricted network access
execution limits
timeout limits
resource limits
complete audit logging
no access to ISIL secrets
Production systems are NEVER used as a general AI experimentation environment.

PHASE 8 — AI SECURITY ANALYSIS
AI receives structured evidence, not unrestricted access to the target.
Input:
Finding
Evidence
Context
Security rule
Severity criteria

AI produces:
What happened
Why it matters
Potential impact
Confidence
How to fix it
What to verify after fixing

AI cannot:
change scan scope
approve its own permissions
delete evidence
declare itself successful
execute production fixes
change security policy


PHASE 9 — DASHBOARD
After scanning, the customer sees:
SECURITY SCORE

CRITICAL
HIGH
MEDIUM
LOW
INFO

Then:
Finding
↓
Evidence
↓
Risk
↓
Explanation
↓
Recommended Fix
↓
Rescan

The dashboard should answer one question immediately:
“What is wrong with my website, how serious is it, and what should I do next?”

PHASE 10 — RESCAN / VERIFICATION
After the customer fixes something:
Original Finding
↓
Customer Fix
↓
Rescan
↓
Compare Evidence
↓
Resolved / Still Present / Changed

This creates the first real feedback loop.

PHASE 11 — TESTING
Every major component requires:
Unit tests
Security rules, validation, authorization, scoring.
Integration tests
API → scanner → evidence → findings → database.
Security tests
Authentication bypass
Authorization bypass
Scope bypass
Secret leakage
Injection attempts
Malformed input
Rate-limit bypass
Tenant isolation
End-to-end test
Create account
→ Add authorized test website
→ Scan
→ Detect known test vulnerabilities
→ Generate evidence
→ Generate report
→ Fix test vulnerability
→ Rescan
→ Confirm resolution

The MVP is not complete until this workflow works reliably.

PHASE 12 — AI AGENT CONTROL
All coding agents working on ISIL follow this loop:
READ
↓
UNDERSTAND
↓
PLAN
↓
ASK / REPORT CONFLICTS
↓
IMPLEMENT
↓
TEST
↓
SECURITY AUDIT
↓
REVIEW
↓
COMMIT

Never:
PROMPT
↓
AUTONOMOUSLY REBUILD EVERYTHING

Every agent task should be small.
Example:
TASK:
Implement HTTPS security-header scanner.

READ:
MVP-SCOPE.md
scanner architecture
finding schema

DO:
Implement scanner
Add tests
Add evidence output

DO NOT:
Change database architecture
Add new AI model
Add autonomous remediation
Modify MVP scope

DONE WHEN:
Tests pass
Evidence is generated
Finding schema is valid
No security regression exists


PHASE 13 — USE DEVELOPMENT TOOLS INTENTIONALLY
Existing tools can be used as specialized workers.
Playwright
Website/browser behavior and controlled web inspection.
Security testing tools
Use only against authorized targets and within the defined scope.
Context/reference tools
Use for documentation and implementation reference.
Sentry / observability
Application errors and operational visibility.
Supabase/PostgreSQL
MVP persistence.
Ollama/local models
Optional local AI experimentation; not required to make the security engine authoritative.
Coolify/self-hosting
Deployment infrastructure when the MVP is ready.
Do not add a tool merely because it exists.
Every tool must have a defined job.

PHASE 14 — RELEASE GATE
Before public MVP:
[ ] Authentication secure
[ ] Authorization secure
[ ] Target authorization enforced
[ ] Scope enforcement tested
[ ] Rate limiting active
[ ] Secrets protected
[ ] Tenant isolation tested
[ ] Sandbox tested
[ ] Audit logging active
[ ] Evidence system working
[ ] Security checks working
[ ] AI hallucination safeguards tested
[ ] Dashboard working
[ ] Rescan working
[ ] Error handling tested
[ ] Privacy/data disclosure available
[ ] No automatic production remediation
[ ] End-to-end test passes

Only then:
PRIVATE PILOT
↓
REAL USERS
↓
MEASURE
↓
FIX
↓
IMPROVE
↓
PUBLIC MVP


PHASE 15 — MEASURE REAL VALUE
Track:
Scans completed
Findings detected
Findings verified
False positives
False negatives discovered
Time to understand finding
Time to remediation
Rescan resolution rate
Repeat usage
Customer retention

The most important metric:
Did ISIL help the customer discover and understand a real security problem they could actually fix?

FINAL ENGINEERING RULE
ISIL should become progressively more capable, not progressively more complicated.
ONE USER
↓
ONE WEBSITE
↓
ONE AUTHORIZED SCAN
↓
REAL EVIDENCE
↓
USEFUL FINDINGS
↓
CLEAR REMEDIATION
↓
RESCAN
↓
PROVEN VALUE
↓
EXPAND

The first MVP proves the security guardian works.
The larger ISIL architecture comes later.

