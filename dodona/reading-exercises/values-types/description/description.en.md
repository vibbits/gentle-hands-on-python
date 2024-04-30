# Values and their Data Types

<video width="100%" controls>
  <source src="https://storage.googleapis.com/vib-training-data/VIDEOS/Python/lesson3.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
 
<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

Using Hedy, you were able to `print` text to the program output area.
You even discovered a special syntax for writing literal text in your programs: you
surrounded the text with quotation marks (`"`). Programmers refer to text between quotation
marks as _strings_. In fact, Python shortens this name to simply `str`. `str` is a  _data type_,
all strings are the type, `str`. As you will discover throughout this course, Python has
a rich set of _data types_ that are useful when writing programs. But first, let us try to
understand why thinking about data types is useful.

---

### Exercise: Thinking with types

Use the interactive console above. What is the result of this operation?

```python
"hello" + 5
```

Read the error message.

 - What happens if you switch the order of the operands to `+`?
 - Why are the error messages different?

---

Indeed it is nonsense. `"hello"` is a string (in Python we say it is a `str`) and `5` is an
integer number (in Python we say `int`). They are different _data types_. You can think of
data types as the _shape_ of some data. The `+` operator expects its operands to be
compatible shapes (data types).

Python allows us programmers the _option_ to explicitly _annotate_ the data types of
values in our programs. This can be very helpful as we will see later on. For now,
let's just look at the syntax for data type annotations in Python.

```python
name: str = "James"
```

In Python, we use the `=` operator for variable assignment. This is the same as in Hedy:
```python
name is "James"
```
But now we use the `:` operator to remind ourselves, or other people reading our code,
that the variable `name` contains a `str`.

## What is the type of a value?

Python provides a function that we can use to discover the data type of a value: `type()`.
Let's use it on some values (you can copy these snippets into the console above):

```python
type("James")
```

```python
type(5)
```

```python
type(len("James"))
```

```python
x = input("What is your name?")
print("Your name is: ", x)
type(x)
```

What do you think is the type of this expression? Try to guess first, then use the `type()` function to check your guess.

```python
"Hello " + "world"
```

## Some other types

Before we finish this chapter, there are 2 further data types that will be
important during this course: `float` and `bool`.

`float`, short for _floating point number_, is a decimal numeric data type
that represents continuous numbers to within some finite accuracy.

`bool`, short for _boolean_ values represent the logical states of `True`
or `False`.

Each of these data types come with their own conversion functions. You should experiment
with them in the console now.

For example, which `int` values are converted to `True`, which are converted to `False`?

```python
bool(0)
```
