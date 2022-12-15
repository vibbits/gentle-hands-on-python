---
title: "Collections"
jupyter:
  nbformat: 4
  nbformat_minor: 5
  kernelspec:
    display_name: "Python 3 (ipykernel)"
    language: "python"
    name: "python3"
  language_info:
    codemirror_mode:
      name: "ipython"
      version: 3
    file_extension: ".py"
    mimetype: "text/x-python"
    name: "python"
    nbconvert_exporter: "python"
    pygments_lexer: "ipython3"
    version: "3.11.0"
---

# Collecting things together

> _"Simple is better than complex."_<sup><a href="#References">1</a></sup>

## Lists

So far we've seen how to store a single value in a variable that you can use in your program.
It is also possible to assign a _collection_ of values to a name. In Python, *lists* are a common example of such collections.

A list is an _ordered_ collection of arbitrary python values. Even other lists! A list inside another list is called a _nested list_.
This is similar to a shopping list. My shopping list sometimes looks like this:

> * Apples
> * Milk
> * Dinner:
>   * Chicken
>   * Chips
>   * Salad
> * Snacks


You can make a list in Python by seperating each value in a list with commas and placing these between square `[]` brackets.

::: {.cell .code}
```python
# My shopping list in Python
["Apples", "Milk", ["Chicken", "Chips", "Salad"], "Snacks"]
```
:::

The type of values in a list can be heterogeneous.

::: {.cell .code}
```python
[1, 2, "Fizz", 4, "Buzz"]
```
:::

Lists can be arbitrarily nested.

::: {.cell .code}
```python
[["foo"], "bar", [["baz"], "zoom"]]
```
:::

::: {.cell .code}
```python
[1, [2, 2, [3, 3, 3, [4, 4, 4, 4]]]]
```
:::

You can annotate the type of _homogeneous_ lists.

::: {.cell .code}
```python
mylist: list[int] = [2, 4, 6, 8]
mylist
```
:::

You can _combine_ lists together with the `+` operator.

::: {.cell .code}
```python
[1, 2] + [3, 4]
```
:::

This gives you a way to _append_ to a list. We will use this pattern a lot during this course.

::: {.cell .code}
```python
mylist: list[int] = [1, 2, 3]
mylist = mylist + [4, 5]
mylist
```
:::

You can even _multiply_ a list by an integer.

::: {.cell .code}
```python
[1, 2, 3] * 2
```
:::

***

### Exercise 5-1: More FizzBuzz

Write a function called `fizzbuzz3()` that returns a list containing the FizzBuzz game played up to 15.

::: {.cell .code}
```python
def fizzbuzz3():
    "Play the Fizz Buzz game up to 15."
    return _

fizzbuzz3()
```
:::

