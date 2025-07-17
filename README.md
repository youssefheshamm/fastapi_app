# 🚀 FastAPI Utility App

A simple FastAPI project that provides two main functionalities:

- 🔢 **Addition**: Add two numbers
- 🔁 **Palindrome Checker**: Check if a word is a palindrome

---

## 📂 Project Structure
FastApi_APP/
```
├── main.py
├──pyproject.toml # Poetry configuration
├── poetry.lock # Dependency lock file
├── README.md # Project info and usage
└── LICENSE
```

---

## ⚙️ Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)
- Git (optional, for cloning)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/youssefheshamm/FastApi_APP.git
   ```
1. **Move into the project folder:**
   ```bash
   cd FastApi_APP
   ```
3. **Install dependencies using Poetry:**
   ```bash
    poetry install
4. **Run the server:**
   ```bash
    poetry run uvicorn main:app --reload
   ```
   OR
   ```bash
    poetry run uvicorn main:app --reload --port 8000
   ```
   
## Once the server is running, you'll see something like:
```bash
  Uvicorn running on http://127.0.0.1:8000
```
Open that link (here it's ```http://127.0.0.1:8000```) in your browser or by using a tool like Postman/Insomnia to access the root endpoint (/), which welcomes you to the API.

### You can also test the endpoints:

➕ Add Endpoint
URL:  `http://127.0.0.1:8000/add/4/5`

Returns the sum of `a = 4` and `b = 5`

Result: `["a = 4, b = 5, a + b = 9 "]`

🔁 Palindrome Checker
URL:  `http://127.0.0.1:8000/pal/radar`

Returns if the word is `a palindrome` or `not a palindrome`

Result: `["The word is a palindrome"]`

Try different words like:

`/pal/hello` → `["The word is not a palindrome"]`

`/pal/9` → `["this is not a word"]`

---

## 🔍 API Endpoints

### ➕ `GET /add/{a}/{b}`

Adds two numbers and returns the result.

```bash
/add/4/5
→ { "a = 4, b = 5, a + b = 9" }

# If inputs are not numeric
/add/a/b
→ { "ERROR: both inputs must be numeric values" }
```
### 🔁 `GET /pal/{word}`

Checks if a word is a palindrome (case-insensitive). Ignores numbers
```bash
/pal/radar
→ { "The word is a palindrome" }

/pal/hello
→ { "The word is not a palindrome" }

# If input is not a word
/pal/9
→ { "this is not a word" }

# If input is only one letter
/pal/i
→ { "The word is too short" }
```



