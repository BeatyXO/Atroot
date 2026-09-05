import { createAccount, createClient } from 'genlayer-js';
import { chain, chainName, contractAddress, rpcEndpoint } from './config';

export function createReadClient() {
  return createClient({ chain, endpoint: rpcEndpoint, account: createAccount() });
}

export async function createInjectedClient(address: string) {
  const client = createClient({ chain, endpoint: rpcEndpoint, account: address as `0x${string}` });
  await client.connect(chainName);
  return client;
}

export async function readContract(functionName: string, args: unknown[] = []) {
  if (!contractAddress) throw new Error('ATROOT contract address is not configured.');
  return createReadClient().readContract({ address: contractAddress as `0x${string}`, functionName, args: args as any[] });
}
