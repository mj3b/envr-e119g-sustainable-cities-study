# Data contracts

JSON Schema Draft 2020-12 contracts describe canonical sources, claims, concepts, reading analyses, lecture alignment, synthesis, assignment relevance, and fidelity gates. Validate them with `python3 scripts/validate.py --schemas` after installing requirements-dev.txt.

Canonical records live in cross-course/. Per-reading claims.json and concepts.json contain references to those IDs; reading analysis.json supplies the argument-map pointer. Synthesis records and Assignment 1 relevance records use their respective contracts. The standard-library validator adds cross-record checks and promotion rules that JSON Schema alone cannot express.

The lecture-segment index contains original speaker labels, inferred roles, and segment-local timestamps only. Full segment text remains in private/extracted/. Unknown roles are preserved; they must be reviewed before attribution.

The research-object and discovery contracts cover cases/research-objects.json and cases/discovery.json. Twelve typed payloads require analytical fields such as disconfirmation, access dates, measurement boundaries and alternative origin. scripts/research_checks.py adds typed reference closure, temporal checks, measurement semantics, content-bound research review and selection readiness.
