# Dunder (Magic) Methods

## Navigation

- ← [Back to Main README](../README.md)

## Table of Contents

- [Overview](#overview)
- [What are Dunder Methods?](#what-are-dunder-methods)
- [The `__init__()` Method](#the-__init__-method)
- [The `__str__()` Method](#the-__str__-method)
- [The `__repr__()` Method](#the-__repr__-method)
- [Comparison Methods](#comparison-methods)
- [Arithmetic Methods](#arithmetic-methods)
- [Container Methods](#container-methods)
- [Common Dunder Methods](#common-dunder-methods)
- [Key Points](#key-points)

## Overview

Dunder methods (short for **double underscore methods**) are special methods built into Python.

They allow your own classes to behave like Python's built-in objects.

Examples include:

- Creating objects
- Printing objects
- Comparing objects
- Adding objects together
- Using `len()`
- Using indexing (`[]`)

They are called automatically by Python.

## What are Dunder Methods?

A dunder method starts and ends with two underscores.

```python
__init__
__str__
__len__
__eq__
```

You should **not** call these methods directly.

Instead, Python calls them for you.

For example:

```python
print(rectangle)
```

actually calls

```python
rectangle.__str__()
```

behind the scenes.

## The `__init__()` Method

`__init__()` initialises a newly created object.

```python
class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length
```

Creating an object

```python
r = Rectangle(3, 4)
```

Python automatically executes

```python
r.__init__(3, 4)
```

This sets the object's initial state.

## The `__str__()` Method

Controls what is displayed when using `print()`.

Without `__str__()`

```python
class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

r = Rectangle(3, 4)

print(r)
```

Output

```
<__main__.Rectangle object at 0x10482...>
```

With `__str__()`

```python
class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __str__(self):
        return f"Rectangle({self.width}, {self.length})"
```

Output

```
Rectangle(3, 4)
```

## The `__repr__()` Method

Provides the official string representation of an object.

```python
class Rectangle:

    def __repr__(self):
        return f"Rectangle({self.width}, {self.length})"
```

Used by

```python
r
repr(r)
```

Unlike `__str__()`, `__repr__()` is mainly intended for developers.

## Comparison Methods

Objects can define how they compare with one another.

### Equality

```python
class Rectangle:

    def __eq__(self, other):
        return (
            self.width == other.width
            and self.length == other.length
        )
```

Example

```python
r1 = Rectangle(3, 4)
r2 = Rectangle(3, 4)

print(r1 == r2)
```

Output

```
True
```

### Less Than

```python
def __lt__(self, other):
    return self.width < other.width
```

Now Python understands

```python
r1 < r2
```

## Arithmetic Methods

Objects can support mathematical operators.

Addition

```python
class Counter:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Counter(self.value + other.value)
```

Example

```python
a = Counter(10)
b = Counter(5)

c = a + b

print(c.value)
```

Output

```
15
```

## Container Methods

### Length

Allows `len()` to work.

```python
class Playlist:

    def __init__(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)
```

Example

```python
playlist = Playlist()

print(len(playlist))
```

### Indexing

Allows square brackets.

```python
class Playlist:

    def __init__(self):
        self.songs = []

    def __getitem__(self, index):
        return self.songs[index]
```

Example

```python
playlist[0]
```

### Membership

Allows the `in` keyword.

```python
def __contains__(self, item):
    return item in self.songs
```

Example

```python
"Song A" in playlist
```

## Common Dunder Methods

| Method | Purpose | Example |
|----------|---------|---------|
| `__init__` | Initialise an object | `Rectangle(3, 4)` |
| `__str__` | User-friendly string | `print(rectangle)` |
| `__repr__` | Developer representation | `repr(rectangle)` |
| `__len__` | Object length | `len(obj)` |
| `__getitem__` | Indexing | `obj[0]` |
| `__setitem__` | Assign by index | `obj[0] = x` |
| `__contains__` | Membership test | `x in obj` |
| `__eq__` | Equality | `a == b` |
| `__lt__` | Less than | `a < b` |
| `__gt__` | Greater than | `a > b` |
| `__add__` | Addition | `a + b` |
| `__sub__` | Subtraction | `a - b` |
| `__mul__` | Multiplication | `a * b` |

## When are Dunder Methods Called?

You rarely call them yourself.

Python calls them automatically.

| You write | Python calls |
|-----------|--------------|
| `Rectangle()` | `__init__()` |
| `print(obj)` | `__str__()` |
| `repr(obj)` | `__repr__()` |
| `len(obj)` | `__len__()` |
| `obj[0]` | `__getitem__()` |
| `obj[0] = 5` | `__setitem__()` |
| `x in obj` | `__contains__()` |
| `a == b` | `__eq__()` |
| `a < b` | `__lt__()` |
| `a + b` | `__add__()` |
