Write a function called `frequencies` that accepts a string as input and computes the frequency
of each letter in the input string (number of times each letter occurs).
Your function should return a dictionary keyed by the letter and the value should be the frequency of
the key.

You can use this template:

```python
def frequencies(text: str) -> dict[str, int]:
    ...
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_frequencies` that returns `"Success"` if the `frequencies`
function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> frequencies('')
{}
>>> frequencies('RAARE')
{'R': 2, 'A': 2, 'E': 1}
>>> frequencies('Tested')
{'T': 1, 'e': 2, 's': 1, 't': 1, 'd': 1}
```
