# FastAPI Mini Project 🚀

This is a simple FastAPI-based backend project that includes multiple endpoints. The application supports arithmetic operations, palindrome checking, and task management via in-memory storage.

---

## 📂 Project Structure
FastApi_APP/
```
├── main.py
├──pyproject.toml # Poetry configuration
├── poetry.lock # Dependency lock file
├── README.md # Project info and usage (You're looking at it!📘)
└── LICENSE
```

---

## 📦 Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (for running the app)
- [Pydantic](https://docs.pydantic.dev/)

---

## 📦 Installation

Install all dependencies using:

```bash
poetry install
```

Or manually with:

```bash
pip install fastapi uvicorn pydantic
```


---

## 🚀 How to Run

Start the server with:

```bash
poetry run uvicorn main:app --reload
```

Then open your browser at:

```
http://127.0.0.1:8000/docs
```

> This will launch the Swagger UI — an interactive documentation for testing the API endpoints.

---

## 🧪 Endpoints

### 🔹 Root Endpoint

- **GET** `/`  
Returns a simple welcome message.

---

### 🔹 Add Two Numbers

- **GET** `/add/{a}/{b}`  
Returns the sum of two numeric values.

**Example:**  
`/add/3/5` → `a = 3, b = 5, a + b = 8`

---

### 🔹 Palindrome Checker

- **GET** `/pal/{word}`  
Checks whether a given word is a palindrome.

**Example:**  
`/pal/radar` → `"The word is a palindrome"`  
`/pal/hello` → `"The word is not a palindrome"`

---

### 🔹 Create a Task

- **POST** `/task/`  
Creates a task with a `title` and optional `description`.

**JSON Body Example:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs"
}
```

**Response:**
```
Task received and stored: ...
```

---

### 🔹 Get a Task by Title

- **GET** `/task/{title}`  
Searches for a task by its title (case-insensitive).

**Example:**  
`/task/Buy groceries` → returns the stored task

If not found, returns:
```
404: Task not found
```

---

## ⚠️ Notes

- Tasks are stored **in-memory** — meaning they will be lost when the server restarts.
- Error handling is included for invalid numeric input and missing tasks.

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---
