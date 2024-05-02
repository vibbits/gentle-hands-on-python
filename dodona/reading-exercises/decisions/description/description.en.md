# Making Decisions

<div style="display:flex; align-items:center; justify-content:center; width:100%; height: 15rem; background-color:lightsteelblue">
Video placeholder
</div>

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

> _"Now is better than never."_ [^1]

## _FizzBuzz_: A counting game
This will be your first non-trivial Python program. "FizzBuzz" is a childrens game to help learn
multiplication. It can be played with 1 or more people and involves taking turns to count up from
`1`. If the number is a multiple of `3`, you don't say the number, instead you say "Fizz". If
the number is a multiple of `5` you say "Buzz". Finally, if the number is a multiple of `3` **and** `5`
you say "Fizz Buzz".

The goal is to write a Python program that will play this game by itself, counting up to some number
argument that we give it. Like this:
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
  <img src="images/fizzbuzz_flowchart.svg" style="height: 800px; width:auto" alt="Fizzbuzz flowchart" />
    <figcaption>A flowchart to tell you how to play Fizzbuzz</figcaption>
</figure>

We're going to begin to implement this `fizzbuzz` function. Although you're already familiar
with universally applicable programming concepts, we will introduce some Python specifics that
will help us to write a `fizzbuzz` function. This begins with _conditional logic_...

## The `if` statement

The **if** statement allows you to only execute an indented _block_ of code if a boolean condition is
satisfied (if the answer to a question is "YES"). You can think of **if** as _guarding_ its indented block.

![Python if statement](https://files.realpython.com/media/t.78f3bacaa261.png)

Just as with function definitions, Python syntax requires that you put a colon `:` after the condition,
and that the block of code guarded by the conditional be **equally indented** to the same **indentation level**.

```python
x = 5 # Assignment to a variable. We put the number 5 in a box called x
 
if x == 5: # Question: is the value in the variable called 'x' equal to 5?
    print("x is five!")

if x!=5: # Question: is the value in the variable called 'x' not equal to 5?
    print("x is not five!")
```

[^1]: [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
