# ISIL Software Supply Chain

Target pipeline:

source
  ->
locked dependencies
  ->
dependency audit
  ->
SAST
  ->
secret scan
  ->
SBOM
  ->
build
  ->
artifact digest
  ->
provenance / attestation
  ->
deployment

Future requirements:

- reproducible builds
- SBOM generation
- dependency vulnerability monitoring
- artifact signing
- build provenance
- provenance verification
