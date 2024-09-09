When you write a program for yourself (or download a Python program from the internet), you will
probably want to run it sooner or later.

This is quite straightforward. You can simply follow these steps:
* Open the terminal program you use (on Windows this might be called "Power Shell" or "CMD"),
* Navigate to the folder where the program is stored,
* Run the program by typing `python my_cool_program.py` (also known as running a "script").

There is an important problem when building programs that you should be aware of: any top-level code
always runs when you run the script **BUT ALSO** at _import_ time. That's right! You can `import`
your program too.

This is a problem because, you probably don't expect to be running Python code just because you
`import`ed something. To avoid this you can use a trick to check if your code is being run as a script
or if it's being imported.

There is a special variable that Python gives you called `__name__` which is the name of the current
module. Try this in your own programming environment if you like: create 2 files.

A file "a.py" should contain:
```python
print("__name__ is: ", __name__)
```

A file "b.py" should contain:
```python
import a
print("I'm in b")
```

Now run `python a.py` (Use a.py as a script, not importing it). This should be printed to the console:
```
__name__ is:  __main__
```

And if you run `python b.py` (Import a.py). This should print:
```
__name__ is:  a
I'm in b
```

Notice that the special variable `__name__` contains `"__main__"` when you run the file as a script.
So when you define code to run when using your program as a script you should use this construction:
```python
if __name__ == "__main__":
   # code to run when using my program as a script.

```

In this exercise you will define a function called `what_am_i` that takes no arguments. This function
should return the contents of the special `__name__` variable. When your code is run as a script,
you should print `"I am a script"` to the console. If your code is imported, you should not print
anything.

You can use this template:

```python
def what_am_i() -> str:
  ...
```

Do not forget to include a docstring on your `what_am_i` function but you do not need to write any
tests.
