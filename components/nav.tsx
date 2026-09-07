'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useState } from 'react';
import { Shield, Wallet } from 'lucide-react';
import WalletModal from './wallet-modal';
export default function Nav(){const path=usePathname();const [open,setOpen]=useState(false);return <><header><Link href="/" className="brand"><span className="mark"><Shield size={19}/></span><span>ATROOT</span><small>COMMAND FIREWALL</small></Link><nav><Link className={path==='/'?'active':''} href="/">Operations</Link><Link className={path.startsWith('/audit')?'active':''} href="/audit">Audit</Link><Link className={path.startsWith('/settings')?'active':''} href="/settings">Settings</Link></nav><button className="wallet-btn" onClick={()=>setOpen(true)}><Wallet size={16}/> Wallet</button></header>{open&&<WalletModal onClose={()=>setOpen(false)}/>}</>}
