# AgentRoot â€” UI/UX

## Art direction

Agent command firewall: ink black, acid lime, warning red, dense command diff, authority graph, no SaaS cards.

Avoid generic AI SaaS patterns: no purple gradients, no robot art, no oversized â€œAI-poweredâ€ hero, no interchangeable rounded-card grid, and no fake validator percentage meter.

## Screen system

- **Briefing:** one sentence explaining the protected action and why semantic consensus is required.
- **Operations view:** active proposals arranged as a domain instrument (graph, rail, queue, dossier, or command board).
- **Proposal dossier:** exact target, bytes/hash, policy version, evidence, semantic matches, and lifecycle.
- **Consensus room:** pending/settled/abstained states with honest labels and bounded decision fields.
- **Execution bay:** challenge window, countdown where applicable, wallet review, receipt, and post-state confirmation.
- **Public audit:** readable event history with explorer links.

## Interaction rules

Use injected wallet only. A disconnected user can browse but cannot write. A wrong-network user gets a clear switch request. Preserve drafts locally only as non-authoritative form state. After a write, wait for the appropriate finalized/accepted receipt, refetch, and show the transaction.

## Responsive behavior

Mobile becomes a vertical incident/proposal dossier; tablet uses a collapsible evidence drawer; desktop uses the full operational canvas. All status meaning must survive without color.

## Accessibility

Keyboard-complete controls, visible focus, semantic headings, reduced motion, contrast-safe status badges, screen-reader announcements for wallet/consensus/receipt states, and copyable hashes.
