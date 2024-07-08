from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    year_published: int
    summary: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        from_attributes = True  # Updated for Pydantic V2

class ReviewBase(BaseModel):
    user_id: int
    review_text: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int
    class Config:
        from_attributes = True  # Updated for Pydantic V2

class SummaryRequest(BaseModel):
    content: str

class User(BaseModel):
    username: str
