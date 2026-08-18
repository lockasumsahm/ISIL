# ISIL — Universal Connection, Authorized Deep Access & Zero-Expertise UX Standard

**Document ID:** ISIL-CONNECTION-UX-001
**Status:** Canonical MVP Requirement
**Authority:** ISIL-MASTER-INDEX-001
**Product:** ISIL Website Security Guardian

---

# 1. PURPOSE

ISIL must make connecting and assessing an authorized website/application as easy as possible while preserving strict authorization, privacy, security, scope, and audit controls.

The product must support two principles simultaneously:

> **SIMPLE FOR EVERYONE**

and

> **DEEP FOR DEVELOPERS**

A beginner should be able to protect a website without understanding cybersecurity or software engineering.

A developer should be able to authorize deeper access to source code, repositories, APIs, dependencies, staging environments, and other relevant application resources when technically supported and explicitly authorized.

---

# 2. CORE PRODUCT PROMISE

The ideal experience is:

> **ENTER WEBSITE**

↓

> **AUTHORIZE**

↓

> **ISIL CONNECTS**

↓

> **ISIL DISCOVERS**

↓

> **ISIL SCANS**

↓

> **ISIL EXPLAINS**

↓

> **USER FIXES**

↓

> **CHECK AGAIN**

↓

> **VERIFIED ✓**

The customer should perform only the actions that genuinely require customer authority.

ISIL should perform everything else that it can safely automate.

---

# 3. UNIVERSAL CONNECTION PRINCIPLE

ISIL must use a **provider-independent Universal Connection Layer**.

The core security engine must not depend on:

* Claude
* Claude Code
* Codex
* Lovable
* Cursor
* Copilot
* Gemini
* GitHub
* GitLab
* Vercel
* Netlify
* Supabase
* any single cloud provider
* any single AI provider
* any single website builder

These are integration paths.

They are not architectural authorities.

The ISIL core remains provider-independent.

---

# 4. UNIVERSAL CONNECTOR ARCHITECTURE

The architecture should follow:

```text
                         ISIL
                           │
                           ▼
                 UNIVERSAL CONNECTION
                         LAYER
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        PUBLIC WEB      APPLICATION    DEVELOPMENT
          ACCESS          ACCESS          ACCESS
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    AUTHORIZATION
                           │
                           ▼
                       SCOPING
                           │
                           ▼
                    RESOURCE GRAPH
                           │
                           ▼
                    SCAN ORCHESTRATOR
                           │
                           ▼
                    SECURITY ENGINE
```

New providers and connection mechanisms must be implemented as adapters/connectors wherever possible.

The core security engine must not be rewritten for every new provider.

---

# 5. CONNECTION LEVELS

ISIL should progressively unlock deeper assessment capability.

## Level 1 — Public Website

Customer provides:

> `https://example.com`

ISIL can safely assess observable public surfaces after authorization.

Possible observations include:

* HTTPS/TLS
* security headers
* cookies
* public assets
* client-side code
* exposed endpoints
* API indicators
* public configuration
* public files
* technology indicators
* observable information disclosure
* other safe public observations

No private code access is implied.

---

## Level 2 — Ownership / Domain Authorization

ISIL verifies that the customer controls or is authorized to assess the target.

Preferred mechanisms include:

* secure provider authorization
* domain verification
* DNS verification
* verification file
* supported platform authorization
* other secure ownership mechanisms

ISIL must automatically verify the result.

---

## Level 3 — Application Access

Where appropriate and explicitly authorized, ISIL may connect to application resources.

Examples:

* source repository
* dependency manifests
* API specifications
* configuration metadata
* staging environment
* test environment
* authorized application services

Access should be:

> **MINIMUM REQUIRED**

> **READ-ONLY BY DEFAULT**

> **EXPLICITLY AUTHORIZED**

---

## Level 4 — Deep Application Security

When the customer authorizes deeper access, ISIL may correlate:

> Website

*

> Source Code

*

> Dependencies

*

> APIs

*

> Configuration

*

> Authorized Test/Staging Environment

to produce a deeper security assessment.

The customer should not have to manually connect every resource when a trusted authorization provider can expose them safely.

---

# 6. AUTHORIZATION IS THE SECURITY BOUNDARY

Universal connectivity does not mean universal permission.

The immutable rule is:

```text
AUTHORIZATION
      ↓
SCOPE
      ↓
ACCESS
      ↓
SCAN
```

Never:

```text
CONNECT
   ↓
SCAN EVERYTHING
```

ISIL must never:

