/** GenLayer success means both consensus finality and successful VM execution. */
export function isSuccessful(receipt: any): boolean {
  const status = String(receipt?.statusName ?? receipt?.status_name ?? '').toUpperCase();
  const consensus = String(receipt?.resultName ?? receipt?.result_name ?? '').toUpperCase();
  const execution = String(receipt?.txExecutionResultName ?? receipt?.tx_execution_result_name ?? receipt?.execution_result ?? '').toUpperCase();
  const statusOk = status === 'ACCEPTED' || status === 'FINALIZED';
  const consensusOk = !consensus || consensus === 'MAJORITY_AGREE';
  const executionOk = !execution || execution === 'SUCCESS';
  return statusOk && consensusOk && executionOk;
}
