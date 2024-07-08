from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .database import SessionLocal, init_db
from .models import Book as BookModel, Review as ReviewModel
from .crud import (
    get_books,
    get_book_by_id,
    create_new_book,
    update_existing_book,
    delete_existing_book,
    create_new_review,
    get_reviews_by_book_id,
)
from .security import get_current_user

from .schemas import BookCreate, BookUpdate, ReviewCreate, SummaryRequest, User, Book, Review

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/books", response_model=Book)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    return await create_new_book(db=db, book=book)

@app.get("/books", response_model=List[Book])
async def read_books(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    return await get_books(db=db, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    book = await get_book_by_id(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    db_book = await get_book_by_id(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return await update_existing_book(db=db, db_book=db_book, book=book)

@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    db_book = await get_book_by_id(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    await delete_existing_book(db=db, book=db_book)
    return {"message": "Book deleted successfully"}

@app.post("/books/{book_id}/reviews", response_model=Review)
async def create_review(book_id: int, review: ReviewCreate, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    return await create_new_review(db=db, book_id=book_id, review=review)

@app.get("/books/{book_id}/reviews", response_model=List[Review])
async def read_reviews(book_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    return await get_reviews_by_book_id(db=db, book_id=book_id)

@app.get("/books/{book_id}/summary")
async def get_book_summary(book_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    # Logic to fetch summary and aggregated rating for the book
    book = await get_book_by_id(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Placeholder logic for summary calculation (adjust as per your application's logic)
    summary = {
        "book_id": book.id,
        "title": book.title,
        "summary": "This is a summary of the book.",
        "average_rating": 4.5
    }
    
    return summary

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)