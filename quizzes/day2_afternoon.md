---
title: "Afternoon, day 2"
mainfont: "Liberation Mono"
---

# What is printed to the console by this code?

```python
for num in [1,3,5,7,9]:
    if 3 < num < 7:
        print(num)
```

A.  4

B.  5

C.  1

D.  6

# What is the result of applying this function?

```python
def foo(bar):
    baz = []
    for v in bar:
        baz = [v] + baz
```

A.  Reverses a list given as an argument

B.  Nothing

C.  Returns the input list unmodified

D.  Sums the values of the input list


# What does this function do?

```python
def bar(baz):
    c = 0
    for i in baz:
        if i == 'a':
            c = c + 1
    return c
```


A.  Counts the number of 'a' characters in a string

B.  Nothing

C.  Retuns a string containing 's' and 'a' charcters depending on the argument

# What is the result of this expression?

```python
sorted([5, 3, 8, 7, 2])
```

A. SyntaxError

B. [2, 3, 5, 7, 8]

C. TypeError
