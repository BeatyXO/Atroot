# ATROOT

ATROOT is a GenLayer command-firewall prototype for one bounded protected target: a release/version state transition. The owner publishes an immutable charter and registers agents. A registered agent submits an exact target, method, release, agent nonce, target execution nonce, and frozen HTTPS evidence digest. GenLayer validators adjudicate the evidence semantically. Approved proposals enter a contract-enforced challenge window, then may be queued, executed through the protected target, and confirmed against target post-state.

## Current implementation

- `contracts/atroot_firewall_v2.py`: owner, charters, agents, nonces, action commitments, evidence digest checks, semantic review, challenge adjudication, queue, execution-pending, and post-state confirmation.
- `contracts/protected_target.py`: owner-bound target that accepts `apply_release` only from the ATROOT address, enforces a monotonic target release nonce, and rejects consumed proposal keys.
- Next.js frontend: operations, audit, proposal detail, wallet, and authority setup pages.

## Fresh StudioNet deployment

Chain ID: `61999`  
RPC: `https://studio.genlayer.com/api`

Firewall: `0x07A32B82A215795A55101b821f2849C1f835Ec4C`  
Protected target: `0x8FB25Fab257942B005B6176ba607578bA73b9afC`

The final firewall deployment transaction was `0xe540200dde4ca6d834efbaf02d93e539fa7ddd920ab19e25daf67c77ddc4c768`. Binding and the required live lifecycle matrix are still pending; this address must not be placed in Vercel until those checks pass.

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
