# ISIL Test Architecture

Tests are organized by verification responsibility.

- unit/ — isolated deterministic behavior
- integration/ — component interactions
- api/ — HTTP/API contracts
- security/ — security controls and abuse cases
- database/ — persistence and transaction behavior
- intelligence/ — intelligence/pipeline behavior
- adapters/ — provider and external adapter contracts
- end_to_end/ — complete user-to-system flows
- contracts/ — machine-verifiable architectural/API contracts
- fixtures/ — reusable deterministic test data
- performance/ — benchmark and latency tests
- load/ — concurrency and throughput validation
- chaos/ — resilience and failure injection
