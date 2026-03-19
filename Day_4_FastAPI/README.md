# Day 4: FastAPI Project

## Objective

To build and test a REST API using FastAPI and understand API development concepts.

---

## Tasks Performed

* Created project structure for FastAPI
* Set up virtual environment in WSL
* Installed FastAPI and required dependencies
* Created API file (api.py)

---

## API Endpoints

### Health Check

GET /health
Returns server status

---

### Items API

POST /items
Creates a new item

GET /items
Returns all items

GET /items/{item_id}
Returns a specific item

DELETE /items/{item_id}
Deletes an item

---

### Math API

POST /math/divide
Divides two numbers

---

## Testing

* Tested all endpoints using Swagger UI
* Verified correct responses
* Checked error handling:

  * Invalid input
  * Item not found
  * Division by zero

---

## What I Learned

I learned how APIs work and how to build them using FastAPI.
I also learned how to test APIs using Swagger UI and handle errors properly.

---

## Result

Successfully created and tested a working FastAPI application with full CRUD operations and error handling.
