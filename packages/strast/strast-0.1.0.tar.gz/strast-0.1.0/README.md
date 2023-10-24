# Strast

Strast is a versatile Python tool that transforms a string representation of a Python literal into the corresponding Python object, building upon the powerful [ast](https://docs.python.org/3/library/ast.html) module. The word "strast" also denotes "passion", reflecting our enthusiasm for data transformation. 

## Features
- Transform string literals to Python objects seamlessly with the power of the `ast` module.
- Flexible type checking to ensure data integrity.
- Supports extensibility through factory and class-based approaches.

## Installation
To install Strast, use pip:

```bash
pip install strast
```

## Usage
```python
import strast
```
### Function
`strast`s core function:
```python
result = strast.c("{'a': 1, 'b': 2}", dict) # or strast.core.strast
print(result)
print(strast("{'a': 1, 'b': 2}", list))
```
Output:
```
{'a': 1, 'b': 2}
TypeError: Expected <class 'list'>, got <class 'dict'> instead.
```

### Factory
`strast` as a closure factory function:
```python
strast = strast.f(dict, list, tuple) # or strast.factory.strast
print(strast("{'a': 1, 'b': 2}"))
print(strast("[1, 2, 3]"))
print(strast("('a', 'b', 'c')"))
```
Output:
```
{'a': 1, 'b': 2}
[1, 2, 3]
('a', 'b', 'c')
```

### Class-based
`strast` as a class:
```python
strast = strast.S(dict) # or strast.class_based.Strast
print(strast.transform("{'a': 1, 'b': 2}"))
```
Output:
```
{'a': 1, 'b': 2}
```
See also [documentation](https://janthmueller.github.io/strast/docs/strast.html)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
Strast is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

