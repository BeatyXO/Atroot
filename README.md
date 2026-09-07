# ATROOT

ATROOT is a GenLayer command-firewall prototype for one bounded protected target: a release/version state transition. The owner publishes an immutable charter and registers agents. A registered agent submits an exact target, method, release, agent nonce, target execution nonce, and frozen HTTPS evidence digest. GenLayer validators adjudicate the evidence semantically. Approved proposals enter a contract-enforced challenge window, then may be queued, executed through the protected target, and confirmed against target post-state.

## Current implementation

- `contracts/atroot_firewall_v2.py`: owner, charters, agents, nonces, action commitments, evidence digest checks, semantic review, challenge adjudication, queue, execution-pending, and post-state confirmation.
- `contracts/protected_target.py`: owner-bound target that accepts `apply_release` only from the ATROOT address, enforces a monotonic target release nonce, and rejects consumed proposal keys.
- Next.js frontend: operations, audit, proposal detail, wallet, and authority setup pages.

## Fresh StudioNet deployment

Chain ID: `61999`  
RPC: `https://studio.genlayer.com/api`

Firewall: `0x1a1490d4BafA65e6C9e412542f46362eE633E056`  
Protected target: `0x62Ec9747b9bC07a74791d233C1bEb8Bd3a5794D8`

Final target deployment transaction: `0x4d228c88a03add250114a1ffc9c21c642e16d9c4b7d5187f5dc10c356f117270`. Final firewall deployment transaction: `0x3b4505b8e4175136cb9be8a5b8cd3445d600a9ba9e90ebe0672e3e33a2e06411`. `bind_firewall` transaction: `0x33a441dfa33c5d5bddf36dac298111a6b88f22b0711b9522e4c6b4ace05c5d72`, finalized `MAJORITY_AGREE`; target readback confirmed the final firewall address.

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
