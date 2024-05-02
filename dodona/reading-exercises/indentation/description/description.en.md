# Indentation

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>


Programming languages often structure code into "blocks". Python uses indentation (whitespace at
the beginning of a line) to do this. Other programming languages you may've used often use curly
_braces_ (`{}`) for this purpose. 

There are 2 things to keep in mind about indentation:

1. The _indentation level_ (which "sub-block") you are in. You have to be careful how you indent
   the code so that your code is correctly grouped into blocks.
2. Consistently indenting code _within_ a block. 

See what happens if indentation is inconsistent? Try to copy this code into the console above:

```python
# This is the "top-level"

def start_of_a_block():
    # This is the beginning of an indented block of code. Note the space at the beginning of the line
   a_variable = 0
    another = 6
```


### Exercise
In general your function should evaluate to some value using the `return` keyword. What happens if
you forget to use a `return`? What happens if you `return` with no value?

```python
def a_function():
    6
    # Solve this exercise in the console above

print(a_function())
```

You can use the console above to discover the answers to these questions. Notice that, in the Python
console, the prompt changes from `>>>` to `...` when indentation is expected.
