# AgentRoot â€” Project Plan

## Objective

Deliver a live, auditable protocol demo whose key moment is a dangerous or consequential action being correctly approved, rejected, challenged, or confirmed by a GenLayer-aware contract.

## Build order

1. Read this pack and inspect the existing repository's tested GenLayer patterns.
2. Define storage structs, bounded fields, generated IDs, enums, event records, and state transitions before writing the evaluator.
3. Implement deterministic guards first: authorization, hashes, nonce/replay, caps, windows, target binding, and confirmation checks.
4. Implement the nondeterministic evaluator inside the supported equivalence-principle pattern. Return a strict JSON schema; compare only authorization-critical fields; abstain on malformed, unavailable, low-confidence, or contradictory evidence.
5. Add Vector Store retrieval as scoped context with model/version metadata and direct-mode fixtures.
6. Build the frontend as an operations console matching ui/ux.md, not as a generic form dashboard.
7. Add direct tests, schema verification, integration tests, and a complete adverse-path proof before visual polish.
8. Deploy to Studionet, record every address/hash in handoff.md, and verify the frontend reads the deployed state.

## Scoring surface

- GenLayer necessity: validators interpret the hard semantic question.
- Protocol depth: roles, versioning, adversarial inputs, challenge, bounded execution, and post-state confirmation.
- Technical rigor: fail-closed behavior, byte/hash binding, deterministic consequences, and no fabricated status.
- Demo quality: one-click readable lifecycle with a visibly blocked malicious case and a successful case.
- Reusability: expose a narrow primitive other protocols could call or consume.

## Definition of done

The happy path, malicious path, malformed-output path, changed-source path, unauthorized path, replay path, and confirmation-failure path are tested and visible in the final UI.
