# Repeating tasks

<div style="display:flex; align-items:center; justify-content:center; width:100%; height: 15rem; background-color:lightsteelblue">
Video placeholder
</div>

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

> _"Flat is better than nested."_ [^1]

A very useful feature of computers is that they can do the same thing over and over again,
perfectly, never getting bored. This ability is expressed by executing a few instructions,
then jumping back to the beginning of the series of instructions and executing them again.
This pattern is called a _loop_. Essentially, a loop is a block of code that is repeatedly executed.

## The `for`-each loop
Now that we understand lists of values (from the previous chapter), you may wish to perform some
computation on each value in a list. This can be achieved by _looping_ over each value one-by-one
so that your computation is executed _for each_ value in the list.

Here is an example of how to write and use a `for`-each loop to print the numbers in a list.

```python
numbers = [1, 2, 3, 4]

for number in numbers: # Read as "for each value (called number) in numbers..."
    print(number)
print("Loop has ended")
```

This can be understood by _unrolling_ the loop. The _unrolled_ version of the above loop would
look like this:

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

Notice that `number` is given the value of each successive value in the collection: first it gets
`1` and the loop block is executed, then it gets `2` and so on.

This also illustrates the utility of loops!
Not only is a loop more concise, but it's easier to read and understand than the unrolled version.
Imagine having to type out all the indexes in a list that contains 100 elements! Then imagine if
you had to change the size of the list... that's a LOT OF WORK!!!

[^1]: [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
