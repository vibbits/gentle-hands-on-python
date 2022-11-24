---
title: "Programs"
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

# Building Programs

> _"Programs must be written for people to read, and only incidentally for machines to execute."_<sup><a href="#References">1</a></sup>

## Functions

In the previous chapter we explored some of the _"building blocks"_ (the fundamental parts) of programming, this chapter introduces the _"combining parts"_ of programming. In order to build up the solution to a problem the building blocks are combined together into larger and larger forms until, finally, a useful whole is produced. This "useful whole" is what we call a program.

The "combining parts" of programs are called "functions". These are equivalent to mathematical functions but we will not use any more mathematical analogies here. Functions can be _defined_, _applied_ (or _used_, _called_), or _composed_. We will see examples of each in this chapter.

---

### Exercise 3-1: Computational thinking

Describe, using plain natural language, how to draw a triangle. Try to notice the potential ambiguities.
Also notice that the _ordering_ of instructions is important. If possible, use these instructions on a friend.

---

## Function Application

Programs are also functions. They consume inputs (also known as arguments) and produce outputs.

![Function](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/191px-Function_machine2.svg.png)

The inputs to a function can be a variety of things (some of which we've seen in the previous chapter), another function, a mouse press, a video stream, signals from a sensor, a file containing sequence data, ...
A function _transforms_ its input to produce its output which can be combined with other functions to build up a whole program.

We've already been using some built-in Python functions, for example **abs()** or **len()**. As you've already seen, in Python you _apply_ a function by typing its name followed by an open parenthesis '(', followed by the argument list, and finally a closing parenthesis ')'.

::: {.cell .code}
```python
abs(-56)
```
:::

::: {.cell .code}
```python
len("hello")
```
:::

## Function Definition

We can also build (or _define_) our own functions. When you're writing your own function, start with the _keyword_ `def` like so:

> ```python
> def name_of_my_function(some, function, arguments):
>     """Some information about the function"""
>  
>     # Some operations
>     
>     return result
> ```
The final part of a function is `return` which specifies what the function evaluates to. This function has `3` arguments called `some`, `function`, and `arguments`. The string immediately after
the definition is called the _docstring_ and is what the `help()` function prints.

Let's write our own function to compute the square of a number. This function takes a single integer argument and returns that number squared. Notice that I have included a type annotation on the argument.

::: {.cell .code}
```python
def my_square(number: int):
    """Compute the square of the input."""
    return number ** 2
```
:::

Notice that, when you run this cell, nothing seems to happen. This only _defines_ the function. It has not yet been run. Think of this as telling Python about your function like you would do with a variable. This also means you can pass functions around like variables.

In order to call the function, we use the following expression:

::: {.cell .code}
```python
my_square()
```
:::

😱 `TypeError: my_square() missing 1 required positional argument: 'number'`

What does that mean? It means `my_square()` expects `1` argument, but we gave it `0` arguments. Let's fix that:

::: {.cell .code}
```python
my_square(-5)
```
:::

So what happens to arguments when they're "passed" to a function? Where do they come from? And where do they go? Let us try to build an intuition.

::: {.cell .code}
```python
# We apply the my_square() function to some argument
my_square(7) # Python then goes off to find the my_square() function
# Found it! It looks like this: def my_square(number):
# Python then places the value 7 that we passed into a variable or box called number
```
:::

::: {.cell .code}
```python
# From the point-of-view of Python, this is essentially what happens:
number = 7 # Argument passed to the my_square function
number ** 2 # Body of the my_square function
```
:::

In your mind, you can simplify this further to just `7 ** 2` or even `49`. When you do this you're using a _metal model_ of Python known as the "substitution model of execution"<sup><a href="#References">2</a></sup>, though it is an imprecise model in this case it will get you a long way.

::: {.cell .code}
```python
# This mental model also works for passing variables as arguments:
my_var = 7
my_square(my_var)
# Once again, Python places the value in the "my_var" box into the variable or box called nnumber.
```
:::

::: {.cell .code}
```python
# From the point-of-view of Python, this is essentially what happens:
my_var = 7 # Initial variable assignment
number = my_var # Argument passed to the my_square function
number ** 2 # Body of the my_square function
```
:::

You can think of function arguments as variables that are assigned on function application.

---

### Exercise 3-2: Function arguments
Try to guess what will be printed before executing the cell.

::: {.cell .code}
```python
a = len("hello")
b = "blob"
c = len(b)
d = my_square(c)

print(a, b, c, d)
```
:::

[Advanced question](Advanced%20Exercises.ipynb#3-2)

---

Information about the function can be retrieved by using the `help()` function. Notice that we are passing the function `my_square` as an argument to the `help` function as if it was a variable.

::: {.cell .code}
```python
help(my_square)
```
:::

---

## Indentation
Python relies on indentation (whitespace at the beginning of a line) to group code into _blocks_. Though this is not a unique characteristic of Python, other programming languages you may've used often use curly brackets or _braces_ (`{}`) for this purpose. 

There are 2 things to keep in mind about indentation:
1. The _indentation level_ (which "sub-block") you are in. You have to be careful how you indent the code so that your code is correctly grouped into blocks.
2. Consistently indenting code _within_ a block. 

See what happens if indentation is inconsistent:

::: {.cell .code}
```python
# This is the "top-level"

def start_of_a_block():
    # This is the beginning of an indented block of code. Note the space at the beginning of the line
   a_variable = 0
    another = 6
```
:::

---

### Exercise 3-3: To return or not to return?
In general youf function should evaluate to some value using the `return` keyword. What happens if you forget to use a `return`? What happens if you `return` with no value?

::: {.cell .code}
```python
def a_function():
    6
    # Solve the exercise here

print(a_function())
```
:::

[Advanced question](Advanced%20Exercises.ipynb#3-3)

---

## Testing
You are probably very confident that the code you've written so far is "correct". But as you write more complicated programs you will probably begin to feel less confident. Testing, among other virtues, allows you to keep this early confidence in the correctness of your programs. One (rather naiive) way of testing is to assert an expectation about the state of your program. This can be achieved using Python keyword **`assert`**. For example, I could test the `multiply` function like so:

::: {.cell .code}
```python
assert 0 == mySquare(0)
assert 1 == mySquare(1)
assert 4 == mySquare(2)
```
:::

Successfully passing these tests will result in no output at all. Failing will result in **`AssertionError`** with no description of what went wrong.

![Testing](images/testing.png)

Your tests become more useful when they check both expected values and unexpected (edge-case) values. If your function expects numbers, does it cope well with very large numbers? What about very small numbers? What about negative numbers? What about zero?

### Testing example
Here I will demonstrate solving an exercise and ensuring the test cases pass

::: {.cell .code}
```python
# Write a function definition here

# These are _test cases_
assert 3 == my_example_function(1, 2), "I expected 3, but got " + str(my_example_function(1, 2))
assert 0 == my_example_function(-51, 51), "I expected 0, but got " + str(my_example_function(-51, 51))
assert my_example_function.__doc__ is not None, "You should write a docstring for your function"
```
:::

---

### Exercise 3-4: Testing
How would you test the following function. Write some tests, try to discover a bug.

::: {.cell .code}
```python
def fractional_part(number):
    """Find the fractional part of an input floating point number."""
    int_part = int(number) + 1
    frac_part = int_part + number
    return int_part

# Write your tests here
```
:::

[Advanced question](Advanced%20Exercises.ipynb#3-8)

---

## Chapter Review
In this chapter you learned how to write code that simplifies the task of understanding a program by
_abstracting away_ details. Functions are a fundamentally important part of programming, indeed they're
the other half of programming. Functions even correspond to mathematical proofs<sup><a href="#References">3</a></sup>!
You have now covered _all_ of the very fundamentals of programming. You've understood the building blocks.
And now you've understood the combining of things together using function definition and application.

If you are new to programming then it is very likely this will seem overwhelming. Learning to program
requires you to understand many new concepts. It is ok if you feel overwhelmed, the remaining chapters
are here to help you practise. In some sense they are just more details of what we have already covered
in the last 2 chapters<sup><a href="#References">4</a></sup>.

### Review Questions

1. What is a function?
<details>
    <summary>Answer</summary>
    A <em>function</em> is a block of re-usable code with a name, that can be called using that name.
</details>

2. What is the result of evaluating a function called?
<details>
    <summary>Answer</summary>
    The <em>return value</em>. Or the value <em>returned by the function</em>.
</details>

3. What are docstrings? How to you access them?
<details>
    <summary>Answer</summary>
    Docstrings are documentation that can be accessed using the <code>help()</code> function.
</details>

4. What is meant by "function application", how is this different from "function composition"?
<details>
    <summary>Answer</summary>
    Function application is synonymous with function "call" or "use". A function is applied to its arguments and evaluated to produce results. Function composition is the combining of several functions together to make a new "thing" that may be applied later. In Python,
    the function application operator is <code>()</code>.
</details>

## References

1. Abelson, H., Sussman, G.J., Sussman, J. (1996) _[Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html) (2 ed.)_. The MIT Press.
2. Chiusano, P., Bjarnason, R. (2015) [Referential transparency, purity, and the substitution model](https://livebook.manning.com/book/functional-programming-in-scala/chapter-1/52). In _Functional Programming in Scala_ (pp.10-12). Manning.
3. [The Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
4. Hoare, C.A.R. (1969) _[An Axiomatic Basis for Computer Programming](https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf)_. Communications of the ACM, 12(10):576-580 and 583.

## 8. Supporting material
* [A Data Centric Introduction to Computing, Chapter 5](https://dcic-world.org/2021-08-21/From_Repeated_Expressions_to_Functions.html)
* [Automate the Boring Stuff with Python, Chapter 3](http://automatetheboringstuff.com/2e/chapter3/)
* [Automate the Boring Stuff with Python video course, Lesson 9](https://youtu.be/WB4hJJkfhLU)


Click [here](04_Decisions.ipynb) to go to the next chapter.
