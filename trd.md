# AgentRoot â€” TRD

## Contract surface

Minimum public methods:

$methods

Use typed dataclasses and bounded strings/arrays. Generated IDs must prevent caller overwrite. Keep proposal, evidence, decision, challenge, and execution records separate so getters can be paginated.

## Decision schema

Define a versioned JSON schema with: decision, confidence_band, policy_fit, critical_risks, evidence_ids, source_status, and bounded ationale. Only the enumerated fields that affect authorization participate in equivalence. Free-form rationale is explanatory only.

## Deterministic / nondeterministic split

Charter interpretation and code/config risk are nondeterministic; roles, hashes, limits, windows, nonce, target, calldata, and post-state confirmation are deterministic.

Deterministic code must own: caller roles, target identity, commit/hash binding, nonce and replay protection, caps, version pins, challenge windows, status transitions, one-time execution, and live post-state confirmation.

Nondeterministic execution may own only: fetching declared public evidence, embedding/retrieval context, interpreting natural language, identifying semantic risks, and proposing bounded decision fields.

## Vector Store design

VecDB[float32, 384, EvidenceValue] or the exact supported typed equivalent. Values include ecord_id, scope_id, kind, source_ref, digest, excerpt, and model_version. KNN is scoped to the current proposal/charter and is capped. Do not loop over unbounded storage.

## Threat model

Prompt injection, mutable URLs, malicious source code/config, replayed proposals, swapped calldata, unauthorized executor, stale policy version, validator disagreement, malformed output, target-side partial execution, and frontend status spoofing.

## Tests

Direct: every transition, role, bound, replay, hash mismatch, challenge, malformed output, disagreement, abstention, and retry.

Integration: deploy target and protocol; run clean and malicious proposals; confirm target state, protocol state, and receipts; verify schema and production build.
