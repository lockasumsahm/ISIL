ISIL-MVP-001
ISIL Website Security Guardian
Canonical MVP Product & Engineering Specification
Status: Canonical MVP
Product: ISIL Website Security Guardian
Mission: Provide small companies, developers, startups, and AI-built applications with an authorized security guardian that continuously identifies, explains, validates, and tracks common website/application security risks.

1. PRODUCT DEFINITION
   ISIL allows an authorized owner to connect a website/application, define its assessment scope, run a controlled security assessment, analyze the observed attack surface and configuration, identify security findings, explain their evidence and impact, recommend remediation, and verify fixes through rescanning.
   Core loop:
   CONNECT
   ↓
   AUTHORIZE
   ↓
   SCOPE
   ↓
   DISCOVER
   ↓
   SCAN
   ↓
   ANALYZE
   ↓
   VALIDATE
   ↓
   FINDINGS
   ↓
   EXPLAIN
   ↓
   REMEDIATE
   ↓
   RESCAN
   ↓
   VERIFY
   ↓
   IMPROVE

ISIL does not claim that a website is completely secure. It reports what its assessment can actually establish.

2. TARGET CUSTOMER
   MVP targets:
   small companies
   startups
   independent developers
   SaaS builders
   AI-assisted/AI-generated applications
   agencies
   technical founders
   teams without dedicated security personnel
   Primary problem:
   “I built or operate a website/application, but I do not know whether common security problems are exposing my users, credentials, APIs, data, or infrastructure.”

3. AUTHORIZED TARGET CONNECTION
   Every target must contain:
   Target URL
   Organization
   Owner
   Authorization status
   Assessment scope
   Created timestamp
   Last scan
   Current security score

Before scanning:
☐ I own or am authorized to assess this target.
☐ I understand the assessment scope.
☐ I authorize ISIL to perform the defined assessment.

ISIL must refuse or stop assessment when authorization/scope is absent or invalid.
MVP supports:
HTTPS website
public application
explicitly authorized domains/subdomains
defined assessment scope
Future versions may support authenticated application testing, repositories, cloud environments, APIs, and infrastructure.

4. MVP SECURITY ASSESSMENT ENGINE
   The scanner evaluates observable security controls including:
   Authentication & Sessions
   authentication exposure indicators
   session-cookie security
   secure/HttpOnly/SameSite configuration
   session transport protection
   obvious authentication misconfiguration
   Authorization
   exposed administrative surfaces
   publicly reachable privileged functionality
   obvious access-control indicators
   authorization-related configuration findings
   API Security
   discovered API surfaces
   exposed API documentation
   insecure transport
   authentication/configuration indicators
   excessive information exposure
   HTTPS/TLS & Headers
   HTTPS enforcement
   certificate/TLS observations
   HSTS
   CSP
   X-Content-Type-Options
   X-Frame-Options / frame protection
   Referrer-Policy
   Permissions-Policy
   other relevant security headers
   Secrets & Credentials
   exposed credentials/API keys where safely detectable
   secrets appearing in public client assets
   sensitive configuration exposure
   credential-like material
   Never expose discovered secrets in the UI; redact them.
   Dependencies
   Where authorized dependency/project information is available:
   known vulnerable dependencies
   outdated security-sensitive packages
   dependency risk
   package metadata
   Sensitive Files & Configuration
   Detect observable exposure of:
   environment/configuration files
   debug information
   source maps where relevant
   directory listings
   backup artifacts
   publicly accessible sensitive files
   server metadata
   Data Exposure
   Detect indicators of:
   excessive information disclosure
   exposed database-related configuration
   publicly accessible sensitive endpoints
   unintended sensitive response data
   Common Web Application Risks
   Check safely for common classes of weaknesses where the MVP can establish evidence without destructive exploitation.
   Security Misconfiguration
   Identify:
   debug mode indicators
   insecure defaults
   unnecessary public services/surfaces
   missing protective controls
   deployment/configuration weaknesses
   AI/Application Security
   Identify observable AI-related risks such as:
   exposed AI/API credentials
   insecure AI endpoints
   publicly exposed model configuration
   unsafe client-side AI secrets
   obvious AI integration security misconfiguration
   unsafe trust boundaries observable from the application
   AI findings are evidence-based; ISIL does not pretend to understand hidden application behavior it cannot observe.

