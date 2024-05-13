Now you finally have all of the tools you need to write a useful fizzbuzz checker program.

Write a function called `fizzbuzz` that accepts a number to play fizzbuzz up to as its input argument.
Your output should be a list of strings playing fizzbuzz for each number counting up to the input.
A reminder of the rules of fizzbuzz:

 - if a number is a multiple of `3` **and** `5`, put `"Fizz Buzz"` in the output list,
 - if a number is a multiple of `3`, put `"Fizz"` in the output list,
 - if a number is a multiple of `5`, put `"Buzz"` in the output list, and
 - otherwise put a string representation of the number into the output list.

You can use this template:

```python
def fizzbuzz(up_to: int) -> list[str]:
    output = []
    ...
    
    return output
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_fizzbuzz` that returns `"Success"` if the `fizzbuzz` function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> fizzbuzz(3)
['1', '2', 'Fizz']
>>> fizzbuzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']
>>> fizzbuzz(0)
[]
```

