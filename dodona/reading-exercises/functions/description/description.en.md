# Building Programs

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

> _"Programs must be written for people to read, and only incidentally for machines to execute."_ [^1]

So far, we explored some of the _"building blocks"_ (the fundamental parts) of programming, this
chapter introduces the _"combining parts"_ of programming. In order to build up the solution to
a problem the building blocks are combined together into larger and larger forms until,
finally, a useful whole is produced.

The "combining parts" of programs are called "functions". In many ways, these are equivalent to
mathematical functions but we will not use any more mathematical analogies here. Functions can
be _defined_, _applied_ (or _used_, _called_, _run_), or _composed_.


## Function Application

You can think of a function as a mystery box. At the top is an opening for you to put things into it.
The mystery box transforms anything you put into it and out the bottom it produces the transformed
object.

![Function](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/191px-Function_machine2.svg.png)

The inputs to a function can be a variety of things (some of which we've seen already): a string,
a number, even another function, a mouse press, a video stream, signals from a sensor, a file
containing sequence data, ...

Two built-in Python functions are `abs()` and `len()`. In Python, you _apply_ a function
by typing its name followed by an open parenthesis `(`, a comma separated list of arguments,
and finally a closing parenthesis `)`.

```python
abs(-56)
```

```python
len("hello")
```

These functions take a single argument. Here is one that takes a list of several arguments.

```python
print(True, "A string", 55)
```


## Function Definition

We can also build (or _define_) our own functions. When you're writing your own function, start
with the _keyword_ `def` like so:

```python
def name_of_my_function(some, function, arguments):
    # Some operations
    
    return result
```

The final part of a function is `return` which _specifies what the function evaluates to_ when
you apply it. This function has `3` arguments called `some`, `function`, and `arguments`. 

Let's write our own function to compute the square of a number. This function takes a single
integer argument and returns that number squared. Notice that I have included a type annotation
on the argument.

```python
def my_square(number: int):
    return number ** 2
```

Notice that, when you run this code, nothing seems to happen. This only _defines_ the function.
It has not yet been run or applied. Think of this as telling Python about your function like you
would do with a variable. It might be helpful to imagine Python has a notebook where it writes
down the names of all the definitions it knows about. When you `def` a new function, Python writes
that name down in its notebook.

This new function can now be applied (using matching opening- and closing parenthesis) as you have
already seen:

```python
my_square()
```

😱 `TypeError: my_square() missing 1 required positional argument: 'number'`

What does that mean? It means `my_square()` expects `1` argument, but we gave it `0` arguments.
Let's fix that:

```python
my_square(-5)
```

Because this is a `TypeError` we know that functions also have a type! You can even annotate the
_type_ of the return value like so:

```python
def my_square(number: int) -> int:
    return number ** 2
```

The _type_ of `my_square` is a _function_ that accepts a single integer parameter and returns an integer.

## Function Arguments

When you apply a function to some arguments you can also say that the arguments are "_passed_" to
the function. You can think of this as dropping the number `7` into the mystery box labelled
`my_square`. So what happens to arguments when they're "passed" to a function? Where do they come
from? And where do they go? Let us try to build an intuition.

```python
# We apply the my_square() function to some argument
my_square(7) # Python then goes off to find the my_square() function
# Found it! It looks like this: my_square(number: int) -> int:
# Python then places the value 7 that we passed into a variable or box called number
# that only the body of my_square can see
```

You can think of function arguments as variables that are assigned on function application.
In order to understand what happens, we can now _substitute_ the name "my_square" with
the function body in the definition of `my_square`:

```python
number = 7 # Argument passed to the my_square function
number ** 2 # Body of the my_square function
```

Since we know that `number` is defined to be `7`, we can _substitute_ the name "number" with
the definition: `7`:

```python
7 ** 2
```

Finally, we're left with a mathematical expression that Python can trivially evaluate.


What we just did together is use a _metal model_ of how Python evaluates programs which is known as
the "substitution model of execution" [^2], though it is an imprecise model for Python, it will get
you a long way.

```python
# This mental model also works for passing variables as arguments:
my_var = 7
my_square(my_var)
# Once again, Python places the value in the "my_var" box into the variable or box called number.
```

The next substitution step is to replace everywhere we see the name "my_var" with its definition: `7`.

```python
# 7 = 7  Initial variable assignment
my_square(7)
```

Next, replace the name "my_square" with its definition.

```python
number = 7 # Argument passed to the my_square function
number ** 2 # Body of the my_square function
```

And proceed as above.

[^1]: Abelson, H., Sussman, G.J., Sussman, J. (1996) _[Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html) (2 ed.)_. The MIT Press.

[^2]: Chiusano, P., Bjarnason, R. (2015) [Referential transparency, purity, and the substitution model](https://livebook.manning.com/book/functional-programming-in-scala/chapter-1/52). In _Functional Programming in Scala_ (pp.10-12). Manning.