* scan unauthorized targets
* access private code without permission
* access private resources without permission
* bypass authentication
* obtain credentials without authorization
* expand scope automatically
* use one authorization to access unrelated resources
* allow an AI agent to grant itself permission
* modify production automatically
* silently escalate privileges

---

# 7. ZERO-EXPERTISE FIRST EXPERIENCE

The first screen should simply ask:

> **What website do you want to protect?**

Input:

> **Website URL**

Then:

> **Protect My Website**

No scanner configuration should be required.

No cybersecurity terminology should be required.

No API knowledge should be required.

No CLI knowledge should be required.

No code knowledge should be required.

---

# 8. AUTOMATIC DISCOVERY

After the URL is entered and authorization is established, ISIL automatically determines what it can safely inspect.

The user should not manually configure:

* crawlers
* security headers
* TLS checks
* public assets
* API discovery
* basic configuration checks
* safe discovery rules
* evidence collection

ISIL handles these automatically.

---

# 9. SMART DEEP-ACCESS RECOMMENDATION

If public inspection cannot establish important security properties, ISIL should explain this in simple language.

Example:

> **Your website is connected.**

> **We can check the public website now.**

> **For a deeper security assessment, we can also inspect the application's code and dependencies.**

> **This can reveal security problems that cannot be seen from the public website.**

Then:

> **Connect Application Code**

The user should not need to understand why repositories or dependencies matter.

---

# 10. NATIVE AUTHORIZATION FIRST

When a supported provider offers a secure authorization mechanism, ISIL should use it.

Preferred flow:

```text
CONNECT CODE
      ↓
SECURE AUTHORIZATION
      ↓
USER APPROVES
      ↓
RETURN TO ISIL
      ↓
CONNECTED ✓
```

ISIL should prefer:

1. Native authorization
2. OAuth/application authorization
3. One-click integrations
4. Guided verification
5. Manual verification
6. Advanced developer configuration

---

# 11. NEVER ASK FOR A PASSWORD OR SECRET WHEN A SAFER METHOD EXISTS

ISIL should never unnecessarily ask users to paste:

* passwords
* private keys
* API secrets
* repository tokens
* cloud credentials

If secure authorization is available, use it.

If credentials are genuinely required for an authorized integration, ISIL must use secure secret handling and minimum required permissions.

Secrets must never be displayed unnecessarily.

---

# 12. READ-ONLY BY DEFAULT

Deep integrations should request the smallest useful permission set.

Preferred:

> **READ-ONLY**

The user should clearly see:

> **What ISIL can access**

> **Why ISIL needs it**

> **What ISIL cannot do**

Example:

### ISIL can:

✓ Read security-relevant source code

✓ Inspect dependencies

✓ Analyze configuration

✓ Correlate application and website evidence

### ISIL cannot:

✕ Modify source code

✕ Delete files

✕ Deploy code

✕ Change production

✕ Change permissions

✕ Grant itself additional access

---

# 13. AUTOMATIC RESOURCE DISCOVERY

After authorization, ISIL should automatically discover resources that are legitimately available through that authorization.

For example:

```text
CONNECTED APPLICATION

✓ Website
✓ Repository
✓ Dependencies
✓ API specification
✓ Authorized staging environment
```

ISIL should recommend the safest useful assessment configuration.

The customer can review or modify the scope.

---

# 14. SIMPLE DEFAULT SCOPE

Beginners should not need to understand scope configuration.

Default:

> **Recommended Safe Assessment**

ISIL automatically selects the appropriate safe checks for the authorized resources.

Advanced users may choose:

> **Customize Scope**

and configure:

* domains
* subdomains
* repositories
* branches
* APIs
* environments
* application areas
* authentication context
* assessment rules

---

# 15. ONE ACTION AT A TIME

If manual action is unavoidable, ISIL must never overwhelm the user.

Bad:

> Configure DNS, OAuth, repository permissions, environment variables and CLI credentials.

Good:

> **Step 1 of 1**

> **We need to verify that you control this website.**

> **Add this verification value.**

> **[Copy]**

> **When finished:**

