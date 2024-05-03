Write a function called `bronze_medal` that accepts a list of scores (highest is better) and returns
the score of third place (bronze medal). If there are less than 3 values in the list then you
should return `None`.

You can use this template:

```python
def bronze_medal(scores: list[int]) -> int | None:
```

## Example

```console?lang=python&prompt=>>>
>>> bronze_medal([0, 1, 2])
0
>>> bronze_medal([54,56,2,1,5223,6,23,57,3,7,3344])
57
>>> bronze_medal([10, 9])

>>> bronze_medal([])

```

Do not forget to include a docstring and a test function called `test_bronze_medal` that returns `"Success"` if the `bronze_medal` function passes all tests.
