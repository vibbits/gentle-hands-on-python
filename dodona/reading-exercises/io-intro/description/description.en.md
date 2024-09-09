# Fetching and storing data


<div style="display:flex; align-items:center; justify-content:center; width:100%; height: 15rem; background-color:lightsteelblue">
Video placeholder
</div>

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>


In this section you  will use 2 sources of data: the internet and files on your own computer.
You will also find out how to store data onto your computer.

<!--<img src="media/92v52l.jpg" alt="Programmers accessing data" style="width:95%;height:auto">-->
![Programmers accessing data](media/92v52l.jpg)

More often than not, the data you need for your program will
come from somewhere outside of your program. Often, that "somewhere" will be a file or some location
on the internet. Especially for more complex data, it becomes essential to be able to fetch data from
the outside, or store processed results somewhere outside of your program.

Incidentally, programmers often shorten "getting data into your program" and "saving data outside
your program" as "input / output", or sometimes even just "I/O".

## Climate data
For the plotting project you've been commissioned to complete, you've been provided with a file
containing monthly global average observations and access to a website for data from individual
countries. You will need to read the global data from the file and
load the country data from the website. This is the raw first ten lines of that file:

```
Time,Anomaly (deg C),Lower confidence limit (2.5%),Upper confidence limit (97.5%)
1901-01,-0.28059345,-0.43856356,-0.122623324
1901-02,-0.26819772,-0.42274347,-0.113651976
1901-03,-0.20081724,-0.36103362,-0.040600866
1901-04,-0.1753031,-0.35032505,-0.00028113974
1901-05,-0.24934465,-0.44425672,-0.05443258
1901-06,-0.23662645,-0.43364984,-0.039603047
1901-07,-0.3289457,-0.51798207,-0.13990928
1901-08,-0.2050631,-0.42178407,0.0116578685
1901-09,-0.35517338,-0.53581136,-0.1745354
```


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
context (within an indented code block) you're able to read from and/or write to the resource. As soon as
you're outside of the code block, the resource will not exist any more (it will be closed).
 
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

If you run this in the console above or in your own development environment, you should see an
error message like this:

```
FileNotFoundError: [Errno 44] No such file or directory: 'readfile.txt'
```

This means that Python couldn't find the file you tried to read from. There is no file called
`"readfile.txt"` in the folder you're working from. Ok, then let's create this file for your
program to read using a context manager:

```python
with open("readfile.txt") as file_resource:
    file_resource.write("Hello world")
```

If you run this, once again you should see the error message,

```
FileNotFoundError: [Errno 44] No such file or directory: 'readfile.txt'
```

Indeed, the file does not exist. Whats more, we did not ask for permission to write to it. If we
have write permission we will be able to create a new file. You can do this using the `mode` parameter
to the `open()` function like this:

```python
with open("readfile.txt", mode="w") as file_resource:
    file_resource.write("Hello world")
```

This time your code should produce no errors. Now you can try to read from the file. Make sure you
can read the string, `"Hello world"` from the file.

The same context manager approach applies when reading data from a web URL:

```python
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

OR, if you're running this in the console above rather than a local development environment,

```
pyodide.ffi.JsException: NetworkError: A network error occurred.
```

You get this error because the resource `"https://get.bob.org/1/2/3"` does not exist.
To confirm this, you can try to visit it with your web-browser if you like. Let's use
a URL that points to a resource that exists this time:

```python
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
