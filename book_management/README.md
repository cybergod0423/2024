# Intelligent Book Management System

## Project Overview

This project is an intelligent book management system using FastAPI, PostgreSQL, and a locally running Llama3 generative AI model, deployed on AWS. The system allows users to add, retrieve, update, and delete books from a PostgreSQL database, generate summaries for books, and provide book recommendations based on user preferences. The system also manages user reviews and generates rating and review summaries for books.

## Features

- **Database Setup**: PostgreSQL to store book information.
- **RESTful API**: FastAPI for handling CRUD operations and other endpoints.
- **Asynchronous Programming**: Async operations for database interactions.

## Create Dockeized Postgres DB
Run PostgreSQL Docker Container: Run a PostgreSQL container named book_management_db on the book_management_network network with the following command:
```docker run -d --name book_management_db --network book_management_network -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=book_management_db -p 5432:5432 postgres:latest```

## Using the FastAPI Application
Start the FastAPI Application: Ensure that your FastAPI application (main.py) is running. You can start it using a command like:

`uvicorn app.main:app --reload`

Replace main with the filename of your FastAPI application if it's named differently.
Accessing the API Endpoints: Once the FastAPI application is running, you can interact with it using tools like curl, Postman, or directly from a web browser.

```Available API Endpoints:
Books API:
GET /books: Retrieve all books.
GET /books/{book_id}: Retrieve a specific book by its ID.
POST /books: Add a new book.
PUT /books/{book_id}: Update a book's information by its ID.
DELETE /books/{book_id}: Delete a book by its ID.
POST /books/{book_id}/reviews: Add a review for a specific book.
GET /books/{book_id}/reviews: Retrieve all reviews for a specific book.
GET /books/{book_id}/summary: Get a summary and aggregated rating for a specific book.
```

Add a New Book:
```
curl -X POST "http://localhost:8000/books" -H "Content-Type: application/json" -H "Authorization: Basic $(echo -n 'user:password' | base64)" -d '{
    "title": "Sample Book",
    "author": "John Doe",
    "genre": "Fiction",
    "year_published": 2023,
    "summary": "This is a sample book."
}'
```

Retrieve All Books:

```
curl -X GET -H "Authorization: Basic $(echo -n 'user:password' | base64)" "http://localhost:8000/books"
```

Retrieve a Specific Book by ID:
```
curl -X GET -H "Authorization: Basic $(echo -n 'user:password' | base64)" "http://localhost:8000/books/{book_id}"
```

Update a Book by ID:
```
curl -X PUT "http://localhost:8000/books/{book_id}" -H "Authorization: Basic $(echo -n 'user:password' | base64)" -H "Content-Type: application/json" -d '{
    "title": "Updated Book Title",
    "author": "Jane Smith"
}'
```

Delete a Book by ID:
```
curl -X DELETE -H "Authorization: Basic $(echo -n 'user:password' | base64)" "http://localhost:8000/books/{book_id}"

```

Add a Review for a Book:
```
curl -X POST -H "Authorization: Basic $(echo -n 'user:password' | base64)" "http://localhost:8000/books/{book_id}/reviews" -H "Content-Type: application/json" -d '{
    "user_id": 1,
    "review_text": "Great book, highly recommended!",
    "rating": 5
}'
```


## Building Docker Image
``` docker build -t book_management_app .```

# Run Docker Container
``` docker run --network bridge --rm -it -p 8000:8000 -e DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/book_management_db book_management_app:latest```


# Deploy on Kubernetes
``` kubectl apply -f .```