5. SAFE VALIDATION & SANDBOX
   ISIL separates observation from validation.
   Passive/low-impact discovery
   ↓
   Security rule detection
   ↓
   Evidence collection
   ↓
   Controlled validation
   ↓
   Finding confidence

Where a finding requires behavioral validation, ISIL may use an isolated sandbox/test environment only when explicitly authorized and technically available.
Sandbox principles:
isolated execution
no production modification
resource limits
network restrictions
time limits
no destructive actions
no persistence
complete audit logging
automatic termination
evidence capture
cleanup after execution
Production systems must never be modified by the MVP.
The MVP is a security assessment and guidance system, not an autonomous penetration-testing agent.

6. FINDING ENGINE
   Every finding follows one canonical structure:
   Finding ID
   Title
   Severity
   Confidence
   Target
   Asset
   Category
   Evidence
   Why It Matters
   Potential Impact
   Recommended Fix
   Verification Method
   Status
   First Detected
   Last Detected
   Resolved At
   Scanner Version
   Rule Version

Severity:
CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL

Confidence:
CONFIRMED
HIGH
MEDIUM
LOW

ISIL must distinguish:
“Detected”
from:
“Suspected.”
No fabricated certainty.

7. EVIDENCE-FIRST AI
   AI is not the source of truth.
   Architecture:
   Scanner
   ↓
   Evidence
   ↓
   Deterministic Rules
   ↓
   Finding
   ↓
   Risk Analysis
   ↓
   AI Explanation

AI may:
explain findings
summarize evidence
prioritize remediation
generate human-readable guidance
explain technical impact
suggest verification steps
AI may not:
invent evidence
invent vulnerabilities
claim an exploit succeeded without evidence
expose secrets
autonomously modify production
bypass authorization
expand assessment scope
hide uncertainty
Every AI-generated statement must be traceable to available evidence or clearly marked as guidance/inference.

8. SECURITY SCORE
   ISIL generates a posture score based on actual findings.
   Example:
   78 / 100
   MODERATE RISK

2 HIGH
4 MEDIUM
7 LOW

Score calculation must be deterministic and versioned.
The score is a posture indicator, not a guarantee of security.

9. CUSTOMER DASHBOARD
   MVP dashboard contains:
   Security Overview
   Websites
   Scans
   Findings
   Finding Details
   Scan History
   Security Trends
   Reports
   Usage
   Billing
   Settings
   Audit History

Customer can see:
current score
open findings
severity distribution
confidence
security categories
scan history
resolved findings
unresolved findings
improvement over time

10. REMEDIATION
    MVP is recommendation-first.
    For each finding:
    WHAT IS WRONG
    ↓
    EVIDENCE
    ↓
    WHY IT MATTERS
    ↓
    HOW TO FIX IT
    ↓
    HOW TO VERIFY IT

Example:
Exposed API credential

Evidence:
Public client asset contains credential-like material.
Value is redacted.

Recommended action:
1. Rotate credential.
2. Remove credential from client-side code.
3. Move secret to protected server-side storage.
4. Deploy change.
5. Rescan.

No automatic production changes in MVP.
Future:
Generate Fix
→ Human Review
→ Explicit Approval
→ Controlled Execution
→ Verification


11. RESCAN & VERIFICATION
    Every finding supports:
    OPEN
    ACKNOWLEDGED
    FIXED_PENDING_VERIFICATION
    RESOLVED
    REOPENED
    FALSE_POSITIVE

After remediation:
RESCAN
↓
REASSESS
↓
VERIFIED ✓

ISIL must preserve historical evidence and show whether the finding actually disappeared.

12. REPORTING
    Generate a security assessment report containing:
    organization
    target
    authorization
    scope
    assessment timestamp
    scanner version
    security score
    findings
    severity
    confidence
    evidence
    remediation guidance
    verification status
    historical comparison
    limitations/disclaimers
    Export:
    PDF
    JSON


13. USAGE & BILLING
    Usage unit:
    One completed assessment of one authorized target at one point in time.
    MVP:
    FREE
    3 scans/month
    1 website
    Security findings
    Score
    Basic report
    Rescanning

