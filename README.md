# AgentRoot

## Product

An agent requests a privileged action such as changing permissions, moving treasury funds, deploying code, or publishing a release. The contract checks the action against a versioned authority charter, requires semantic validator approval, executes only hash-bound calldata, then confirms the real post-action state.

This is a GenLayer-native protocol, not a backend workflow. Off-chain preparation may collect and display evidence, but the contract owns the lifecycle and only deterministic settlement becomes canonical.

## Why GenLayer is essential

Charter interpretation and code/config risk are nondeterministic; roles, hashes, limits, windows, nonce, target, calldata, and post-state confirmation are deterministic. The implementation must make this boundary visible in code, tests, and UI. A normal EVM contract can bind bytes and enforce roles; it cannot independently interpret the meaning of arbitrary source, policy, evidence, or behavior.

## Existing-work exclusion

AgentRoot is not RootGuard: it governs many heterogeneous agent actions under a capability charter, not one upgrade controller.|one mock target, one agent, native GEN fee only, code/config URL evidence, successful and malicious proposals| It must not become a betting app, grant reviewer, quote verifier, appeal court, creative lineage app, or generic AI dashboard.

## Stack lock

Next.js App Router + TypeScript; genlayer-js@1.1.8; injected EIP-1193 wallet only; Studionet chain ID 61999; RPC https://studio.genlayer.com/api; Python Intelligent Contract; no server signer and no canonical backend database.

## Lifecycle

Agent owner publishes charter; agent proposes action; validators inspect action and sources; one bounded challenge window opens; exact bytes queue; target state is read back; only confirmed execution becomes final.

## Security invariants

Agent can never widen its own authority; proposal bytes cannot change between review and execution; failed confirmation cannot mark success; replayed nonce is rejected.

## Vector Store

Use GenLayer's typed Vector Store for scoped retrieval of policies, source excerpts, manifests, prior decisions, and evidence. Store record ID, kind, source reference, digest, embedding model/version, and bounded excerpt. Retrieval informs the evaluator; similarity alone never authorizes an action.

## MVP proof


