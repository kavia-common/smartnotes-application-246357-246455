export interface Tag {
  id: number;
  name: str;
}

export interface Note {
  id: number;
  title: string;
  content: string;
  is_pinned: boolean;
  is_favorite: boolean;
  created_at: string;
  updated_at?: string;
  tags: Tag[];
}

export interface NoteCreate {
  title: string;
  content: string;
  is_pinned?: boolean;
  is_favorite?: boolean;
  tags: string[];
}

export interface NoteUpdate {
  title?: string;
  content?: string;
  is_pinned?: boolean;
  is_favorite?: boolean;
  tags?: string[];
}
