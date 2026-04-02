# Mod 8 Lab: Custom Set

## Description

Impliment a class `CustomSet` that mirrors the python set. The starter code contains skeleton code for all necessary functions with instructions. `TestLab8.py` contains tests to help you debug. 

**Do not use the built-in `set` or `dict` classes in this assignment.**

## Examples

Examples below are intended to be illustrative, not exhaustive.

```python
>>> from lab8 import CustomSet
>>> s = CustomSet()
>>> "hello" in s
False
>>> s.add("hello")
>>> len(s)
1
>>> "hello" in s
True
>>> s.remove("hello")
>>> s.remove(5)
Traceback (most recent call last):
...
KeyError: Attempt to remove non-extant item 5
>>> 
```

## Submitting

At a minimum, submit a file named `lab8.py` containing a class `CustomSet`.

Students must submit **individually** by the due date (typically Sunday at 11:59 pm EST) to receive credit.