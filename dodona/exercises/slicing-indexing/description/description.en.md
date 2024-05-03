Write a function called `reverse_second` that accepts a nested list as an argument and returns the original
list with second element reversed.

You can use this template:

```python
def reverse_second(arg):
    "Reverse the second element of a nested list."
    if len(arg) >= 2:
        return _
    else:
        return _
```

## Example

```console?lang=python&prompt=>>>
>>> reverse_second([[1]])
[[1]]
>>> reverse_second([[1], [2]])
[[1], [2]]
>>> reverse_second([[1, 5], [8,9 10]])
[[1, 5], [10, 9, 8]]
>>> reverse_second([1, ['h', 'e', 'l', 'l', 'o'], 2])
[1, ['o', 'l', 'l', 'e', 'h'], 2]
```

Don't forget to include a docstring and a test function called `test_reverse_second` that returns
`"Success"` if the `reverse_second` function passes all tests.
