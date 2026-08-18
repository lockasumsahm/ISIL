# AI-OPERATING-PROTOCOL.md

# ISIL — AI Operating Protocol

**Status:** Canonical AI Coordination Protocol
**Scope:** All AI agents and AI-assisted engineering systems operating on ISIL
**Primary Engineering Agent:** Claude Code

---

# 1. PURPOSE

This protocol defines how AI systems work on ISIL without creating architectural drift, unsafe autonomy, excessive context consumption, persistent-memory corruption, or unverified engineering changes.

The protocol separates:

```text
Authority
Knowledge
Context
Memory
Implementation
Review
```

---

# 2. AI ENGINEERING STACK

ISIL uses the following roles:

```text
                    HUMAN
                      │
                      ▼
             ISIL MASTER INDEX
                      │
                      ▼
          AI OPERATING PROTOCOL
                      │
                      ▼
                CLAUDE CODE
             Primary Engineer
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Headroom       Claude-Mem    Code Review
   Context        Memory        Graph
   Optimization                 Structural
                                Intelligence
       │              │              │
       └──────────────┼──────────────┘
                      ▼
                ISIL REPOSITORY
```

---

# 3. ROLE DEFINITIONS

## Claude Code

Primary engineering agent.

Responsibilities:

* understand tasks
* inspect repository
* implement changes
* write tests
* run validation
* maintain documentation
* integrate approved tooling
* report results

Claude Code owns execution of engineering tasks.

Claude Code does not own constitutional authority.

---

## Headroom

Context optimization layer.

Responsibilities:

* compress redundant context
* reduce repeated tool output
* reduce token waste
* preserve relevant information
* enable efficient long-context work

Headroom must never alter authoritative meaning.

---

## Claude-Mem

Persistent project memory.

Responsibilities:

* preserve useful historical context
* remember implementation decisions
* retain known issues
* preserve recurring engineering knowledge
* support cross-session continuity

Memory is advisory.

Current authoritative documents override memory.

---

## Code Review Graph

Repository structural intelligence layer.

Responsibilities:

* map code structure
* trace dependencies
* calculate impact radius
* identify affected flows
* identify test relationships
* support efficient code review
* reduce unnecessary repository reading

Graph data describes the codebase.

It does not define ISIL's intended architecture.

---

# 4. SOURCE OF TRUTH

The most important rule:

```text
AI MEMORY ≠ ARCHITECTURE
AI OUTPUT ≠ SPECIFICATION
AI OPINION ≠ POLICY
AI MODEL ≠ AUTHORITY
```

The authoritative chain is:

```text
Human decision
↓
Constitutional Architecture
↓
ISIL-MASTER-INDEX-001
↓
Approved Engineering Specification
↓
Policy
↓
MVP Specification
↓
Current Implementation
↓
AI Proposal
```

---

# 5. STARTUP PROTOCOL

At the beginning of a substantial Claude Code session:

### STEP 1

Locate:

```text
ISIL-MASTER-INDEX-001
```

### STEP 2

Read the relevant Master Index entries.

### STEP 3

Identify the documents governing the requested task.

### STEP 4

Use Code Review Graph if available.

### STEP 5

Inspect only the relevant implementation.

### STEP 6

Check persistent memory for previous decisions.

### STEP 7

Verify remembered decisions against current authority.

### STEP 8

Produce a plan.

Only then implement.

---

# 6. CONTEXT ECONOMY

AI context is treated as an engineering resource.

Use:

```text
Master Index
+
Graph
+
Targeted source reads
+
Relevant memory
```

instead of:

```text
Entire repository
+
Entire documentation corpus
+
Entire conversation
```

Headroom may compress context.

If information is critical, retrieve the source.

Never allow token optimization to reduce correctness.

---

# 7. MEMORY POLICY

Persistent memory may contain:

```text
Architecture decisions
Implementation history
Known bugs
Known failed approaches
Engineering conventions
Task history
```

Persistent memory must NOT contain:

```text
API keys
Passwords
Tokens
Private credentials
Production secrets
Sensitive customer information
```

Memory conflicts are resolved by:

```text
Current authoritative source
>
Memory
```

---

# 8. CODE REVIEW GRAPH POLICY

For codebase exploration:

```text
Code Review Graph
        ↓
Architecture overview
        ↓
Semantic search
        ↓
Impact radius
        ↓
Affected flows
        ↓
Targeted source reading
```

For code changes:

```text
Change
 ↓
Graph update
 ↓
Impact analysis
 ↓
Affected tests
 ↓
Review
```

If the graph is unavailable or stale:

```text
VERIFY / UPDATE GRAPH
```

then continue.

Never trust stale structural data blindly.

---

# 9. IMPLEMENTATION PROTOCOL

Every non-trivial task follows:

```text
UNDERSTAND
    ↓
TRACE
    ↓
PLAN
    ↓
IMPLEMENT
    ↓
TEST
    ↓
SECURITY REVIEW
    ↓
IMPACT REVIEW
    ↓
DOCUMENT
    ↓
REPORT
```

