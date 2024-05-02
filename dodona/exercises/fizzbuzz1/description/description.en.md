Write a function called `fizzbuzz` that accepts a number input and returns a string.

If the input is a multiple of `3` **and** `5`, return `"Fizz Buzz"`. If the input is
a multiple of `3`, return `"Fizz"`. And if the input is a multiple of `5`, return `"Buzz"`.

You can use this template:

```python
def fizzbuzz(number: int) -> str:
    if _:
        return "Fizz Buzz"
    if _:
        return "Fizz"
    if _:
        return "Buzz"
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_fizzbuzz` that returns `"Success"` if the `fizzbuzz` function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> fizzbuzz(33)
'Fizz'
>>> fizzbuzz(30)
'Fizz Buzz'
>>> fizzbuzz(20)
'Buzz'
```

<details>
  <summary>HINT: How to test if a number is a multiple of another?</summary>
  The modulo operator: 
  <code>
    %
  </code>
</details>
