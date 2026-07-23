
## Navigation

- ← [Back to Main README](../README.md)

## Table of Contents

- [Introduction](#introduction)
- [What is a Class?](#what-is-a-class)
- [Objects and Instances](#objects-and-instances)
- [Attributes](#attributes)
- [Methods](#methods)
- [The `__init__()` Method](#the-__init__-method)
- [The `self` Parameter](#the-self-parameter)
- [Default Parameters](#default-parameters)
- [Encapsulation and Information Hiding](#encapsulation-and-information-hiding)
- [Getters and Setters](#getters-and-setters)
- [Properties](#properties)
- [Key Points](#key-points)

## Introduction

Until now we've created programs using functions, loops and variables.

Object-Oriented Programming (OOP) allows us to combine **data** and the **functions that operate on that data** into a single object.

The blueprint for creating objects is called a **class**.

## What is a Class?

A class defines a new data type.

Think of it like a blueprint for creating objects.

```python
class Rectangle:
    pass
```

At the moment the class does nothing, but it allows us to create Rectangle objects.

## Objects and Instances

An object is an **instance** of a class.

```python
class Rectangle:
    pass

r = Rectangle()
p = Rectangle()
```

Both `r` and `p` are different Rectangle objects.

Each object stores its own data independently.

## Attributes

Attributes store the state (data) of an object.

Without using `__init__()` we can create attributes manually.

```python
class Rectangle:
    pass

r = Rectangle()

r.x = 0
r.y = 0
r.w = 2
r.l = 4
```

We can access them using dot notation.

```python
print(r.x)
print(r.w)
```

Output

```
0
2
```

### Problem

Nothing forces every Rectangle to have the same attributes.

```python
p = Rectangle()

p.x = 1
p.y = 2
p.w = 3
p.h = 5
```

Notice we accidentally used `h` instead of `l`.

Later code expecting `l` will fail.

This is why constructors exist.

## Methods

A method is simply a function that belongs to a class.

Example without methods:

```python
def area_rectangle(rect):
    return rect.w * rect.l
```

Usage

```python
print(area_rectangle(r))
```

Methods place this behaviour inside the class itself.

## The `__init__()` Method

`__init__()` is called automatically whenever an object is created.

Its job is to initialise the object's attributes.

```python
class Rectangle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 1
        self.l = 1
```

Now every Rectangle automatically has these attributes.

```python
r = Rectangle()

print(r.w)
```

Output

```
1
```

## Passing Parameters

Instead of always creating the same rectangle, we can pass values.

```python
class Rectangle:

    def __init__(self, x, y, width, length):
        self.x = x
        self.y = y
        self.w = width
        self.l = length
```

Creating rectangles becomes much easier.

```python
r = Rectangle(0, 0, 4, 6)

print(r.w)
```

Output

```
4
```

## Default Parameters

Constructors can also have default values.

```python
class Rectangle:

    def __init__(self, x=0, y=0, width=1, length=1):
        self.x = x
        self.y = y
        self.w = width
        self.l = length
```

Now both of these work.

```python
r = Rectangle()

p = Rectangle(2, 3, 5, 8)
```

## The `self` Parameter

Every method has `self` as its first parameter.

`self` refers to the object calling the method.

Example

```python
class Rectangle:

    def __init__(self, width, length):
        self.w = width
        self.l = length

    def area(self):
        return self.w * self.l
```

Calling the method

```python
r = Rectangle(3, 4)

print(r.area())
```

Output

```
12
```

Python secretly converts

```python
r.area()
```

into

```python
Rectangle.area(r)
```

The object itself becomes the `self` parameter.

## Encapsulation and Information Hiding

Objects should protect their internal data.

Instead of allowing anyone to change attributes directly, we hide implementation details.

Python uses a naming convention.

Protected attributes begin with an underscore.

```python
class Rectangle:

    def __init__(self, width, length):
        self._w = width
        self._l = length
```

This tells other programmers:

> "Don't access these directly."

Python does not enforce this rule, but it is an important convention.

## Validating Data

Constructors should reject invalid values.

```python
class Rectangle:

    def __init__(self, width, length):

        if width <= 0:
            raise ValueError("Width must be positive")

        if length <= 0:
            raise ValueError("Length must be positive")

        self._w = width
        self._l = length
```

Now invalid rectangles cannot be created.

```python
Rectangle(-5, 10)
```

Raises

```
ValueError
```

## Getters and Setters

A getter returns a value.

```python
def get_width(self):
    return self._w
```

A setter changes a value safely.

```python
def set_width(self, width):

    if width <= 0:
        raise ValueError("Width must be positive")

    self._w = width
```

Usage

```python
r.set_width(5)

print(r.get_width())
```

## Properties

Python provides a cleaner way using properties.

Getter

```python
@property
def width(self):
    return self._w
```

Setter

```python
@width.setter
def width(self, value):

    if value <= 0:
        raise ValueError("Width must be positive")

    self._w = value
```

Usage looks like a normal attribute.

```python
r.width = 8

print(r.width)
```

Instead of

```python
r.set_width(8)

print(r.get_width())
```

Properties make code easier to read while still validating data.

## Methods vs Properties

Use a **property** when accessing data.

```python
print(r.width)
```

Use a **method** when performing an action.

```python
print(r.area())
```

Rule of thumb:

- Properties represent an object's **state**.
- Methods represent an object's **behaviour**.
