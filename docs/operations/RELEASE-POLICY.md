# ISIL Release Policy

Environments:

- development
- staging
- production

Release path:

commit
 -> CI
 -> artifact
 -> staging
 -> automated validation
 -> approval
 -> production
 -> health verification
 -> rollback capability

Every production release must have:

- release identifier
- commit SHA
- artifact digest
- deployment record
- health verification
- rollback procedure
