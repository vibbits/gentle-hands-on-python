# Building Programs

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>


## Help

Python comes with an in-built documentation system that you can access using a function called `help()`.

```python
help(abs)
```

The message for our own `my_square` function is not very useful though:

```python
def my_square(number: int) -> int:
  return number ** 2

help(my_square)
```

In order to make the help message for our function more useful we have to slightly
_change the definition_ of `my_square` to include a _docstring_. If you put a string on the
line immediately after the name of your function, this string will be included in the help
message for you.

```python
def my_square(number: int) -> int:
    "Compute the square of the input number."
    return number ** 2
```

Now check the help message.

```python
help(my_square)
```