---

# 10. TASK BOUNDARIES

Every task should define:

```text
Objective
Scope
Relevant documents
Allowed files
Expected behavior
Tests
Acceptance criteria
```

Agents should not expand scope automatically.

If additional work is discovered:

```text
OUT-OF-SCOPE FINDING
```

Record it and continue only if it does not compromise the current task.

---

# 11. ARCHITECTURAL CHANGE PROTOCOL

If implementation requires architectural change:

STOP.

Produce:

```text
ARCHITECTURAL CHANGE REQUEST

Current architecture:
Proposed architecture:
Reason:
Alternatives:
Security impact:
Reliability impact:
Maintenance impact:
Provider dependency:
Migration impact:
Rollback:
Testing plan:
```

Human approval is required before implementation.

---

# 12. SECURITY-Critical CHANGE PROTOCOL

For changes involving:

* authentication
* authorization
* secrets
* cryptography
* sandboxing
* agent permissions
* production infrastructure
* data access
* security boundaries

the agent must perform an explicit security review.

Required questions:

```text
What can this access?
What can this execute?
What data can this expose?
What happens if compromised?
What is the blast radius?
How is it audited?
How is it revoked?
How is it tested?
```

---

# 13. AI MODEL ROUTING

ISIL may use multiple models.

Models are selected according to task requirements.

Example:

```text
Simple classification
→ local/low-cost model

Large contextual reasoning
→ primary reasoning model

Independent verification
→ secondary model

Code structure
→ Code Review Graph

Context optimization
→ Headroom

Historical continuity
→ Claude-Mem
```

No model may independently become the final authority for constitutional or security-critical decisions.

---

# 14. MODEL DISAGREEMENT

If two AI systems disagree:

```text
Model A
Model B
   ↓
Evidence comparison
   ↓
Authoritative documentation
   ↓
Human review if unresolved
```

Do not resolve disagreement by majority vote alone.

Evidence has priority over model consensus.

---

# 15. AGENT PERMISSIONS

AI agents operate with least privilege.

Permissions should be separated into:

```text
READ
WRITE
EXECUTE
NETWORK
PRODUCTION
SECRETS
```

Default:

```text
READ = allowed where necessary
WRITE = task-scoped
EXECUTE = task-scoped
NETWORK = restricted
PRODUCTION = denied by default
SECRETS = denied by default
```

Permissions must be explicitly expanded when required.

---

# 16. DESTRUCTIVE OPERATIONS

Destructive actions require explicit human approval.

Examples:

```text
database deletion
production migration
credential revocation
production deployment
data deletion
architecture replacement
repository-wide destructive refactor
```

Never infer approval from a vague instruction.

---

# 17. TESTING PROTOCOL

After implementation:

```text
Unit Tests
↓
Integration Tests
↓
Security Tests
↓
Impact Analysis
↓
Regression Tests
↓
Final Review
```

For security-sensitive code, security validation is mandatory.

---

# 18. SESSION COMPLETION

Before ending a significant engineering session:

```text
1. Summarize changes
2. Run validation
3. Record failures
4. Update documentation if necessary
5. Record useful persistent memory
6. Verify no secrets entered memory
7. Identify remaining work
8. Report architectural impact
```

Do not create false completion.

---

# 19. MEMORY HANDOFF

Useful handoff information:

```text
Completed
Current architecture
Important decisions
Known failures
Known risks
Next task
Relevant files
Relevant Master Index entries
```

Avoid storing temporary conversational noise.

---

# 20. HUMAN OVERSIGHT

AI augments human judgment.

AI does not replace:

* architectural authority
* security acceptance
* legal decisions
* privacy decisions
* production authorization
* risk acceptance
* irreversible operational decisions

Human authority remains final.

---

# 21. FAILURE PROTOCOL

When an agent cannot determine the correct action:

```text
STOP
↓
STATE UNCERTAINTY
↓
SHOW EVIDENCE
↓
IDENTIFY CONFLICT
↓
REQUEST DECISION
```

Never:

```text
UNCERTAIN
↓
GUESS
↓
IMPLEMENT
```

---

# 22. FINAL AI OPERATING LOOP

The permanent ISIL AI engineering loop is:

```text
MASTER INDEX
     ↓
UNDERSTAND
     ↓
GRAPH
     ↓
RELEVANT CONTEXT
     ↓
MEMORY
     ↓
PLAN
     ↓
IMPLEMENT
     ↓
TEST
     ↓
SECURITY REVIEW
     ↓
IMPACT REVIEW
     ↓
DOCUMENT
     ↓
MEMORY HANDOFF
     ↓
NEXT TASK
```

---

# 23. FINAL PRINCIPLE

AI exists to make ISIL engineering more capable.

It must never make ISIL less governed.

Therefore:

```text
More AI
≠
More autonomy

More AI
=
More capability under stronger controls
```

ISIL agents must remain:

```text
evidence-driven
architecture-aware
security-first
privacy-preserving
provider-independent
auditable
reversible
human-governed
```

**The system may evolve. The engineering discipline does not.**