> **[I've Done This]**

ISIL then automatically verifies the result.

---

# 16. NO UNNECESSARY COPY-PASTE

The priority order is:

> **AUTOMATE**

↓

> **ONE-CLICK**

↓

> **GUIDED**

↓

> **COPY**

↓

> **MANUAL**

Copy/paste must be a fallback.

It must never be the default if secure automation is technically possible.

---

# 17. SMART PROVIDER ADAPTERS

The Universal Connection Layer should support adapters for different ecosystems.

Examples may include:

* GitHub
* GitLab
* Bitbucket
* Vercel
* Netlify
* Cloudflare
* Supabase
* common cloud providers
* common CI/CD systems
* common website builders
* common application platforms
* developer environments
* future providers

The architecture must make adding a new provider an adapter problem rather than a core-platform rewrite.

Provider support should be added according to actual API/authorization capabilities.

---

# 18. AI DEVELOPMENT TOOL INTEGRATION

ISIL may provide optional integrations for:

* Claude Code
* Codex
* Cursor
* GitHub Copilot
* Gemini CLI
* other compatible development agents

These tools can assist with:

* installing an ISIL integration
* configuring an authorized project
* generating configuration
* explaining integration steps
* preparing code changes
* running tests

However:

> **AI coding agents are implementation assistants, not authorization authorities.**

They cannot:

* grant ISIL access without user approval
* expand ISIL scope
* bypass provider permissions
* access unrelated repositories
* modify production automatically
* override ISIL security controls

---

# 19. AI WEBSITE BUILDER INTEGRATION

For websites created with AI website builders, ISIL should provide the simplest available connection path.

The customer should ideally be able to:

> **Connect Website**

↓

> **Choose Platform**

↓

> **Authorize**

↓

> **ISIL Automatically Detects Available Resources**

↓

> **Recommended Assessment**

Where a platform does not provide an integration, the URL-based public assessment remains available.

ISIL must never pretend that an integration exists when the platform does not provide the necessary capabilities.

---

# 20. CONNECTION STATUS

The customer should always see what is happening.

Example:

```text
CONNECTING YOUR WEBSITE

✓ Website found
✓ Authorization verified
✓ Scope established
✓ Public surface discovered
✓ Available resources identified
✓ Security assessment prepared

Ready to scan.
```

The system should never leave users wondering whether something is working.

---

# 21. CONNECTION FAILURE

Never display only:

> `Connection failed`

Instead:

> **We couldn't connect this resource.**

> **Why:** Your authorization has expired.

> **No changes were made to your application.**

> **Try again**

or:

> **Choose another connection method**

ISIL should provide the simplest recovery path.

---

# 22. RESOURCE ACCESS CONTROL

Every connected resource must have an explicit record containing, where applicable:

* resource identity
* provider
* owner
* authorization status
* permission level
* scope
* creation time
* last verification
* connection status
* access expiration
* revocation status

Customers must be able to:

> **View Access**

> **Change Scope**

> **Reconnect**

> **Disconnect**

---

# 23. ACCESS REVOCATION

Customers must always be able to disconnect authorized resources.

When disconnected:

> ISIL must stop using the authorization.

Where supported, ISIL should also revoke its provider-side authorization.

Historical security evidence may remain according to ISIL's retention policy, but active access must cease.

---

# 24. RESOURCE GRAPH

ISIL should maintain an internal relationship model:

```text
Organization
      │
      ├── Website
      │
      ├── Repository
      │
      ├── API
      │
      ├── Dependency Set
      │
      └── Authorized Environment
              │
              ▼
           Scope
              │
              ▼
             Scan
              │
              ▼
           Evidence
              │
              ▼
           Findings
```

This allows ISIL to correlate evidence across authorized resources without requiring the customer to manually manage relationships.

---

# 25. EVIDENCE MUST REMAIN SEPARATE FROM CONNECTION

Connection provides access.

Connection does not prove a vulnerability.

The architecture remains:

```text
CONNECTION
    ↓
AUTHORIZED RESOURCE
    ↓
OBSERVATION
    ↓
EVIDENCE
    ↓
DETERMINISTIC RULE
    ↓
FINDING
    ↓
AI EXPLANATION
```

AI must never treat access alone as evidence of a vulnerability.

---

# 26. BEGINNER MODE

Beginner Mode should use human language.

Instead of:

> **“HTTP Strict Transport Security is absent.”**

Say:

> **Your website does not currently tell browsers to always use a secure connection.**

Then:

> **Why this matters**

> **How to fix it**

> **Check Again**

Technical details remain available.

---

# 27. DEVELOPER MODE

Developer Mode exposes:

* technical evidence
* requests/responses where appropriate
* affected assets
* code locations where authorized
* dependencies
* rule IDs
* scanner version
* rule version
* confidence
* raw evidence
* API information
* scan configuration
* logs
* integration details

ISIL should therefore be:

> **Simple on the surface. Deep underneath.**

---

# 28. PROGRESSIVE DISCLOSURE

Information should be layered.

### Level 1

> **3 security issues found**

### Level 2

> **What happened**

### Level 3

> **Why it matters**

### Level 4

> **Evidence**

### Level 5

> **Technical details**

### Level 6

> **Raw developer information**

Beginners should never be forced through Level 6.

---

# 29. CUSTOMER CONTROL

At all times the customer should understand:

> **WHAT IS CONNECTED**

> **WHAT IS AUTHORIZED**

> **WHAT IS BEING SCANNED**

> **WHAT ISIL CAN SEE**

> **WHAT ISIL CANNOT DO**

> **WHAT ISIL FOUND**

> **WHAT EVIDENCE SUPPORTS IT**

> **WHAT THE CUSTOMER SHOULD DO NEXT**

---

# 30. SECURITY INVARIANTS

These requirements are non-negotiable:

```text
NO AUTHORIZATION
      =
NO PRIVATE ACCESS

NO VALID SCOPE
      =
NO SCAN

NO EVIDENCE
      =
NO CONFIRMED FINDING

NO USER APPROVAL
      =
NO PRIVILEGE ESCALATION

NO EXPLICIT PRODUCTION AUTHORIZATION
      =
NO PRODUCTION MODIFICATION
```

The convenience layer must never weaken these invariants.

---

# 31. MVP CONNECTION DEFINITION OF DONE

The connection system is MVP-ready when a first-time non-technical customer can:

* [ ] Enter a website URL.
* [ ] Understand what ISIL wants to do.
* [ ] Authorize the website.
* [ ] Complete ownership verification.
* [ ] Start a safe assessment.
* [ ] See real-time progress.
* [ ] Understand the result.
* [ ] Request deeper application assessment.
* [ ] Grant read-only access where supported.
* [ ] Understand exactly what additional access provides.
* [ ] Connect authorized application resources without unnecessary technical work.
* [ ] Avoid manual secret/token handling whenever a safer method exists.
* [ ] See connected resources.
* [ ] See access permissions.
* [ ] Revoke connections.
* [ ] Rescan.
* [ ] Verify improvement.

A developer must additionally be able to use documented APIs, SDKs, CLI integrations, CI/CD integrations, and supported AI-development workflows.

---

# 32. UNIVERSALITY STANDARD

ISIL must NOT claim:

> **“We can access every website on Earth automatically.”**

That would be technically and architecturally false.

The correct standard is:

> **“ISIL can assess any compatible authorized web target through the simplest available connection method, and its provider-independent architecture allows new platforms and integrations to be added without changing the core security engine.”**

For a public website:

> **URL + authorization → assessment**

For private application resources:

> **explicit authorization → appropriate read-only connection → deeper assessment**

For unsupported platforms:

> **safe fallback connection method**

This is the correct definition of universal connectivity.

---

# 33. FINAL EXPERIENCE STANDARD

ISIL should feel like:

> **“Give ISIL your website. Tell us you are authorized. ISIL handles the complexity.”**

Not:

> **“Configure a cybersecurity platform.”**

Not:

> **“Learn how to use a security scanner.”**

Not:

> **“Open your terminal and follow 14 technical instructions.”**

The product should progressively remove unnecessary technical work while preserving complete security transparency.

---

# 34. FINAL ISIL PRINCIPLE

> **ISIL hides unnecessary complexity — never security truth.**

> **Simple enough for someone who has never used a security tool.**

> **Powerful enough for a professional developer.**

> **Deep enough to inspect authorized application code and security-relevant resources.**

> **Universal enough to support multiple providers without coupling the core platform to any one provider.**

> **Secure enough that convenience never overrides authorization, scope, privacy, or least privilege.**

The ultimate experience is:

```text
             USER
               │
               ▼
        ENTER WEBSITE
               │
               ▼
        AUTHORIZE ISIL
               │
               ▼
       ISIL CONNECTS
               │
               ▼
       ISIL DISCOVERS
               │
               ▼
     ISIL REQUESTS DEEPER
       ACCESS IF NEEDED
               │
               ▼
      USER APPROVES ACCESS
               │
               ▼
       ISIL MAPS RESOURCES
               │
               ▼
        ISIL DEFINES SAFE
             SCOPE
               │
               ▼
          ISIL SCANS
               │
               ▼
       ISIL COLLECTS
           EVIDENCE
               │
               ▼
      ISIL GENERATES
          FINDINGS
               │
               ▼
       AI EXPLAINS
          EVIDENCE
               │
               ▼
       USER FIXES ISSUE
               │
               ▼
         CHECK AGAIN
               │
               ▼
         VERIFIED ✓
```

**This is the canonical 10/10 connection standard for the ISIL MVP:**

> **One website. One clear authorization. Minimum customer effort. Maximum safe automation. Read-only deep access by default. Provider-independent architecture. Evidence-first security. Beginner-friendly UX. Full developer depth when needed.**
