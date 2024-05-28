Strings can be indexed and sliced in the same way that lists are. In fact, you can think of
strings as special purpose lists. Lists that just contain characters.

Write a function called `truncate` that takes a string, and a maximum length for that string as input.
If the string is longer than the maximum length then `truncate` should truncate the string and replace
at most the last 3 (or less) characters with ellipses ("...") such that the length of the returned
string is equal to the maximum length argument. Please see the example for clarification.

You can use this template:

```python
def truncate(text: str, max_len: int) -> str:
```

## Example

```console?lang=python&prompt=>>>
>>> truncate("hello world", 10)
'hello w...'
>>> truncate("python", 10)
'python'
>>> truncate("python", 6)
'python'
>>> truncate("James", 4)
'J...'
>>> truncate("", 4)
''
>>> truncate("James", 3)
'...'
>>> truncate("python", 1)
'.'
>>> truncate("TEST", 2)
'..'
```

Don't forget to include a docstring and a test function called `test_truncate` that returns `"Success"` if the `truncate` function passes all tests.
