from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Job, Base
from app.scraper import scrape_jobs

Base.metadata.create_all(bind=engine)

app = FastAPI(title="WorkBoard API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Job Scraper API running"}

@app.post("/scrape")
def scrape_and_store(db: Session = Depends(get_db)):
    jobs = scrape_jobs()

    db.query(Job).delete()

    for job in jobs:
        db.add(Job(**job))

    db.commit()
    return {"message": "Jobs scraped & stored", "count": len(jobs)}

@app.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@app.get("/jobs/search")
def search_jobs(location: str, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.location.contains(location)).all()
