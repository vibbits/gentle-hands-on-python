# Testing

You are probably very confident that the code you've written so far is "correct". Afterall, how
difficult is the identity function (a function that just returns its argument)? But as you write more
complicated programs you will probably begin to feel less confident.

Testing, among other virtues, allows you to keep this early confidence in the correctness of your
programs. One (rather naïve) way of testing is to assert an expectation about the state of your
program. With Python, this can be achieved using the keyword **`assert`**. For example, I could
test the `my_square` function like so:

```python
def test_my_square():
  assert 0 == my_square(0)
  assert 1 == my_square(1)
  assert 4 == my_square(2)
  return "Success"
```

Successfully passing these tests will result in the function returning the string "Success".
Failing will result in an **`AssertionError`**.

<img src="media/testing.png" alt="Testing" style="width:95%;height:auto">

Your tests become more useful when they check both expected values and unexpected (edge-case) values.
If your function expects numbers, does it cope well with very large numbers? What about very small
numbers? What about negative numbers? What about zero?

You should not expect to test all possible inputs unless size of the domain of your input type is
very small (for example, the size of the domain of the `bool` type is only `2`).
