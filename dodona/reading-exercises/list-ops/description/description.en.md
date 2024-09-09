# Operating on lists

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

In this section you will use the `operator` library which is part of the Python standard
library (if you're interested, see the documentation
[here](https://docs.python.org/3/library/operator.html)). The `operator` library defines functions
that are equivalent to the usual operators you've seen so far (e.g. `+`, `*`, _indexing_, etc.).
Let's begin by importing the `operator` library.

```python
import operator
```

As you progress through the course you will use other facilities provided by the Python standard
library. It's very useful to be aware of them so that you don't need to re-invent what is already
available.

You might already appreciate the utility of lists, if not the next few exercises should demonstrate
how they can be useful. In order to complete the next exercises you will need to know how to perform
some operations on lists as a whole. Here are 3 new things to become acquainted with:

 - The `sorted()` function sorts lists
 - The `in` operator checks if a value is contained in a list.
 - `operator.itemgetter()` is a function that behaves like the index (`[]`) operator.

The first 2 definitions are available to you without needing to `import` a library.
Here are some examples of what `in` and `sorted` does:

```console?lang=python&prompt=>>>
>>> 6 in [1, 3, 5, 7, 9]
False
```

```console?lang=python&prompt=>>>
>>> 8 in [2, 4, 6, 8, 10]
True
```

```console?lang=python&prompt=>>>
>>> sorted([5, 10, 2, 7, 1])
[1, 2, 5, 7, 10]
```

```console?lang=python&prompt=>>>
>>> sorted([[5], [10], [2], [7], [1]])
[[1], [2], [5], [7], [10]]
```


We can customise the behaviour of the `sorted()` function because it takes 2 _optional_ named
arguments: `reverse` to sort in reverse order, and `key` to extract the value to sort from
a structure. One structure you may wish to extract a sort key from is another list, say:

```python
song = [["french hens", 3],
        ["ladies dancing", 9],
        ["pipers piping", 11],
        ["swans a-swimming", 7],
        ["geese a-laying", 6],
        ["turtle doves", 2],
        ["calling birds", 4],
        ["maids a-milking", 8],
        ["drummers drumming", 12],
        ["lords a-leaping", 10],
        ["gold rings", 5],
        ["partridge in a pear tree", 1]]
```

Simply sorting this will not do what we want.

```console?lang=python&prompt=>>>
>>> sorted(song)
[['calling birds', 4],
 ['drummers drumming', 12],
 ['french hens', 3],
 ['geese a-laying', 6],
 ['gold rings', 5],
 ['ladies dancing', 9],
 ['lords a-leaping', 10],
 ['maids a-milking', 8],
 ['partridge in a pear tree', 1],
 ['pipers piping', 11],
 ['swans a-swimming', 7],
 ['turtle doves', 2]]
```

Instead of sorting on the first element of each nested list you need to sort on the second element:
the number of each gift. The `key` argument requires a function. This function is given each nested
list and it should return the value with which to sort. This is the index operator, `[]`. But the
index operator is not a function. This is where the `operator` library is useful.


```console?lang=python&prompt=>>>
>>> sorted(song, key=operator.itemgetter(1))
[['partridge in a pear tree', 1],
 ['turtle doves', 2],
 ['french hens', 3],
 ['calling birds', 4],
 ['gold rings', 5],
 ['geese a-laying', 6],
 ['swans a-swimming', 7],
 ['maids a-milking', 8],
 ['ladies dancing', 9],
 ['lords a-leaping', 10],
 ['pipers piping', 11],
 ['drummers drumming', 12]]
```

This sorts the song correctly. Finally, sorting in reverse:

```console?lang=python&prompt=>>>
>>> sorted(song, key=operator.itemgetter(1), reverse=True)
[['drummers drumming', 12],
 ['pipers piping', 11],
 ['lords a-leaping', 10],
 ['ladies dancing', 9],
 ['maids a-milking', 8],
 ['swans a-swimming', 7],
 ['geese a-laying', 6],
 ['gold rings', 5],
 ['calling birds', 4],
 ['french hens', 3],
 ['turtle doves', 2],
 ['partridge in a pear tree', 1]]
```
