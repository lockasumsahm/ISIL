# ADR-010 — Agent Safety Architecture

Status: Proposed

Agent execution is treated as a privileged subsystem.

Untrusted inputs include:
- repositories
- tool results
- MCP results
- retrieved documents
- external webpages
- model-generated commands

Required controls include:
- least privilege
- explicit tool allowlists
- command validation
- output validation
- execution boundaries
- secret isolation
- audit events
- runaway limits
- approval boundaries for consequential actions
