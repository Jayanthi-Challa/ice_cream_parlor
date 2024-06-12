from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, init_db
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion, Allergen

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/seasonal_flavors/")
def read_seasonal_flavors(db: Session = Depends(get_db)):
    return db.query(SeasonalFlavor).all()

@app.post("/seasonal_flavors/")
def create_seasonal_flavor(name: str, db: Session = Depends(get_db)):
    db_flavor = SeasonalFlavor(name=name)
    db.add(db_flavor)
    db.commit()
    db.refresh(db_flavor)
    return db_flavor

# Similar endpoints can be created for ingredients, customer suggestions, and allergens
