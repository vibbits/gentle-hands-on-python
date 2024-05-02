Extend the function called `fizzbuzz` that you wrote earlier by returning the input number if it
doesn't match any of the conditions. Your function should accept a number input and return a string.

As a reminder, if `number`
* is a multiple of `3`, return `"Fizz"`
* is a miltiple of `5`, return `"Buzz"`
* is a multiple of `3` **and** `5`, return `"Fizz Buzz"`
* otherwise, return number (converted to a string)

You can use this template:

```python
def fizzbuzz(number: int) -> str:
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
>>> fizzbuzz(22)
'22'
```
