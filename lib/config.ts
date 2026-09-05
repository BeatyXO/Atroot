import { studionet, localnet, testnetAsimov, testnetBradbury } from 'genlayer-js/chains';

const chains = { studionet, localnet, testnetAsimov, testnetBradbury } as const;
export const chainName = (process.env.NEXT_PUBLIC_GENLAYER_CHAIN ?? 'studionet') as keyof typeof chains;
export const chain = chains[chainName] ?? studionet;
export const contractAddress = process.env.NEXT_PUBLIC_ATROOT_CONTRACT_ADDRESS ?? '';
export const rpcEndpoint = process.env.NEXT_PUBLIC_GENLAYER_RPC ?? 'https://studio.genlayer.com/api';
export const explorerBase = 'https://explorer-studio.genlayer.com';
