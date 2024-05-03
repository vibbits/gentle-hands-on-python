Slicing presents a possible solution to playing the FizzBuzz game: slice starting at the 3$^{rd}$
element of a list with a `step` of 3, assign an appropriately sized list of `["Fizz"]` strings.
The same for 5. Write a function, called `fizzbuzz()` that attempts to play the Fizz Buzz game in
this way. The input will be a list containing the counted numbers, you should use slicing to
replace the appropriate numbers with `"Fizz"` or `"Buzz"`.

You can use this template:

```python
def fizzbuzz4(counted: list[int]) -> list[str | int]:
    counted[_:_:3] = ["Fizz"] * (len(counted) // 3)
    counted[_:_:5] = ["Buzz"] * (len(counted) // 5)
    return counted
```

## Example

```console?lang=python&prompt=>>>
>>> fizzbuzz([1, 2, 3, 4, 5])
[1, 2, "Fizz", 4, "Buzz"]
```

Does this version of your `fizzbuzz` function play thi Fizz Buzz game correctly?
If not, what is wrong with the solution?

Don't forget to include a docstring and a test function called `test_fizzbuzz` that returns
`"Success"` if the `fizzbuzz` function passes all tests.
