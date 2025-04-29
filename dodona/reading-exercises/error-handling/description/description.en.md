# Error handling

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

> _"Errors should never pass silently."_ [^1]

Even if you write the perfect program, you will still face "errors".
The operation you're trying to perform or the computation cannot
proceed. When errors happen, you can decide what to do with them.
Up until now, you have let errors crash your programs. This is a
valid error handling strategy that is reasonable in some circumstances... but not _all_ circumstances. Often, when an error happens, you will know what you want to do. For example, if a file is not present on the disk then you can try to download it. Or another example, if a computation is taking too long to complete you
may decide to use partial results.

In general, there are 4 common mechanisms for handling errors in programs:
1. [Exceptions](https://en.wikipedia.org/wiki/Exception_handling_(programming))
2. [Return values](https://en.wikipedia.org/wiki/Result_type)
3. [Condition systems](https://gigamonkeys.com/book/beyond-exception-handling-conditions-and-restarts)
4. Ignorance

Programming languages usually encourage a single mechanism, Python encourages the use of a mechanism known as "[Exceptions](https://docs.python.org/3/tutorial/errors.html)". The other mechanisms are either much less common or nonexistent in Python code so they will not be discussed further in this course.

You've probably seen exceptions before. For example, run the following code in the terminal above:

```python
1/0
```

If there is a way to recover from the error (or if you want a more detailed error message) you can "catch" the exception before it
crashes your program. For example, lets re-write the `safe_div`
function from earlier in the course. Here is a definition without
any error handling:

```python
def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator
```

As above, selecting a denominator of `0` will cause this program
to crash with a `ZeroDivisionError`. In order to handle this
exception you can surround the exception raising lines in a
try-except block like this:

```python
def safe_div(numerator: float, denominator: float) -> float | None:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("You cannot divide by zero")
```

In this case line 3 raises a `ZeroDivisionError` but the program
does not crash. Instead then `except` block is executed. Note that
multiple types of errors can be handled with this mechanism. E.g.

```python
def safe_div(numerator: float, denominator: float) -> float | None:
    print("Starting safe_div")  # This is not in the try-except, exceptions not caught
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("This should never happen")
```

## Signaling your own errors

Finally, you can signal errors to users of your own functions by raising errors
yourself. To do this you can use the `raise` keyword like this:

```python
def safe_div(numerator: float, denominator: float) -> float:
    raise NotImplementedError("safe_div is not yet implemented")
```

Try to call this function for yourself. Can you handle the error?
Before you mark this lesson as complete you should read through the Python
documentation on exceptions [here](https://docs.python.org/3/library/exceptions.html).

[^1]: [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
