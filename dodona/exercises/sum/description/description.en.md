Write a function called `summing` that computes the sum of the numbers in an input list. It should
accept a list of numbers (integers or floats) as its input argument. Your output should also be a
number.

Here are some example executions. Do not forget to include a docstring and a test function
called `test_summing` that returns `"Success"` if the `summing` function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> summing([1, 2, 3])
6
>>> summing([-1, 0, 1])
0
>>> summing([])
0
```

Your second task is to find the Python standard library function that does the same thing (Hint: you
can look through [this list](https://docs.python.org/3/library/functions.html)) and assign it to a
variable called `python_sum`. YOU MAY NOT USE THIS FUNCTION IN YOUR SOLUTION.

You can use this template:

```python
def summing(nums: list[int | float]) -> int | float:
    ...
    
python_sum = abs
```
