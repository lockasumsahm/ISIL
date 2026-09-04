# ISIL Security Controls

## Mandatory controls

- Authentication on protected interfaces
- Centralized authorization
- Tenant isolation
- Input validation
- Output validation
- Secret protection
- Audit logging
- Rate limiting
- Request timeouts
- Safe retry policy
- Prompt-injection defenses
- Tool authorization
- External-content isolation
- Dependency vulnerability scanning
- Secret scanning
- Static analysis
- Artifact integrity
- Release provenance

## AI-specific controls

- Treat model output as untrusted data.
- Treat repository content as untrusted data.
- Treat MCP responses as untrusted data.
- Never permit retrieved content to redefine system authority.
- Never expose secrets to models unnecessarily.
- Enforce tool permissions outside the model.
- Enforce tenant boundaries outside the model.
