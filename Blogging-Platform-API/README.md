# Blogging Platform API

---
A simple REST API for a blogging platform built with FastAPI and PostgreSQL.

## Requirements

---

- Python 3.14
- UV
- PostgreSQL

## Installation

---
1. Clone Repo
```commandline
git clone https://github.com/dfnc1/Mini-Project-Python.git
cd ./Mini-Project-Python/Blogging-Platform-API/
```
2. Install Depedencies 
```commandline
uv sync
```
3. Activate Virtual Environment
```commandline
source .venv/bin/activate
```
4. Create `.env` file and add this line
```dotenv
DB_URL="postgresql://username:password@localhost:port/db-name"
```
5. Run App
```commandline
uvicorn main:app --reload
```

## Endpoints

| Method | Endpoint      | Description       |
|--------|---------------|-------------------|
| GET    | /posts        | Get all posts     |
| GET    | /posts/{id}   | Get post by ID    |
| POST   | /posts        | Create a new post |
| PUT    | /posts/{id}   | Update a post     |
| DELETE | /posts/{id}   | Delete a post     |

## API Documentation

Once the server is running, open:

http://127.0.0.1:8000/docs