[Advanced question](Advanced%20Exercises.ipynb#5-1)

***

## What's the length?

What is the length of this list `[1, [2, [3, 4]]]`? If you say `2`, you're right. If you say `4`, you're also right!
However, Python only agrees with you if you said `2`. This is because Python does not look at the structure of the
values in a list. So when you ask Python, `len([1, [2, [3, 4]]])`? Python sees, `len([💩, 💩])`.

::: {.cell .code}
```python
len([1, [2, [3, 4]]])
```
:::

You may wonder if there is a way to compute the number of nested values (`4` in the above example), this is left as an advanced exercise.

## Indexing and Slicing

Lists are _ordered_ collections of values. It is sometimes necessary to work with a particular value within a list, requiring us to
extract that value from the list. This "extract" operation is known as indexing. For example, if you wish to work with the second element
of a list you would need to _index_ the list at a particular _offset_ from the beginning of the list.

The beginning of the list is at an offset of _zero_ elements from the beginning of the list. So in order to "extract" the first element
of a list, we index it at `0` using the _index operator_: `[]`.

::: {.cell .code}
```python
my_list = ['A', 'E', 'I', 'O', 'U', 'Y']
my_list[0]
```
:::

The second element the list is at _index_ `1` and so on.

```python
my_list[1]
```

You can replace a value in a list by combining the index operator with the assignment operator.

::: {.cell .code}
```python
my_list[0] = 42
my_list
```
:::

_Slicing_ is a generalisation of _indexing_ which allows you to view a _slice_ of the list. If you think of the list
as a loaf of bread, you can slice out a part of the loaf as small or as large as you like.

```python
my_list[start_index : end_index : step]
```

Here are some examples of indexing and slicing. Try to guess the output before you execute each cell.

::: {.cell .code}
```python
my_list[1]
```
:::

::: {.cell .code}
```python
my_list[54]
```
:::

::: {.cell .code}
```python
my_list[1:2]
```
:::

::: {.cell .code}
```python
my_list[1:3]
```
:::

Notice that the slicing operation always stops just short of the _end index_.

::: {.cell .code}
```python
my_list[-1]
```
:::

::: {.cell .code}
```python
my_list[5:-1]
```
:::

There is a special shortcut for slicing _from the beginning_ or _to the end_:

::: {.cell .code}
```python
my_list[:5]
```
:::

::: {.cell .code}
```python
my_list[5:]
```
:::

::: {.cell .code}
```python
my_list[:-4]
```
:::

::: {.cell .code}
```python
my_list[-4:]
```
:::

You can copy the whole list using the slicing operator.

::: {.cell .code}
```python
a_copy = my_list[:]
a_copy
```
:::

Rather than slicing every element in the range, you can slice every step-th element.

::: {.cell .code}
```python
my_list[::2]
```
:::

What would this do?

::: {.cell .code}
```python
my_list[::-1]
```
:::

You can also assign to slices.

::: {.cell .code}
```python
my_list[4:] = [2, 1, 0]
my_list
```
:::

Be careful when assigning to slices when the step is not `1`.

::: {.cell .code}
```python
my_list[::2] = ['a', 'e', 'i', 'o', 'u']
my_list
```

***

### Exercise 5-2: Slicing nested lists
Write a function that accepts a nested list as an argument and returns the original
list with second element reversed. For example, given input `[[1, 2], [3, 4]]`, return `[[1, 2], [4, 3]]`.

::: {.cell .code}
```python
def reverse_second(arg):
    "Reverse the second element of a nested list."
    if len(arg) >= 2:
        return _
    else:
        return _

assert reverse_second([[1]]) == [[1]], "Expected [[1]], got: " + str(reverse_second([[1]]))
assert reverse_second([[1], [2]]) == [[1], [2]], "Expected [[1], [2]], got: " + str(reverse_second([[1], [2]]))
assert reverse_second([[1, 5], [10, 9, 8]]) == [[1, 5], [8, 9, 10]], "Expected [[1, 5], [8, 9, 10]], got: " + str(reverse_second([[1, 5], [10, 9, 8]]))
assert reverse_second([1, ['h', 'e', 'l', 'l', 'o'], 2]) == [1, ['o', 'l', 'l', 'e', 'h'], 2], "Expected [1, ['o', 'l', 'l', 'e', 'h'], 2], got: " + str(reverse_second([1, ['h', 'e', 'l', 'l', 'o'], 2]))
```
:::

***

### Exercise 5-3: Sliced FizzBuzz
Slicing presents a possible solution to playing the FizzBuzz game: slice starting at the 3$^{rd}$ element of a list with a `step` of 3, assign an appropriately sized list of `["Fizz"]` strings. The same for 5. Write a function, called `fizzbuzz4()` that attempts to play the Fizz Buzz game in this way. The input will be a list containing the counted numbers, you should use slicing to replace the appropriate numbers with `"Fizz"` or `"Buzz"`.

::: {.cell .code}
```python
def fizzbuzz4(counted):
    counted[_:_:3] = ["Fizz"] * (len(counted) // 3)
    counted[_:_:5] = ["Buzz"] * (len(counted) // 5)
    return counted

fizzbuzz4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
```
:::

Does `fizzbuzz4()` correctly play the Fizz Buzz game? If not, what is wrong with this solution? Can you fix it?

[Advanced question](Advanced%20Exercises.ipynb#5-2)

***

## Operating on Lists and using Python utilities

In the following section we will use the `operator` library which is part of the Python standard library (if you're
interested, see the documentation [here](https://docs.python.org/3/library/operator.html)). The `operator` library
defines functions that are equivalent to the usual operators you've seen so far (e.g. `+`, `*`, _indexing_, etc.).
Let's begin by importing the `operator` library.

::: {.cell .code}
```python
import operator
```
:::

As you progress through the course we will use other facilities provided by the Python standard library. It's very
useful to be aware of them so that you don't need to re-invent what is already available.

You might already appreciate the utility of lists, if not the next few exercises aim to demonstrate how they can be
useful. In order to complete the next exercises you will need to know how to perform some operations on lists as a
whole. Here are 3 new things to become acquainted with:

* The `sorted()` function sorts lists
* The `in` operator checks if a value is contained in a list.
* `operator.itemgetter()` is a function that behaves like the index (`[]`) operator.

The first 2 definitions are available to you without needing to `import` a library. Let us experiment to see what they do.

::: {.cell .code}
```python
6 in [1, 3, 5, 7, 9]
```
:::

::: {.cell .code}
```python
8 in [2, 4, 6, 8, 10]
```
:::

::: {.cell .code}
```python
sorted([5, 10, 2, 7, 1])
```
:::

::: {.cell .code}
```python
sorted([[5], [10], [2], [7], [1]])
```
:::


We can customise the behaviour of the `sorted()` function because it takes 2 _optional_ named arguments: `reverse` to sort in reverse order, and
`key` to extract the value to sort from a structure. One structure you may wish to extract a sort key from is another list, say:

::: {.cell .code}
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
:::

Simply sorting this will not do what we want.

::: {.cell .code}
```python
sorted(song)
```
:::

Instead of sorting on the first element of each nested list you need to sort on the second element: the number of each gift.
The `key` argument requires a function. This function is given each nested list and it should return the value with which
to sort. This is the index operator, `[]`. But the index operator is not a function. This is where the `operator` library
is useful.


::: {.cell .code}
```python
sorted(song, key=operator.itemgetter(1))
```
:::

This sorts the song correctly. Finally, sorting in reverse:

::: {.cell .code}
```python
sorted(song, key=operator.itemgetter(1), reverse=True)
```
:::

***

### Exercise 5-4: Bronze medal

Write a function that accepts a list of scores (highest is better) and return the score of third place (bronze medal).

::: {.cell .code}
```python
def bronze_medal(scores):
    return _

assert bronze_medal([0, 2, 1]) == 0, "Expected: 0, got: " + str(bronze_medal([0, 2, 1]))
assert bronze_medal([54,56,2,1,5223,6,23,57,3,7,3344]) == 57, "Expected: 57, got: " + str(bronze_medal([54,56,2,1,5223,6,23,57,3,7,3344]))
```
:::

***

### Exercise 5-5: Citations
You're given a list containing some data. Each element of the list is another list containing 2 values: the
name of a country, and the average number of citations per citable document produced within that country.
Write a function that takes this list as an argument and returns the name of the country with the second
highest number of average citations.
<!-- Data are from: https://www.scimagojr.com/countryrank.php?order=cd&ord=desc -->

::: {.cell .code}
```python
assert second_highest([['A', 1.0], ['B', 0.5]]) == "B", "Expected: 'B', got: " + str(second_highest([['A', 1.0], ['B', 0.5]]))
assert second_highest([
    ['Netherlands Antilles', 38.46],
    ['Tokelau', 51.9],
    ['Seychelles', 33.56],
    ['Anguilla', 133.98],
    ['Saint Lucia', 37.31],
    ['Panama', 37.87],
    ['Bermuda', 43.33],
    ['Federated States of Micronesia', 85.49],
    ['Gambia', 42.14],
    ['Belize', 41.59]]) == 'Federated States of Micronesia'
```
:::

[Advanced question](Advanced%20Exercises.ipynb#5-5)

***

## Chapter Review
In this chapter you learned how to store multiple values into an ordered, mutable collection called
a `list`. You learned how to access individual values and slices of values. You also learned how to
sort lists and check for membership in a list.


## Review Questions

1. What are lists used for?
<details>
    <summary>Answer</summary>
    To collect values together. 
</details>


2. What does it mean for a list to be mutable?
<details>
    <summary>Answer</summary>
    A value can be changed after creation. The assignment operator (`=`) works.
</details>


3. Is a string (`str`) like a list?
<details>
  <summary>Answer</summary>
  Yes. In the sense that strings can be indexed and sliced. They're collections
  of only characters though. And strings are immutable. You cannot assign to a
  string index.
</details>


4. What is _slicing_?
<details>
    <summary>Answer</summary>
    Slicing is a way to access ranges of elements in a list (or string).
</details>

5. Can you turn a string into a list of characters?
<details>
  <summary>Answer</summary>
  Yes using the `list()` function.
</details>


## References

1. Zen of Python: https://www.python.org/dev/peps/pep-0020/

## Supporting material
* [Automate the Boring Stuff with Python, Chapter 4](http://automatetheboringstuff.com/2e/chapter4/)
* [Automate the Boring Stuff with Python video course, Lesson 13](https://youtu.be/5n6o1MaXDoE)
* [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)
* [How to Design Programs, Chapter 6](https://htdp.org/2003-09-26/Book/curriculum-Z-H-9.html#node_chap_6)
* [Programming Python, Chapter 14](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14.html)

Click [here](06_Loops.ipynb) to go to the next chapter.
