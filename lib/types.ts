export type Proposal = { proposal_id:number; proposer:string; title:string; target:string; action_hash:string; intent:string; charter_version:string; status:number; confidence_band:number; rationale:string; created_at:number };
export const statusName = (status:number) => ['EMPTY','REVIEWING','APPROVED','REJECTED','ABSTAINED'][status] ?? 'UNKNOWN';
