Write a function called `clamp` that accepts a number to clamp between a lower and upper bound.

 - if `number` is less than the lower bound, return the lower bound,
 - if `number` is more than the upper bound, return the upper bound,
 - otherwise just return `number`.

You can use this template:

```python
def clamp(number: int, lower: int, upper: int) -> int:
```

## Example

```console?lang=python&prompt=>>>
>>> clamp(5, 0, 10)
5
>>> clamp(0, 0, 10)
0
>>> clamp(-1, 0, 10)
0
>>>clamp(10, 0, 10)
10
>>>clamp(11, 0, 10)
10
```

Do not forget to include a docstring and a test function called `test_clamp` that returns `"Success"` if the `clamp` function passes all tests.
