'use client';

import { useEffect, useState } from 'react';
import { Search } from 'lucide-react';
import api from '@/lib/api';
import { Note } from '@/types';
import NoteCard from '@/components/NoteCard';

export default function Home() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchNotes();
  }, [search]);

  const fetchNotes = async () => {
    try {
      const response = await api.get('/notes', {
        params: { search: search || undefined }
      });
      setNotes(response.data);
    } catch (error) {
      console.error('Failed to fetch notes:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-8 max-w-7xl mx-auto">
      <header className="mb-8 flex items-center justify-between">
        <div>
          <h2 className="text-3xl font-bold text-gray-900 mb-2">My Notes</h2>
          <p className="text-gray-500">Capture your thoughts in style.</p>
        </div>
        
        <div className="relative w-96">
          <input
            type="text"
            placeholder="Search notes..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-10 pr-4 py-2 bg-white border border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-200 focus:border-amber-400 transition-all font-serif"
          />
          <Search className="absolute left-3 top-2.5 text-gray-400" size={18} />
        </div>
      </header>

      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3].map((n) => (
            <div key={n} className="h-48 bg-gray-100/50 rounded-xl animate-pulse" />
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {notes.map((note) => (
            <NoteCard key={note.id} note={note} />
          ))}
          {notes.length === 0 && (
            <div className="col-span-full text-center py-20 text-gray-400 font-serif italic">
              No notes found. Create one to get started!
            </div>
          )}
        </div>
      )}
    </div>
  );
}
