Computers generally (and therefore most languages used to program computers) understand fractional
decimal numbers using a standard called IEEE-754. [^1]
Along with the specific binary representation of these numbers, IEEE-754 defines the operations that
can be performed on them and the possible errors that can occur.

One of these errors is division by zero. Mathematically, a division by zero is undefined but IEEE-754
defines it to be positive infinity. [^2] In Python however, your program will crash if you attempt to
divide a number by zero.

Your task here is to write a "safe" division function called `safe_div` that does not crash
your program. If your function is called with a zero divisor you should return the string,
`"You cannot divide by zero"`. Otherwise you should return the result of the division operation
between the 2 arguments to the function.

You can use this template:

```python
def safe_div(dividend: float, divisor: float) -> float:
```

## Example

```console?lang=python&prompt=>>>
>>> safe_div(5, 2)
2.5
>>> safe_div(5, 0)
'You cannot divide by zero'
```

Don't forget to include a docstring and a test function called `test_safe_div` that returns
`"Success"` if the `safe_div` function passes all tests.

[^1]: [https://en.wikipedia.org/wiki/IEEE_754](https://en.wikipedia.org/wiki/IEEE_754)

[^2]: Details about this can be found here: [https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF](https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF)
