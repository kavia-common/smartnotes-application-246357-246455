from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Tag Schemas ---
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True

# --- Note Schemas ---
class NoteBase(BaseModel):
    title: str
    content: str
    is_pinned: Optional[bool] = False
    is_favorite: Optional[bool] = False

class NoteCreate(NoteBase):
    tags: List[str] = []  # List of tag names to associate

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_pinned: Optional[bool] = None
    is_favorite: Optional[bool] = None
    tags: Optional[List[str]] = None

class Note(NoteBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tags: List[Tag] = []

    class Config:
        from_attributes = True
