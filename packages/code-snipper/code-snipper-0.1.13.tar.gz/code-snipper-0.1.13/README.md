[![PyPI version](https://badge.fury.io/py/code-snipper.svg)](https://badge.fury.io/py/code-snipper)


# codesnipper

This package helps you to extract code sections from a string or a text file.

For example:

If you have a string as follows:

````
Hello world, this is an example

```python
x = 1
y = 2
```
Exit line
````
The package can help you extract the code section i.e.
```
x = 1
y = 2
```
and it will extract the programming language which is `python` in the above case.
It works with multiple code sections as well within a file or string.
