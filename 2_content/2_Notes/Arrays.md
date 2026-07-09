# Arrays

## Navigation

- ← [Back to Main README](../README.md)

## Table of Contents

- [Fixed Arrays](#1-fixed-arrays)
- [Dynamic Arrays](#2-dynamic-arrays)

## 1. Fixed Arrays

> [!info] Definition
> A **fixed array** is a contiguous block of memory whose size is determined when the array is created. Once allocated, its size **cannot be changed**.

### 1.1 Initialisation

**Time Complexity:** **O(n)**

> [!info]
> Creating an array of size **n** requires allocating memory for **n** elements.

![[../../5_Assets/Arrays_1.png]]

### 1.2 Index Access (Lookup)

**Time Complexity:** **O(1)**

> [!info]
> Arrays provide **constant-time access** to elements because each element occupies a fixed location in memory.

Given the address of the first element, the memory address of any index can be calculated directly.

![[../../5_Assets/Arrays_2.png]]

### 1.3 Searching

**Time Complexity:** **O(n)**

> [!note]
> If the value of an element is unknown, each element may need to be examined until the target is found.

> [!tip]
> Index lookup (`array[i]`) is **not** the same as searching for a value.

### 1.4 Inserting an Element

**Time Complexity:** **O(n)**

> [!warning]
> Since a fixed array has a fixed capacity, inserting a new element requires making space by shifting existing elements.

If the array is already full:

- The final element is lost (or insertion is impossible, depending on the implementation).
- Every element after the insertion point is shifted one position to the right.

![[../../5_Assets/Arrays_3.png]]

![[../../5_Assets/Arrays_4.png]]

---

### 1.5 Deleting an Element

**Time Complexity:** **O(n)**

Removing an element creates a gap.

To maintain contiguous storage, all following elements are shifted one position to the left.

## 2. Dynamic Arrays

> [!info] Definition
> A **dynamic array** automatically resizes when additional capacity is required.

Unlike fixed arrays, dynamic arrays can grow during program execution.

### 2.1 Resizing Method 1

When the array becomes full:

1. Create a new array with one additional element.
2. Copy every element into the new array.
3. Insert the new value.

![[../../5_Assets/Arrays_5.png]]

Although simple, this approach is inefficient because every resize copies the entire array.

### 2.2 Resizing Method 2 (Common Implementation)

Most programming languages increase capacity by a **growth factor** (commonly ×2).

![[../../5_Assets/Arrays_6.png]]

Advantages:

- Fewer reallocations
- Faster appends
- Better overall performance
