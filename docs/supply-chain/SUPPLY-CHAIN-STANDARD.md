# ISIL Software Supply-Chain Standard

Required direction:

dependency declaration
    ->
lockfile
    ->
dependency vulnerability scan
    ->
secret scan
    ->
SAST
    ->
SBOM
    ->
artifact integrity
    ->
provenance
    ->
release

Rules:

- Prefer pinned/reproducible dependency resolution.
- Do not silently install dependencies during normal application execution.
- Do not commit generated virtual environments.
- Review high-risk dependency changes.
- Record important build provenance.
