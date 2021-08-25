---
title:
    - Quiz
mainfont: "Liberation Mono"
---

# What is printed to the console by this code?

```python
for num in range(1, 10, 2):
    if 3 < num < 7:
        print(num)
```

- 4

- 5

- 1

- 6

# What does this function do?

```python
def foo(bar):
    baz = []
    for v in bar:
        baz = [v] + baz
```

- Reverses a list given as an argument

- Nothing

- Returns the input list unmodified

- Sums the values of the input list

# What is the output of this expression?

```python
range(10, 5, -1)
```

- `[10, 9, 8, 7, 6]`

- `[10, 9, 8, 7, 6, 5]`

- `range(10, 5, -1)`

# What does this function do?

```python
def bar(baz):
    c = 0
    for i in baz:
        if i == 's':
            c -= 1
        elif i == 'a':
            c += 1
    return c
```


- Counts the number of 's' and 'a' characters in a string

- Nothing

- Unary calculator: 'a' for `+1`, 's' for `-1`

- Retuns a string containing 's' and 'a' charcters depending on the argument
