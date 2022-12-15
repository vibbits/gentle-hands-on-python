---
title: "Decisions"
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

# Making Decisions

> _"Now is better than never."_<sup><a href="#References">1</a></sup>

## _FizzBuzz_: A counting game
This will be your first non-trivial Python program. "FizzBuzz" is a childrens game to help learn multiplication.
It can be played with 1 or more people and involves taking turns to count up from `1`. If the number is a
multiple of `3`, you don't say the number, instead you say "Fizz". If the number is a multiple of `5` you say
"Buzz". Finally, if the number is a multiple of `3` **and** `5` you say "Fizz Buzz".

The goal is to write a Python program that will play this game by itself, counting up to some number argument
that we give it. Like this:
```python
>>> fizzbuzz(15)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
```

<figure>
  <img src="images/fizzbuzz_flowchart.svg" style="height: 800px" alt="Fizzbuzz flowchart" />
    <figcaption><em style="font-weight:bold">Figure 4-1</em>: A flowchart to tell you how to play Fizzbuzz</figcaption>
</figure>

In this chapter we're going to begin to implement this `fizzbuzz` function. Although you're already familiar
with universally applicable programming concepts, we will introduce some Python specifics that will help us
to write a `fizzbuzz` function. This begins with _conditional logic_...

## The `if` statement

The **if** statement allows you to only execute an indented _block_ of code if a boolean condition is
satisfied (if the answer to a question is "YES"). You can think of **if** as _guarding_ its indented block.

