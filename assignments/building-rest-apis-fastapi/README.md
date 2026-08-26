# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with Python and FastAPI. Practice defining routes, validating request data, returning JSON responses, and testing API behavior with automatically generated documentation.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Set up a FastAPI application that manages a collection of books. Define the data structure for a book and create routes for reading the collection and retrieving one book by its ID.

#### Requirements

Completed program should:

- Create a FastAPI application that can be started with a development server.
- Store at least three books with an ID, title, author, and publication year.
- Provide a `GET /books` route that returns all books as JSON.
- Provide a `GET /books/{book_id}` route that returns one matching book.
- Return an appropriate error response when the requested book does not exist.


### 🛠️ Add Book Creation and Validation

#### Description

Extend the API with a route for adding books. Use a Pydantic model to validate incoming JSON data and return a clear response when the request is invalid.

#### Requirements

Completed program should:

- Define a request model with required title and author fields.
- Validate that the publication year is a valid integer.
- Provide a `POST /books` route that accepts a JSON request body.
- Assign a unique ID to each new book and return the created book as JSON.
- Return a successful HTTP status for a valid book and a validation error for invalid data.
- Make the routes visible and testable through FastAPI's interactive documentation at `/docs`.