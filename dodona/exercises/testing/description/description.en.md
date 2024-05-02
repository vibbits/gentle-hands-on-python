Here is a function to return the fractional part of a floating point number (passed in as an
argument):

```python
def fractional_part(number: float) -> float:
    """Find the fractional part of an input floating point number."""
    int_part = int(number) + 1
    frac_part = int_part + number
    return int_part
```

Here is how it should work

## Example

```console?lang=python&prompt=>>>
>>> fractional_part(1.0)
0.0
>>> fractional_part(2.5)
0.5
>>> fractional_part(-1.5)
0.5
```


Copy the definition of the `fractional_part` function into the script below. Then write a test function
called, `test_fractional_part` to test this function. As you write your tests, you should fix the bugs
in my incorrect definition of the `fractional_parts` function.

If all of your tests pass, your `test_fractional_part` function should return the string `"Success"`.

## Why am I getting very slightly wrong answers?
<details>
  <summary>Why am I getting a very slightly wrong answer?</summary>
  Decimal fractional (a.k.a. floating point) numbers are represented in binary by the computer. Also,
  the computer doesn't have infinite space to store numbers so some numbers that need more that the
  finite precision that the computer can represent. In your test, you can check if the result is
  "close enough" (within some small number) to the result you expected like this:
  
  <code>
    <span class="k">assert</span> <span class="nf">abs</span><span class="p">(</span><span class="nf">expected</span> <span class="o">-</span> <span class="nf">result</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">0.0001</span>
  </code>
</details>
