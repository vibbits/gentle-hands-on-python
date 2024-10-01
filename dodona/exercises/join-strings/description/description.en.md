Write a function called `joining` that takes a list of strings and a connector as arguments. Your
function should return a single string containing all elements from the input list with the connector
string between them, joined together into a single string.

Here are some example executions. Do not forget to include a docstring and a test function
called `test_joining` that returns `"Success"` if the `joining` function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> joining(["Hello", "world"], ", ")
'Hello, world'
>>> joining(["1", "+", "2"], " ")
'1 + 2'
>>> joining([], "--")
''
>>> joining(["Hola"], "++++")
'Hola'
>>> joining(["One", "Two", "Three", "Four"], " and ")
'One and Two and Three and Four'
```

You can use this template:

```python
def joining(values: list[str], connector: str) -> str:
    ...
```
