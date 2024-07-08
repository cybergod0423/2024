from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Book, Review
from .schemas import BookCreate, BookUpdate, ReviewCreate

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Book).offset(skip).limit(limit))
    return result.scalars().all()

async def get_book_by_id(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    return result.scalars().first()

async def create_new_book(db: AsyncSession, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def update_existing_book(db: AsyncSession, db_book: Book, book: BookUpdate):
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def delete_existing_book(db: AsyncSession, book: Book):
    await db.delete(book)
    await db.commit()

async def create_new_review(db: AsyncSession, book_id: int, review: ReviewCreate):
    db_review = Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_reviews_by_book_id(db: AsyncSession, book_id: int):
    result = await db.execute(select(Review).where(Review.book_id == book_id))
    return result.scalars().all()
