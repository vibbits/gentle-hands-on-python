# Otherwise: `else` and `elif` statements

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

You may wish to perform a computation based on one of several conditions. An example from everyday
experience is "What meal will I eat?"


**If** it is breakfast time, then **eat breakfast**

**Otherwise, if** it is lunch time, then **eat lunch**

**Otherwise, if** it is tea time, then **eat tea**

**Otherwise**, **eat snacks**.



In this example we select _only one_ of 4 possible actions (eat breakfast, eat lunch, eat tea, or
eat snacks). This can be neatly translated into pseudo-Python using `if`, `elif`, and `else`:

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

You will notice that `elif` is not the same as another **if**-statement. An **elif** is only
executed if the previous `if` (and other preceding elifs) are not executed. An `elif` is a
convenient short-hand for `else` followed by `if`. The above example is exactly equivalent to:

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

Only a single block is selected in combined `if`/`elif` blocks. You can verify this by copying this
example into the console. Experiment with the value of `x` and the order of the conditions to
convince yourself that only a single block is executed.

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
