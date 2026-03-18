from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def get_notes(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    search: Optional[str] = None,
    tag: Optional[str] = None,
    is_pinned: Optional[bool] = None,
    is_favorite: Optional[bool] = None
):
    query = db.query(models.Note)

    if search:
        query = query.filter(
            (models.Note.title.ilike(f"%{search}%")) | 
            (models.Note.content.ilike(f"%{search}%"))
        )
    
    if is_pinned is not None:
        query = query.filter(models.Note.is_pinned == is_pinned)
        
    if is_favorite is not None:
        query = query.filter(models.Note.is_favorite == is_favorite)

    if tag:
        query = query.join(models.Note.tags).filter(models.Tag.name == tag)

    # Order by pinned first, then updated_at desc
    query = query.order_by(models.Note.is_pinned.desc(), models.Note.updated_at.desc().nulls_last())
    
    return query.offset(skip).limit(limit).all()

def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(
        title=note.title,
        content=note.content,
        is_pinned=note.is_pinned,
        is_favorite=note.is_favorite
    )
    
    # Handle tags
    for tag_name in note.tags:
        tag = get_tag_by_name(db, tag_name)
        if not tag:
            tag = create_tag(db, schemas.TagCreate(name=tag_name))
        db_note.tags.append(tag)
        
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, note_update: schemas.NoteUpdate):
    db_note = get_note(db, note_id)
    if not db_note:
        return None
    
    update_data = note_update.model_dump(exclude_unset=True)
    
    # Handle tags separately if present
    if 'tags' in update_data:
        tags_data = update_data.pop('tags')
        db_note.tags = [] # Clear existing tags
        for tag_name in tags_data:
            tag = get_tag_by_name(db, tag_name)
            if not tag:
                tag = create_tag(db, schemas.TagCreate(name=tag_name))
            db_note.tags.append(tag)
            
    for key, value in update_data.items():
        setattr(db_note, key, value)
        
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note

def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tag_by_name(db: Session, name: str):
    return db.query(models.Tag).filter(models.Tag.name == name).first()

def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()

def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
