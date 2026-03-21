# Blogging Platform API

---

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
2. Install UV
```commandline
pip install uv
```
3. Install Depedencies 
```commandline
uv sync
```
4. Create .env file 
```.dotenv
DB_URL="postgresql://username:password@host:port/db-name"
```
5. Run App
```commandline
uvicorn main:app --reload
```
