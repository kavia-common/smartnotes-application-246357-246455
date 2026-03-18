'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Home, Plus, Tag, Settings, Star } from 'lucide-react';
import { cn } from '@/lib/utils';

export default function Sidebar() {
  const pathname = usePathname();

  const links = [
    { href: '/', label: 'All Notes', icon: Home },
    { href: '/favorites', label: 'Favorites', icon: Star },
    // { href: '/tags', label: 'Tags', icon: Tag },
  ];

  return (
    <div className="flex flex-col h-screen w-64 bg-amber-50 border-r border-amber-200 text-amber-900 font-serif">
      <div className="p-6">
        <h1 className="text-2xl font-bold tracking-tight">SmartNotes</h1>
      </div>
      
      <nav className="flex-1 px-4 space-y-2">
        <Link 
          href="/create"
          className={cn(
            "flex items-center gap-3 px-4 py-3 rounded-lg transition-colors mb-6",
            "bg-amber-900 text-amber-50 hover:bg-amber-800 shadow-sm"
          )}
        >
          <Plus size={20} />
          <span>New Note</span>
        </Link>

        {links.map((link) => {
          const Icon = link.icon;
          const isActive = pathname === link.href;
          return (
            <Link
              key={link.href}
              href={link.href}
              className={cn(
                "flex items-center gap-3 px-4 py-2 rounded-lg transition-colors",
                isActive 
                  ? "bg-amber-200 text-amber-900 font-medium" 
                  : "hover:bg-amber-100/50"
              )}
            >
              <Icon size={18} />
              <span>{link.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="p-4 border-t border-amber-200">
        <div className="text-xs text-amber-700/60 text-center">
          Retro Theme v1.0
        </div>
      </div>
    </div>
  );
}
