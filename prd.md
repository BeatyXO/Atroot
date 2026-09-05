# AgentRoot â€” PRD

## User promise

An agent requests a privileged action such as changing permissions, moving treasury funds, deploying code, or publishing a release. The contract checks the action against a versioned authority charter, requires semantic validator approval, executes only hash-bound calldata, then confirms the real post-action state.

## Actors

- Owner/controller: defines the charter or policy.
- Proposer/agent: submits the action or evidence.
- Challenger: submits one bounded adverse signal during the review window.
- Executor/relayer: submits the exact approved bytes.
- Public observer: reads the complete audit trail without a wallet.

## Required product flows

### Setup

Create or enroll the protected target, publish the versioned policy/charter, and show its hash and owner.

### Proposal

Submit an action with target, value, calldata/source reference, nonce, expiry, and human-readable intent. Show the exact bytes that will be bound.

### Review

Display evidence indexing, Vector Store matches, consensus pending state, stable decision fields, confidence band, and abstention reasons. Never invent validator progress.

### Challenge

Allow a bounded challenge with a new evidence reference. Show that a challenge can freeze or redirect the proposal according to deterministic rules.

### Settlement

Display the final state, exact consequence, receipt, target post-state, and all linked transaction hashes.

## Non-goals

No universal safety guarantee, no professional legal/medical advice, no private-key generation, no hidden mock mode in live mode, and no free-form model output directly controlling funds or authority.

## Acceptance criteria

1. A new user understands the protected action before connecting a wallet.
2. A malicious fixture is visibly rejected for a specific stable reason.
3. A successful fixture reaches confirmed finality and proves the target state.
4. Refreshing during consensus does not lose the proposal.
5. Every consequential action has a review screen and explicit wallet confirmation.
