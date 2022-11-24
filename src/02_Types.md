---
title: "Data Types"
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

# Data Types

Using [Hedy](https://hedy.org), you were able to `print` text to the program output area.
You even discovered a special syntax for writing literal text in your programs: you
surrounded the text with quotation marks (`"`). Programmers refer to text between quotation
marks as _strings_. In fact, Python shortens this name to simply `str`. `str` is a  _data type_,
all strings are the type, `str`. As you will discover throughout this course, Python has
a rich set of _data types_ that are useful when writing programs. But first, let us try to
understand why thinking about data types is useful.

What is the result of an operation like this?

```python
"hello" + 5
```

Indeed it is nonsense. `"hello"` is a string (in Python we say it is a `str`) and `5` is an
integer number (in Python we say `int`). They are different _data types_. You can think of
data types as the _shape_ of some data. The `+` operator expects its operands to be
compatible shapes (data types), so if we try to run this code, Python will tell us that
the operation is not allowed with these types of operands:

::: {.cell .code}
```python
"hello" + 5
```
:::

or,

::: {.cell .code}
```python
5 + "hello"
```
:::

Notice the difference in error message. Why are the error messages different?

Python allows us programmers the _option_ to explicitly _annotate_ the data types of
values in our programs. This can be very helpful as we will see later on. For now,
let's just look at the syntax for data type annotations in Python.

::: {.cell .code}
```python
name: str = "James"
```
:::

In Python, we use the `=` operator for variable assignment. This is the same as in Hedy:
```python
name is "James"
```
But now we use the `:` operator to remind ourselves, or other people reading our code,
that the variable `name` contains a `str`.

## What is the type of a value?

Python provides a function that we can use to discover the data type of a value: `type()`.
Let's use it on some values:

::: {.cell .code}
```python
type("James")
```
:::

::: {.cell .code}
```python
type(5)
```
:::

::: {.cell .code}
```python
type(len("James"))
```
:::

::: {.cell .code}
```python
x = input("What is your name?")
print("Your name is: ", x)
type(x)
```
:::

---

### Exercise 2-1: What's that type?

What is the type of this expression?

```python
"Hello " + "world"
```

try to guess first, then use the `type()` function to check your guess.

::: {.cell .code}

:::

## Chapter Review

In this chapter you learned that all values in Python have a _data type_. You
learned that operations on data expect compatible data types, and you learned
how to annotate your programs with their types.

## Review Questions

1. What is a `str`?
<details>
  <summary>Answer</summary>
  A <code>str</code> is the <em>data type</em> of all text.
</details>

2. Is it possible to use the `+` operator when the operands are both `int` data types?
<details>
  <summary>Answer</summary>
  Yes. This would be addition of numbers.
</details>

3. Does Python check my type annotations?
<details>
  <summary>Answer</summary>
  No. Like comments, they are for people reading your code.
  There are separate programs that will check your types but these
  are out of scope for this course.
</details>

Click [here](03_Functions.ipynb) to go to the next chapter.
