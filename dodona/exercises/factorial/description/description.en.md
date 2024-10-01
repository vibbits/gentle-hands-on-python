Write a function called `factorial` that computes the factorial of its argument. It should accept a
single number as its input argument. Your output should also be a number.

Here is the mathematical definition of `factorial(n)`:
$$
n! = n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 3 \cdot 2 \cdot 1
$$

You can use this template:

```python
def factorial(n: int) -> int:
    ...
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_factorial` that returns `"Success"` if the `factorial` function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> factorial(3)
6
>>> factorial(5)
120
>>> factorial(1)
1
>>> factorial(0)
1
```
