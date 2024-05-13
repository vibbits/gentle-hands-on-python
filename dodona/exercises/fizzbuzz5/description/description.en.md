Write a function called `fizzbuzz` that accepts a list of integers as its input. Your output should be
a list of strings playing fizzbuzz for each number in the input. Note that the numbers in the input list might not be in order. For each integer in the input list you should check:

 - if it is a multiple of `3` **and** `5`, put `"Fizz Buzz"` in the output list,
 - if it is a multiple of `3`, put `"Fizz"` in the output list,
 - if it is a multiple of `5`, put `"Buzz"` in the output list, and
 - otherwise put a string representation of the number into the output list.

You can use this template:

```python
def fizzbuzz(numbers: list[int]) -> list[str]:
    output = []
    for number in numbers:
        ...
    
    return output
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_fizzbuzz` that returns `"Success"` if the `fizzbuzz` function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> fizzbuzz([1, 2, 3])
['1', '2', 'Fizz']
>>> fizzbuzz([4, 5, 6, 15])
['4', 'Buzz', 'Fizz', 'Fizz Buzz']
>>> fizzbuzz([])
[]
```

