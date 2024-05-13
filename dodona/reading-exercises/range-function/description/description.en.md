# Generating a range of numbers

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

You may be justifiably upset with me after that last exercise. I just told you that loops allow you to
do things repeatedly without having to type out every single case... and yet that's exactly what you
just did in the last exercise didn't you?

Well yes and no. You didn't write out lots of `if`/`elif`/`else` blocks (I hope). But you did have to
list the entire series of numbers that were used to play the game. Or at least you did in the argument
to your function.

What if you wanted to count to `100` or `1000`, would you have to type out `1000` numbers accurately?
Thankfully no, this is a perfect opportunity to introduce another helpful little function from the
standard library.

## The `range()` function

The `range()` function allows you to generate a range of numbers from a starting value up to (but not
including) an end value. By default the starting value is `0` and the numbers will go _up to, but not
including_ the argument that you  provide. But the output of `range()` is not very useful by itself.
Try typing these examples into the python window above:

```python
range(10)
```

You can convert the range to a list to see what values are in the range.

```python
list(range(10))
```

Or loop over each value in the range and print it.

```python
for val in range(10):
    print(val)
```

You can also provide your own starting value.

```python
# Start from 5, up to 10
for val in range(5, 10):
    print(val)
```

Finally, like with slicing, you can provide a `step`.

```python
# Start from 9, down to 0, in steps of -1
for val in range(9, 0, -1):
    print(val)
```
