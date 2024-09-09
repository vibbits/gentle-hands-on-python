# How many values in a list

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

What is the length of this list `[1, [2, [3, 4]]]`?

If you say `2`, you're right. If you say `4`, you're also right!

However, Python only agrees with you if you said `2`. This is because Python does not look at the
structure of the values in a list. So when you ask Python, `len([1, [2, [3, 4]]])`?
Python sees, `len([💩, 💩])`.


Copy this code into the console and experiment with it:

```python
len([1, [2, [3, 4]]])
```


You may wonder if there is a way to compute the number of nested values (`4` in the above example),
this is left as an advanced exercise for you.
