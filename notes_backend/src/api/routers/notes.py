from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Note, summary="Create a new note")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db=db, note=note)

@router.get("/", response_model=List[schemas.Note], summary="Get all notes with optional filters")
def read_notes(
    skip: int = 0, 
    limit: int = 100, 
    search: Optional[str] = Query(None, description="Search term for title or content"),
    tag: Optional[str] = Query(None, description="Filter by tag name"),
    is_pinned: Optional[bool] = Query(None, description="Filter by pinned status"),
    is_favorite: Optional[bool] = Query(None, description="Filter by favorite status"),
    db: Session = Depends(get_db)
):
    notes = crud.get_notes(db, skip=skip, limit=limit, search=search, tag=tag, is_pinned=is_pinned, is_favorite=is_favorite)
    return notes

@router.get("/{note_id}", response_model=schemas.Note, summary="Get a specific note")
def read_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.put("/{note_id}", response_model=schemas.Note, summary="Update a note")
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    db_note = crud.update_note(db, note_id=note_id, note_update=note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/{note_id}", response_model=schemas.Note, summary="Delete a note")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.delete_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note
