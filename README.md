# ATROOT

ATROOT is a GenLayer command-firewall prototype for one bounded protected target: a release/version state transition. The owner publishes an immutable charter and registers agents. A registered agent submits an exact target, method, release, agent nonce, target execution nonce, and frozen HTTPS evidence digest. GenLayer validators adjudicate the evidence semantically. Approved proposals enter a contract-enforced challenge window, then may be queued, executed through the protected target, and confirmed against target post-state.

## Current implementation

- `contracts/atroot_firewall_v2.py`: owner, charters, agents, nonces, action commitments, evidence digest checks, semantic review, challenge adjudication, queue, execution-pending, and post-state confirmation.
- `contracts/protected_target.py`: owner-bound target that accepts `apply_release` only from the ATROOT address, enforces a monotonic target release nonce, and rejects consumed proposal keys.
- Next.js frontend: operations, audit, proposal detail, wallet, and authority setup pages.

## Fresh StudioNet deployment

Chain ID: `61999`  
RPC: `https://studio.genlayer.com/api`

Firewall: `0x189332008A6a989ba68F5f049A638Ecca19944cd`  
Protected target: `0x3F0722f27045EfD5dE32503D06a93288Fa141a0d`

Final target deployment transaction was not captured by the CLI output. Final firewall deployment transaction: `0x2add30f9d3db28062d234a10a8296bb98f68b835cae5549c69a5434801749a50`. `bind_firewall` finalized with `MAJORITY_AGREE`; target readback confirmed the final firewall address. The target and bind transaction hashes must be recovered from the StudioNet explorer/receipt before final submission.

## Verification status

Automated source/security tests pass for action binding, evidence digest checks, registration protection, target authorization/replay checks, and challenge adjudication structure. TypeScript/build verification is in progress for this revision.

The fresh live semantic review currently finalized `MAJORITY_DISAGREE` and therefore remained non-executable. A complete live `APPROVE → EXECUTED` lifecycle, emitted-child receipt tracking, and the full malicious/replay/challenge matrix are not yet proven. Do not describe the current deployment as submission-ready or change Vercel to it until those scenarios pass.

## Limitations

The frontend and deployment helpers still need final integration verification for emitted child transaction receipts. GenLayer direct-mode tests require a runtime artifact matching the contract's pinned `py-genlayer` version; the installed runner currently fails during its calldata bootstrap, so those tests are documented as blocked rather than falsely marked green. Vector Store is not claimed as shipped.

## Local checks

```text
python -m unittest discover -s tests -v
pytest tests/test_v2_direct.py -q
npx tsc --noEmit --pretty false --incremental false
```
