from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import notes, tags
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartNotes API",
    description="Backend API for SmartNotes application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes.router)
app.include_router(tags.router)

@app.get("/")
def health_check():
    return {"message": "Healthy"}
