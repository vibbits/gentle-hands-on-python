# Lists

<div style="display:flex; align-items:center; justify-content:center; width:100%; height: 15rem; background-color:lightsteelblue">
Video placeholder
</div>

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

> _"Simple is better than complex."_ [^1]

So far we've seen how to store a single value in a variable that you can use in your program.
It is also possible to assign a _collection_ of values to a name. In Python, *lists* are a common example of such collections.

A list is an _ordered_ collection of arbitrary python values. Even other lists! A list inside another list is called a _nested list_.
This is similar to a shopping list. My shopping list sometimes looks like this:

* Apples
* Milk
* Dinner:
  * Chicken
  * Chips
  * Salad
* Snacks


You can make a list in Python by seperating each value in a list with commas and placing these between square `[]` brackets.


```python
# My shopping list in Python
["Apples", "Milk", ["Chicken", "Chips", "Salad"], "Snacks"]
```


The type of values in a list can be heterogeneous.


```python
[1, 2, "Fizz", 4, "Buzz"]
```


Lists can be arbitrarily nested.


```python
[["foo"], "bar", [["baz"], "zoom"]]
```



```python
[1, [2, 2, [3, 3, 3, [4, 4, 4, 4]]]]
```


You can annotate the type of _homogeneous_ lists.


```python
mylist: list[int] = [2, 4, 6, 8]
mylist
```


You can _combine_ lists together with the `+` operator.


```python
[1, 2] + [3, 4]
```

This gives you a way to _append_ to a list. We will use this pattern a lot during this course.

```python
mylist: list[int] = [1, 2, 3]
mylist = mylist + [4, 5]
mylist
```

You can even _multiply_ a list by an integer.

```python
[1, 2, 3] * 2
```

[^1]: [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
