# Indexing and slicing

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

Lists are _ordered_ collections of values. It is sometimes necessary to work with a particular value
within a list, requiring you to extract that value from the list. This "extract" operation is known as
indexing. For example, if you wish to work with the second element of a list you would need to _index_
the list at a particular _offset_ from the beginning of the list.

The beginning of the list is at an offset of _zero_ elements from the beginning of the list. So in
order to "extract" the first element of a list, we index it at `0` using the _index operator_: `[]`.

```console?lang=python&prompt=>>>
>>> my_list = ['A', 'E', 'I', 'O', 'U', 'Y']
>>> my_list[0]
'A'
```

The second element the list is at _index_ `1` and so on.

```console?lang=python&prompt=>>>
>>> my_list[1]
'E'
```

You can replace a value in a list by combining the index operator with the assignment operator.

```console?lang=python&prompt=>>>
>>> my_list[0] = 42
>>> my_list
[42, 'E', 'I', 'O', 'U', 'Y']
```
:::

_Slicing_ is a generalisation of _indexing_ which allows you to view a _slice_ of the list.
If you think of the list as a loaf of bread, you can slice out a part of the loaf as small or
as large as you like.

```python
my_list[start_index : end_index : step]
```

Here are some examples of indexing and slicing. You should copy these examples into the console above
and experiment with what they do until you feel comfortable that you have an intuition for the
correct results.

```console?lang=python&prompt=>>>
>>> my_list[1]  # Indexing
'E'
```

```console?lang=python&prompt=>>>
>>> my_list[54]  # Indexing
IndexError: list index out of range
```

```console?lang=python&prompt=>>>
>>> my_list[1:2]  # Slicing
['E']
```

```console?lang=python&prompt=>>>
>>> my_list[1:3]  # Slicing
['E', 'I']
```

Notice that the slicing operation always stops just short of the _end index_.

```console?lang=python&prompt=>>>
>>> my_list[-1]  # Indexing
['Y']
```

```console?lang=python&prompt=>>>
>>> my_list[3:-1]  # Slicing
['O', 'U']
```

There is a special shortcut for slicing _from the beginning_ or _to the end_:

```console?lang=python&prompt=>>>
>>> my_list[:3]
[42, 'E', 'I']
```

```console?lang=python&prompt=>>>
>>> my_list[3:]
['O', 'U', 'Y']
```

```console?lang=python&prompt=>>>
>>> my_list[:-4]
[42, 'E']
```

```console?lang=python&prompt=>>>
>>> my_list[-4:]
['I', 'O', 'U', 'Y']
```

You can copy the whole list using the slicing operator.

```python
a_copy = my_list[:]
a_copy
```

Rather than slicing every element in the range, you can slice every step-th element.

```console?lang=python&prompt=>>>
>>> my_list[::2]
[42, 'I', 'U']
```

What does a step of `-1` do?

```console?lang=python&prompt=>>>
>>> my_list[::-1]
['Y', 'U', 'O', 'I', 'E', 42]
```
:::

You can also assign to slices.

```console?lang=python&prompt=>>>
>>> my_list[4:] = [2, 1, 0]
>>> my_list
[42, 'E', 'I', 'O', 2, 1, 0]
```

Be careful when assigning to slices when the step is not `1`. You need to make sure that the size of
the slice is the same size as the list you're assigning.

```console?lang=python&prompt=>>>
>>> my_list[::2] = ['a', 'e', 'i', 'o']
>>> my_list
['a', 'E', 'e', 'O', 'i', 1, 'o']
```

But:

```console?lang=python&prompt=>>>
>>> my_list[::3] = [1, 3, 5, 7, 9]
ValueError: attempt to assign sequence of size 5 to extended slice of size 3
>>> my_list
['a', 'E', 'e', 'O', 'i', 1, 'o']
```
