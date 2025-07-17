from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"This is the root endpoint😎"}


@app.get("/add/{a}/{b}")
def add_numbers(a, b):
    try:
        a_num = float(a)
        b_num = float(b)
        result = a_num + b_num
        if a_num.is_integer():
            a_num = int(a_num)
        if b_num.is_integer():
            b_num = int(b_num)
        if result.is_integer():
            result = int(result)
        return {f"a = {a_num}, b = {b_num}, a + b = {result} "}
    except ValueError:
        return {"ERROR: both inputs must be numeric values"}
