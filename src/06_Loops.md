---
title: "Loops"
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

# If at first you don't succeed, try, and try again

> _"Flat is better than nested."_<sup><a href="#References">1</a></sup>

A very useful feature of computers is that they can do the same thing over and over again, perfectly, never getting bored.
In Python this ability is expressed using a _loop_. Essentially, a loop is a block of code that is repeatedly executed.

## The `for`-each loop
Now that we understand _collections_ of values (from the previous chapter), you may wish to perform some computation on
each value in a collection. This can be achieved by _looping_ over each value one-by-one so that your computation is
executed _for each_ value in the collection.

Here is an example of to write and use a `for`-each loop to "count" up from 1:

::: {.cell .code}
```python
numbers = [1, 2, 3, 4]

for number in numbers: # Read as "for each value (called number) in numbers..."
    print(number)
print("Loop has ended")
```
:::

This can be understood by _unrolling_ the loop. The _unrolled_ version of the above loop would look like this:

::: {.cell .code}
```python
numbers = [1, 2, 3, 4]

number = numbers[0] # Set number to the first value in numbers
print(number)

number = numbers[1] # Set number to the second value in numbers
print(number)

number = numbers[2] # Set number to the third value in numbers
print(number)

number = numbers[3] # Set number to the fourth value in numbers
print(number)

print("Loop has ended")
```
:::

Notice that `number` is given the value of each successive value in the collection: first it gets `1` and the loop block is
executed, then it gets `2` and so on.

This also illustrates the utility of loops!
Not only is a loop more concise, but it's easier to read and less error prone. Imagine having to type out all the indexes
in a list that contains 100 elements! Then imagine if you had to change the size of the list... that's a LOT OF WORK!!!

Lets use our new knowledge of loops to try to play the Fizz Buzz game again. This time, checking each number as we come accross it in a loop.

***

### Exercise 6-1: Can we play Fizz Buzz yet?
Write a function to play the fizzbuzz game up to `15`. You function should accept no arguments and return a list starting at `1` that tracks the progress of a game of Fizz Buzz.

That is, your function should use a loop to produce this list: `[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']`

::: {.cell .code}
```python
def fizzbuzz5():
    game = []
    for number in _:
        _
    
    return game

assert fizzbuzz() == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'], "Output is not correct :("
fizzbuzz()
```
:::

