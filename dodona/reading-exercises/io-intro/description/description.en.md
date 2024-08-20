# Fetching and storing data

<div style="display:flex; align-items:center; justify-content:center; width:100%; height: 15rem; background-color:lightsteelblue">
Video placeholder
</div>

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

In this section you  will use 2 sources of data: the internet and the filesystem. You will also look at
storing your data onto the filesystem. More often than not, the data you need for your program will
come from somewhere outside of your program. Often, that "somewhere" will be a file or some location
on the internet. Especially for more complex data, it becomes essential to be able to fetch data from
the outside, or persist processed results to somewhere outside of your program.

Incidentally, programmers often shorten "getting data into your program" and "saving data outside
your program" as "input / output", or sometimes even just "I/O".

## Climate data
For the plotting project you've been commissioned to complete, you've been provided with a file
containing monthly global average observations and access to a website for data from individual
countries. You will need to read the global data from the file and
load the country data from the website. Let us begin...


## How to deal with the outside world (**Here be dragons**)

The outside world is a dangerous and scary place. Here, in your Python programming environment you
are relatively safe. But out there lie horrific things like missing files, URLs that point to
nowhere and even... INVALID DATA!!! Luckily Python gives us some mechanisms to help us deal with
this frightening place.

There are, in general, 3 steps to dealing with the outside world:

1. "Open" a resource (could be a file or a URL, or...)
2. "Read" from or "write" to the resource
3. "Close" the resource

Python provides you with the concept of a _context manager_ which handles the "close" step for you.
So we only need worry about opening the correct resource and performing the I/O we need.
The `with` keyword tells Python to _manage a context_
([Documentation](https://docs.python.org/3/reference/datamodel.html#context-managers)). Within this
context (within an indented code block) you're able to read from and write to the resource. As soon as
you're outside of the code block, the resource will not exist any more.
 
Let's see what a context manager looks like with an example:

```python
# Open a file resource...
with open("readfile.txt") as file_resource: # file_resource is a context manager
    # Read from the file resource
    contents = file_resource.read()

# Outside the with block, the context manager has done it's job and closed the file resource.
# We cannot access file_resource now... but we still have the contents!
print(contents)
```

You should see an error message like this:

```
FileNotFoundError: [Errno 44] No such file or directory: 'readfile.txt'
```

This means that Python couldn't find the file you tried to read from. There is no file called `"data/readfile.txt"`
on your computer. Ok, then let's create this file for your program to read using a context manager:

```python
with open("readfile.txt") as file_resource:
    file_resource.write("Hello world")
```

Once again you should see the error message,

```
FileNotFoundError: [Errno 44] No such file or directory: 'readfile.txt'
```

Indeed, the file does not exist. Whats more, we did not ask for permission to write to it. If we have write
permission we will be able to create a new file. You can do this using the `mode` parameter to the
`open()` function like this:

```python
with open("readfile.txt", mode="w") as file_resource:
    file_resource.write("Hello world")
```

This time your code should produce no errors. Now you can try to read from the file. Make sure you
can read the string, `"Hello world"` from the file.

The same context manager approach applies when reading data from a web URL:

```python
# Compatibility code (you don't need to understand the next 4 lines)
import sys
if "pyodide" in sys.modules:
  import pyodide_http
  pyodide_http.patch_all()
# End of compatibility code
from urllib import request

# Open a web resource...
with request.urlopen("https://get.bob.org/1/2/3") as web_resource: # web_resource is a context manager
    # Read from the web resource
    contents = web_resource.read()

# Outside the with block, the context manager has done it's job and closed the web resource.
# We cannot access web_resource now... but we still have the contents!
print(contents)
```

You should see an error message like,

```
urllib.error.URLError: <urlopen error [Errno -2] Name or service not known>
```

OR

```
pyodide.ffi.JsException: NetworkError: A network error occurred.
```

In this case, it is because the resource `"https://get.bob.org/1/2/3"` does not exist. Let's use
a URL that points to a resource that exists this time:

```python
# Compatibility code (you don't need to understand the next 4 lines)
import sys
if "pyodide" in sys.modules:
  import pyodide_http
  pyodide_http.patch_all()
# End of compatibility code
from urllib import request

# Open a web resource...
with request.urlopen("https://httpbin.org/get") as web_resource: # web_resource is a context manager
    # Read from the web resource
    contents = web_resource.read()

# Outside the with block, the context manager has done it's job and closed the web resource.
# We cannot access web_resource now... but we still have the contents!
print(contents)
```

What is printed by this? Is there anything strange about the output? Did you notice
the `b` at the beginning of the output? Continue to the next lesson to find out what
that `b` means.