STARTER
25 scans/month
5 websites
Full reports
History
Advanced findings

PRO
100 scans/month
20 websites
Continuous/scheduled scanning
Team features
Advanced reporting

Usage dashboard:
2 / 3 scans used
1 / 1 websites
Reset date

Failed ISIL infrastructure scans do not consume customer usage.
Security history remains accessible after usage is exhausted.

14. AUDIT & GOVERNANCE
    Log:
    login events
    target creation
    authorization
    scope changes
    scan initiation
    scan completion
    findings
    finding status changes
    report generation
    rescan
    billing events
    administrative actions
    AI actions
    scanner/ruleset versions
    Every important security event must be traceable.

15. ISIL SELF-PROTECTION
    ISIL must apply its own security principles to itself.
    Minimum:
    secure authentication
    authorization
    encrypted transport
    secret management
    input validation
    rate limiting
    audit logging
    dependency monitoring
    secure headers
    isolated scanner execution
    tenant isolation
    data minimization
    encrypted sensitive data
    least privilege
    scanner sandbox isolation
    ISIL must never become the security vulnerability it claims to detect.

16. CORE MVP ARCHITECTURE
    ISIL WEB APP
    │
    ▼
    API / AUTH LAYER
    │
    ┌───────────┴───────────┐
    ▼                       ▼
    TARGET MANAGER          USAGE/BILLING
    │
    ▼
    AUTHORIZATION
    │
    ▼
    SCAN ORCHESTRATOR
    │
    ┌────┴────┐
    ▼         ▼
    DISCOVERY   RULE ENGINE
    │         │
    └────┬────┘
    ▼
    EVIDENCE
    │
    ▼
    FINDING ENGINE
    │
    ┌────┴────┐
    ▼         ▼
    RISK ENGINE   AI
    │         │
    └────┬────┘
    ▼
    RESULTS API
    │
    ┌────┼─────────────┐
    ▼    ▼             ▼
    DASHBOARD REPORT     HISTORY
    │
    ▼
    RESCAN
    │
    ▼
    VERIFICATION


17. MVP DATA MODEL
    Minimum entities:
    User
    Organization
    Membership
    Target
    Authorization
    Scope
    Scan
    Asset
    Finding
    FindingEvent
    Evidence
    Report
    Usage
    Subscription
    AuditEvent

Do not introduce unnecessary enterprise entities until the MVP requires them.

18. MVP API SURFACE
    /auth/*
    /organizations/*
    /targets/*
    /authorizations/*
    /scans/*
    /findings/*
    /reports/*
    /usage/*
    /billing/*
    /audit/*

API must enforce:
authentication
authorization
tenant isolation
rate limits
input validation
audit logging

19. MVP NON-GOALS
    Do NOT build initially:
    autonomous hacking
    autonomous production remediation
    VPN
    browser extension
    enterprise SOC
    cloud-wide security platform
    full penetration-testing platform
    autonomous security agent
    unrestricted AI agent
    infrastructure takeover
    destructive testing
    broad enterprise compliance platform
    These are future expansion areas.

20. DEFINITION OF DONE
    The MVP is complete only when a real authorized customer can:
1. Create account
2. Create organization
3. Add website
4. Confirm authorization
5. Define scope
6. Start scan
7. See real scan progress
8. Receive evidence-backed findings
9. Understand severity/confidence
10. See security score
11. Read remediation guidance
12. Download report
13. Fix a finding
14. Rescan
15. See verification
16. View scan history
17. Track usage
18. Upgrade when usage ends
19. View billing status
20. See audit history

And the entire process must work without ISIL modifying the customer's production system.

FINAL PRODUCT PRINCIPLE
ISIL is not an AI that randomly “checks security.” ISIL is an evidence-first security guardian that establishes authorization, observes the authorized attack surface, safely validates what it can, converts evidence into structured findings, explains those findings with AI, guides remediation, and verifies improvement through rescanning.
The MVP proves one thing:
A small company can connect its website to ISIL and get a trustworthy answer to: “What security problems can ISIL actually find, what should I fix first, and did the fix work?”
Everything beyond that belongs to the larger ISIL architecture.


