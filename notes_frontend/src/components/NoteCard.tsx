import Link from 'next/link';
import { Pin, Star } from 'lucide-react';
import { format } from 'date-fns';
import { Note } from '@/types';
import { cn } from '@/lib/utils';

interface NoteCardProps {
  note: Note;
}

export default function NoteCard({ note }: NoteCardProps) {
  return (
    <Link href={`/note/${note.id}`}>
      <div className="group relative p-5 bg-white border border-amber-100 rounded-xl shadow-sm hover:shadow-md hover:border-amber-300 transition-all cursor-pointer h-full flex flex-col">
        <div className="flex justify-between items-start mb-2">
          <h3 className="font-serif text-lg font-semibold text-gray-900 line-clamp-1 group-hover:text-amber-700 transition-colors">
            {note.title || 'Untitled'}
          </h3>
          <div className="flex gap-1 text-amber-400">
            {note.is_pinned && <Pin size={16} className="fill-current" />}
            {note.is_favorite && <Star size={16} className="fill-current" />}
          </div>
        </div>
        
        <p className="text-gray-600 text-sm line-clamp-3 mb-4 flex-grow font-sans">
          {note.content}
        </p>

        <div className="flex items-center justify-between mt-auto">
          <div className="flex gap-2 flex-wrap">
            {note.tags.slice(0, 3).map(tag => (
              <span key={tag.id} className="px-2 py-0.5 bg-amber-50 text-amber-700 text-xs rounded-full border border-amber-100">
                #{tag.name}
              </span>
            ))}
          </div>
          <span className="text-xs text-gray-400">
            {note.updated_at ? format(new Date(note.updated_at), 'MMM d, yyyy') : ''}
          </span>
        </div>
      </div>
    </Link>
  );
}
