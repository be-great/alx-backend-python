# Type Annotations in Python 3

Type annotations allow you to specify the expected data types for function parameters, return values, and variables. Python is dynamically typed, but with type hints (introduced in Python 3.5), you can add a layer of optional static typing.

-  Even if there is a type mismatch, Python code will still run normally because Python’s type annotations are not enforced at runtime. They are purely for documentation and static type checking tools like mypy
```python
def add (a: int,  b: int) -> int:
    return a + b
```

## annotating variables
```python
name: str = "Alice"
age: int = 25
items: List[str] = ["dfds","df"]
```

## Duck Typing
- "If it walks like a duck and quacks like a duck, it's a duck."
- instead of checking the type of an object, you check whether it behaves like a certain type.
## validating Code with mypy
If there are any type mismatches, mypy will report them.
```bash
pip install mypy
mypy main.py
```