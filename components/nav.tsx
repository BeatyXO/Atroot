'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Shield, Wallet } from 'lucide-react';
export default function Nav(){const path=usePathname();return <header><Link href="/" className="brand"><span className="mark"><Shield size={19}/></span><span>ATROOT</span><small>COMMAND FIREWALL</small></Link><nav><Link className={path==='/'?'active':''} href="/">Operations</Link><Link className={path.startsWith('/audit')?'active':''} href="/audit">Audit</Link><Link className={path.startsWith('/settings')?'active':''} href="/settings">Settings</Link></nav><Link className="wallet-btn" href="/settings"><Wallet size={16}/> Wallet</Link></header>}