![Python if statement](https://files.realpython.com/media/t.78f3bacaa261.png)

Just as with function definitions, Python syntax requires that you put a colon `:` after the condition,
and that the block of code guarded by the conditional be **equally indented** to the same **indentation level**.

::: {.cell .code}
```python
x = 5 # Assignment to a variable. We put the number 5 in a box called x
 
if x == 5: # Question: is the value in the variable called 'x' equal to 5?
    print("x is five!")

if x!=5: # Question: is the value in the variable called 'x' not equal to 5?
    print("x is not five!")
```
:::

***

### Exercise 4-1: The beginnings of FizzBuzz

Using the template below, write out the 3 conditions we need for the FizzBuzz game. Replace the `_` characters with your conditions.
You may find the modulo division (or _remainder_) operator useful: `%`.

::: {.cell .code}
```python
def fizzbuzz1(number: int) -> str:
    if _:
        return "Fizz Buzz"
    if _:
        return "Fizz"
    if _:
        return "Buzz"
    
assert "Fizz" == fizzbuzz1(33), "Expected: \"Fizz\", got: " + str(fizzbuzz1(33))
assert "Fizz Buzz" == fizzbuzz1(30), "Expected: \"Fizz Buzz\", got: " + str(fizzbuzz1(30))
assert "Buzz" == fizzbuzz1(20), "Expected: \"Buzz\", got: " + str(fizzbuzz1(20))
```
:::

For extra points, why is "Fizz Buzz" returned first? What happens if you check the "Fizz Buzz" condition last?

[Advanced question](Advanced%20Exercises.ipynb#4-1)

***

### Exercise 4-2: Clamping

Can you spot (and fix!) the bug caused by incorrect grouping of code in the following snippet?
<details>
    <summary>What should this function do?</summary>
    <ul>
        <li>if <code>value</code> is lower than 0 (e.g. -2 or -7), it will be overwritten by the value 0</li>
        <li>if <code>value</code> is higher than 10 (e.g. 132 or 17), it will be overwritten by the value 10.</li>
        <li>otherwise, if <code>value</code> is between 0 and 10 it will be returned unchanged.
    </ul>
</details>

::: {.cell .code}
```python
def clamp_0_10(value: int) -> int:
    "Bound value between 0 and 10 inclusive"
    minimum_value = 0
    maximum_value = 10
    
    if value < minimum_value:
        print(value, "is too small")
    value = minimum_value
    
    if value > maximum_value:
        print(value, "is too big")
    value = maximum_value
    return value

assert 0 == clamp_0_10(-5), "Input: -5, expected:  0, got: " + str(clamp_0_10(-5))
assert 0 == clamp_0_10(0), "Input:  0, expected:  0, got: " + str(clamp_0_10(0))
assert 5 == clamp_0_10(5), "Input:  5, expected:  5, got: " + str(clamp_0_10(5))
assert 10 == clamp_0_10(10), "Input: 10, expected: 10, got: " + str(clamp_0_10(10))
assert 10 == clamp_0_10(11), "Input: 11, expected: 10, got: " + str(clamp_0_10(11))
```
:::

[Advanced question](Advanced%20Exercises.ipynb#4-2)

***
### Exercise 4-3: Division by zero

Write a program to compute division that checks for division by zero. Complete your code in the template provided below by replacing the `_` characters.

::: {.cell .code}
```python
def division(x: int, y: int):
    if _:
        return "You cannot divide by zero"
    
    return x / y

assert "You cannot divide by zero" == division(1, 0), "Expected: \"You cannot divide by zero\", got: " + str(division(1, 0))
assert 1.0 == division(1, 1), "Expected: 1.0, got: " + str(division(1, 1))
```
:::

[Advanced question](Advanced%20Exercises.ipynb#4-3)

***

### Exercise 4-4: Odd and even

Write a function that returns "odd" when its input is odd, and "even" otherwise. Also add you own test to ensure your answer is correct.

::: {.cell .code}
```python
def even_or_odd(num: int) -> str:
    _
```
:::

[Advanced question](Advanced%20Exercises.ipynb#4-4)

***

## Otherwise: `else` and `elif` statements

You may wish to perform a computation based on one of several conditions. An example from everyday experience
is "What meal will I eat?"


**If** it is breakfast time, then **eat breakfast**

**Otherwise, if** it is lunch time, then **eat lunch**

**Otherwise, if** it is tea time, then **eat tea**

**Otherwise**, **eat snacks**.



In this example we select _only one_ of 4 possible actions (eat breakfast, eat lunch, eat tea, or eat snacks).
This can be neatly translated into pseudo-Python using `if`, `elif`, and `else`:

```python
if 6_00 <= current_time() <= 10_00:
    eat_breakfast()
elif 12_00 <= current_time() <= 13_00:
    eat_lunch()
elif 17_00 <= current_time() <= 20_00:
    eat_tea()
else:
    eat_snacks()
```

You will notice that `elif` is not the same as another **if**-statement. An **elif** is only executed if the
previous `if` (and other preceding elifs) are not executed. An `elif` is a convenient short-hand for `else`
followed by `if`. The above example is exactly equivalent to:

```python
if 6_00 <= current_time() <= 10_00:
    eat_breakfast()
else:
    if 12_00 <= current_time() <= 13_00:
        eat_lunch()
    else:
        if 17_00 <= current_time() <= 20_00:
            eat_dinner()
        else:
            eat_snacks()
```

Only a single block is selected in combined `if`/`elif` blocks:

::: {.cell .code}
```python
x = 5
 
if x == 5:
    print("x is 5")
elif x < 10:
    print("x is less than ten")
elif x > 0:
    print("x is positive")

print("The end")
```
:::

Now only the code under the first condition is executed, not the second or the third. If we switch the conditions around a bit:

::: {.cell .code}
```python
x = 5
 
if x < 10:
    print("x is less than ten")
elif x == 5:
    print("x is 5")
elif x > 0:
    print("x is positive")

print("The end")
```
:::

Now something different is printed because only a single conditional block is ever executed.

***

### Exercise 4-5: More FizzBuzz

Extend the fizzbuzz function you wrote earlier by returning the input number if it doesn't match any of the conditions.

A reminder, if `number`
* is a multiple of `3`, return `"Fizz"`
* is a miltiple of `5`, return `"Buzz"`
* is a multiple of `3` **and** `5`, return `"Fizz Buzz"`
* otherwise, return number

Use the template provided below, replace the `_` characters.

::: {.cell .code}
```python
def fizzbuzz2(number):
    if _:
        return "Fizz Buzz"
    elif _:
        return "Fizz"
    elif _:
        return "Buzz"
    _:
        _
    
assert "Fizz" == fizzbuzz2(33), "Expected: \"Fizz\", got: " + str(fizzbuzz2(33))
assert "Fizz Buzz" == fizzbuzz2(30), "Expected: \"Fizz Buzz\", got: " + str(fizzbuzz2(30))
assert "Buzz" == fizzbuzz2(20), "Expected: \"Buzz\", got: " + str(fizzbuzz2(20))
assert 16 == fizzbuzz2(16), "Expected: 16, got: " + str(fizzbuzz2(16))
```
:::

[Advanced question](Advanced%20Exercises.ipynb#4-5)

***

## Chapter Review
In this chapter you've learned how to _guard_ an indented block with an `if` statement in order to conditionally execute
the block of code. You've also learned how to check multiple conditions using `if` with `elif`. And finally, you've
learned how to use `else` as a catch-all final alternative.


## Review Questions

1. What is a code block?
<details>
    <summary>Answer</summary>
    A series of Python statements that are equally indented and executed together.
</details>


2. What does "equally indented" mean?
<details>
    <summary>Answer</summary>
    The amount of indentation (whitespace) after the start of a row of characters is the same.
</details>


3. What can be in an `if` or `elif` condition?
<details>
    <summary>Answer</summary>
    Any boolean expression including function calls.
</details>


4. What is the difference between `if` and `elif`?
<details>
    <summary>Answer</summary>
    <code>elif</code> is just short for an <code>else</code> followed by an <code>if</code>
</details>

## References

1. Zen of Python: https://www.python.org/dev/peps/pep-0020/

## Supporting material
* [Automate the Boring Stuff with Python, Chapter 2](http://automatetheboringstuff.com/2e/chapter2/)
* [Automate the Boring Stuff with Python video course, Lesson 5](https://youtu.be/lWeCgEbk-Ro)
* [Real Python: Conditional statements](https://realpython.com/python-conditional-statements/)
* [How to Design Programs, Chapter 4](https://htdp.org/2003-09-26/Book/curriculum-Z-H-7.html#node_chap_4)


Click [here](05_Collections.ipynb) to go to the next chapter.