[Advanced question](Advanced%20Exercises.ipynb#6-1)

---

**What!?** I just told you that loops allow you to do things repeatedly without having to type out every single case... and yet that's exactly what you just did! Didn't you?

Well yes and no. You didn't write out 15 `if`/`elif`/`else` blocks which is a win. But you did have to list the entire series of numbers that were used to play the game.
What if you wanted to count to `100` or `1000`, would you have to type out `1000` numbers accurately? Thankfully no, this is a perfect opportunity to introduce another helpful
little function from the standard library.

## Generating a `range()` of numbers

The `range()` function allows us to generate a range of numbers. By default the starting value is `0` and the numbers will go _up to, but not including_ the
argument we provide. But the output of `range()` is not very useful by itself.

::: {.cell .code}
```python
range(10)
```
:::

You can convert the range to a list to see what values are in the range.

::: {.cell .code}
```python
list(range(10))
```
:::

Or loop over each value in the range and print it.

::: {.cell .code}
```python
for val in range(10):
    print(val)
```
:::

You can also provide your own starting value.

::: {.cell .code}
```python
for val in range(5, 10):
    print(val)
```
:::

Finally, like with slicing, you can provide a `step`.

::: {.cell .code}
```python
for val in range(9, 0, -1):
    print(val)
```
:::

***

### Exercise 6-2: Let's play Fizz Buzz
Finally, we have all of the tools we need to write a concise program to play Fizz Buzz. Write a function called `fizzbuzz6` that takes an integer argument which is the number to count up to and returns a list starting at 1 tracking the progress of playing the Fizz Buzz game.

::: {.cell .code}
```python
def fizzbuzz6(end):
    "Play Fizz Buzz"
    ...

assert fizzbuzz6(0) == []
assert fizzbuzz6(2) == [1, 2]
assert fizzbuzz6(5) == [1, 2, 'Fizz', 4, 'Buzz']
assert fizzbuzz6(15) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']

fizzbuzz6(30)
```
:::

Although this is the last time we will look at the Fizz Buzz game, it is useful to reflect on your final implementation. What is good about it? What could be improved? How easy
is it to change if requirements change (say if we add the 3$^{rd}$ condition on multiples of `7`)?

***

### Exercise 6-3: Factorial
Write a function that computes the factorial of its argument.

$$n! = n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 3 \cdot 2 \cdot 1$$

::: {.cell .code}
```python
def myfactorial(number):
    # 5! = 5 * 4 * 3 * 2 * 1
    _

assert myfactorial(0) == 1, "Expected 1, got: " + str(myfactorial(0))
assert myfactorial(1) == 1, "Expected 1, got: " + str(myfactorial(1))
assert myfactorial(2) == 2, "Expected 2, got: " + str(myfactorial(2))
assert myfactorial(5) == 120, "Expected 120, got: " + str(myfactorial(5))
```
:::

***

### Exercise 6-4: Summing numbers
Below is the definition of a function to sum numbers from in the argument (a list). You have 2 tasks:

1. Identify and fix the bug(s) using techniques you have explored so far.
1. Find the Python standard library function that does the same thing (Hint: you can look through [this list](https://docs.python.org/3/library/functions.html)).

::: {.cell .code}
```python
def mysum(data):
    "Sum all of the numbers in the input list (called data)"
    total = 0
    for number in end:
        total = number
    
    return total
```
:::

***

### Exercise 6-5: Join strings
Once again, below is the deefinition of a function that takes a list of strings and joins them into a single string with comma seperators.

Here are 2 examples of the expected output:
```python
>>> myjoin(["hello", "world"])
"hello,world"

>>> myjoin(["sample1", "0.5"])
"sample1,0.5"
```

Your task is to identify and fix the bug(s) using techniques you have explored so far. The Python function to do this looks like, `','.join(strings)`.

::: {.cell .code}
```python
def myjoin(strings):
    joined = ""
    for string in strings:
        joined = joined + string + ","
```
:::

[Advanced question](Advanced%20Exercises.ipynb#6-5)

***

## Chapter Review
Congratulations! By now you understand enough Python to tackle complex and interesting problems. Hopefully you noticed the exercises are becoming more interesting. Keep practicing
and your confidence and ability to solve problems can only improve.

In this chapter you've learned how to ask the computer to repeat a block of code for you using a `for`-each loop. You also learned about 2 useful built-in functions: `sum()` and
`join()`.


## Review Questions

1. Why is "looping" useful?
<details>
    <summary>Answer</summary>
    Manually repeating computations is tedious and error prone. Try not to repeat yourself, computers are much better at it.
</details>

2. What is a `for`-each loop used for?
<details>
    <summary>Answer</summary>
    Repeating operations on each element of a <em>collection</em> such as a list or tuple.
</details>

3. What is `range()` used for?
<details>
    <summary>Answer</summary>
    Save us typing out a range of numbers in a <code>for</code>-each loop. A <em>range</em> has a given start point, to a given end point, and uses a given
    step size.
</details>

4. What operation **cannot** be performed in the block of code being looped over?
<details>
    <summary>Answer</summary>
    None! All Python operations can be performed in a loop. But <b>be careful</b>: NEVER mofify the list it'er looping over.
</details>


## References

1. Zen of Python: https://www.python.org/dev/peps/pep-0020/

## Supporting material
* [Automate the Boring Stuff with Python, Chapter 2](https://realpython.com/python-for-loop/)
* [Automate the Boring Stuff with Python video course, Lesson 14](https://youtu.be/umTnflPbYww)
* [Real Python: For loop](https://realpython.com/python-for-loop/)
* [Programming Python, Chapter 8](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch08.html)

Click [here](07_Dictionaries.ipynb) to go to the next chapter.
