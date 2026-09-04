# ISIL Requirement Traceability

Every major requirement should eventually map:

REQ
 ->
ARCH
 ->
SPEC
 ->
IMPLEMENTATION
 ->
TEST
 ->
SECURITY CONTROL

Example:

REQ-001
ARCH-001
SPEC-001
app/core/...
tests/contracts/...
SEC-001

No critical requirement is considered verified until an executable verification artifact exists.
