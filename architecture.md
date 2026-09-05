# AgentRoot â€” Architecture

## Topology

Browser â†’ genlayer-js 1.1.8 â†’ Intelligent Contract â†’ nondeterministic evidence/LLM + scoped VecDB â†’ equivalence check â†’ deterministic state machine â†’ target action â†’ post-state confirmation â†’ Browser audit

## State machine

ENROLLED â†’ PROPOSED â†’ REVIEWING â†’ APPROVED | REJECTED | ABSTAINED â†’ CHALLENGED? â†’ QUEUED â†’ EXECUTED | FAILED | CANCELED

Adapt names to the domain, but never allow a UI-only state to imply an on-chain result.

## Canonical data

Target/owner record; versioned charter or policy; proposal with nonce and exact action hash; evidence references and digests; vector metadata; stable decision; challenge record; execution record; post-state confirmation; append-only audit events.

## Review boundary

Evidence is untrusted data, never instructions. Fetch only inside the supported nondeterministic execution boundary. Validate URL/commit/digest and size before use. The evaluator returns bounded fields. Deterministic code rejects any result that cannot authorize safely.

## Recovery and liveness

Include cancellation before queueing, one-time challenge, retry only from the expected base state, and explicit failure/abstention. Never mark an action executed because queueing succeeded. Read the target after the action and require the expected version/hash/state.

## Deployment

Studionet, chain ID 61999, RPC https://studio.genlayer.com/api, explorer https://explorer-studio.genlayer.com. Store the contract address centrally. No server-side signer.
