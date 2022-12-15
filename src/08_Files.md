---
title: "Files"
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

# Fetching and storing data

In this chapter we will consider 2 sources of data: the internet and the filesystem of your own computer. We will also look at storing
your data to the filesystem of your computer. More often than not the data you need for your program will come from somewhere outside
of your program. Often, that "somewhere" will be a file or some location on the internet. Especially for more complex data, it becomes
essential to be able to fetch data from the outside, or persist data to somewhere outside of your program.

## Climate data
For the plotting project you've been commissioned to complete, you've been provided with a file containing monthly global average
observations and access to a website for data from individual countries. You will need to read the global data from the file and
load the country data from the website. Let us begin...


## How to deal with the outside world (**Here be dragons**)

The outside world is a dangerous and scary place. Here, in your Python programming environment you are relatively safe. But out
there lie horrific things like missing files, URLs that point to nowhere and even... INVALID DATA!!! Luckily Python gives us
some mechanisms to help us deal with this frightening environment.

There are, in general, 3 steps to dealing with the outside world:

1. "Open" a resource (could be a file or a URL, or...)
2. "Read" from or "write" to the resource
3. "Close" the resource

Python provides us with the concept of a _context manager_ which handles the "close" step for us. So we only need worry about
opening the correct resource and performing the I/O we need. The `with` keyword tells Python to _manage a context_
([Documentation](https://docs.python.org/3/reference/datamodel.html#context-managers)). Within this context (within an indented
code block) you're able to read from and write to the resource. As soon as you're outside of the code block, the resource will
not exist any more.
 
Let's see what a context manager looks like with an example reading from file and web resources...

::: {.cell .code}
```python
# Open a file resource...
with open("data/readfile.txt") as file_resource: # file_resource is a context manager
    # Read from the file resource
    contents = file_resource.read()

# Outside the with block, the context manager has done it's job and closed the file resource.
# We cannot access file_resource now... but we still have the contents!
print(contents)
```
:::

::: {.cell .code}
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
:::

These are "Happy paths" through your program where we _know_ the resources exist, saving exceptional circumstances.
Before we move on, let us observe what happens in a couple of "Unhappy paths" where errors occur.

::: {.cell .code}
```python
# Open a file that does not exist
with open("this-file-does-not-exist.txt") as file_resource:
    contents = file_resource.read()

print(contents)
```
:::

::: {.cell .code}
```python
# Read from a file after the context manager has closed it
with open("data/readfile.txt") as file_resource:
    pass

contents = file_resource.read()
print(contents)
```
:::


## Explore the global data

In order to understand how to use the data in a file, we need to understand what's in it. As you saw above, the `read()`
function reads all the data from the file. The global data file is probably quite large though so let's try to see just the beginning.
We have 2 options: The `readline()` function will read up to a new line character, or we could pass an argument to the
`read()` function that is the number of characters to read.

::: {.cell .code}
```python
with open("data/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv") as global_data_manager:
    first_line = global_data_manager.readline()
    second_line = global_data_manager.readline()
    
print(first_line + second_line)
```
:::

You may've guessed based on the extension that this is tabular data in "comma-separated values (CSV)" format.
If not, then you can tell by the structure of the data we've read.

The [HadCRUT](https://www.metoffice.gov.uk/hadobs/hadcrut5/) website describes what we're looking at. Column,

  1. Year-Month labels
  2. 'Best-estimate' computed monthly means from 200 ensemble measurements as difference from 1961-1990 reference period.
  3. 2.5% confidence from 200 ensemble measurements.
  4. 97.5% confidence from 200 ensemble measurements.

Although CSV is a conceptually simple data format it can be difficult to read and write _correctly_. The Python standard library
provides a module (called `csv`) to help us easily read and write this format. Let's use this library to read the global data...

::: {.cell .code}
```python
import csv

global_data = []
with open("data/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv") as global_data_manager:
    read_data = global_data_manager.read().splitlines()
    reader = csv.DictReader(read_data)
    
    for reading in reader:
        global_data = global_data + [reading]

global_data[:5]
```
:::

This is a great start. The next step is to clean these data up a little. Here are a few things we can do to make them easier to work with:

1. Convert the temperature values from strings to numbers
1. Use a `datetime` object to record the time rather than a string
1. The confidence interval is not interesting for us at the moment so we can discard those.

First, what is a `datetime` object? Python provides a module for dealing with dates, times, timezones, and differences between
times in the standard library. See the documentation [here](https://docs.python.org/3/library/datetime.html). Or especially
the section on format codes [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

::: {.cell .code}
```python
from datetime import datetime

# An example of a date from the data is the string "1901-5"
date1 = datetime.strptime("1901-05", "%Y-%m")
print("Year:", date1.year, "Month:", date1.month, "Day:", date1.day, "day of the week:", date1.weekday()) # Monday is 0
```
:::

::: {.cell .code}
```python
# An example of a date from the data is the string "1901-May"
date1 = datetime.strptime("1901-May", "%Y-%b")
print("Year:", date1.year, "Month:", date1.month, "Day:", date1.day, "day of the week:", date1.weekday()) # Monday is 0
```
:::

::: {.cell .code}
```python
# An example of a parsing error:
datetime.strptime("May 1901", "%Y-%b")
```
:::

---

### Exercise 8-1: Clean the data!

Write a function to _clean_ the data we read from the file. The input to your function will be a dictionary like this:

```python
{
  'Time': '1901-05',
  'Anomaly (deg C)': '-0.24934465',
  'Lower confidence limit (2.5%)': '-0.44425672',
  'Upper confidence limit (97.5%)': '-0.05443258'
}
```

The output of your function should look like this:

```python
{
  'Time': datetime.datetime(1901, 5, 1, 0, 0),
  'Temperature': -0.24934465
}
```

::: {.cell .code}
```python
def clean_global_data(reading):
    ""
    return _

assert clean_global_data({'Time': '1901-05','Anomaly (deg C)': '-0.24934465','Lower confidence limit (2.5%)': '-0.44425672','Upper confidence limit (97.5%)': '-0.05443258'}) == {'Time': datetime(1901, 5, 1, 0, 0),'Temperature': -0.24934465}
```
:::

[Advanced question](Advanced%20Exercises.ipynb#8-1)

---

### Exercise 8-2: Load the data

Write a function that reads the global temperature data file and returns a list of cleaned dictionaries.

::: {.cell .code}
```python
def global_data(filename):
    ""
    return _

assert global_data("data/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv")[4] == {'Time': datetime(1901, 5, 1, 0, 0),'Temperature': -0.24934465}
```
:::

---

## Saving data for later

At this point you may wish to save your cleaned data for later inspection or use. The resource workflow of:
`open`, `write`, `close` is the same as before. Let's see what this looks like in general:

::: {.cell .code}
```python
# Open a file resource...
with open("test.txt", mode="w") as file_resource: # file_resource is a context manager. Notice the extra mode="w"
    # Write to the file resource
    file_resource.write("Hello outside world!")

# Outside the with block, the context manager has done it's job and closed the file resource.
# We cannot access file_resource now... but we still have the contents!
```
:::

Now you should be able to find a file called "test.txt" in the file browser on the left of this notebook.

Naturally, the CSV library allows us to write correct CSV formatted data without the hastle...

::: {.cell .code}
```python
with open("test.csv", mode="w") as file_resource:
    writer = csv.DictWriter(file_resource, fieldnames=["Time", "Temperature"])
    writer.writeheader()
    writer.writerows(global_data("data/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv"))
```
:::

---

### Exercise 8-3: Save the data!

Write a function that takes a list of dictionaries as an argument and saves them to a CSV formatted file.

::: {.cell .code}
```python
def save_data(data, filename):
    ""
    _

glo = global_data("data/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv")
save_data(glo, "data/global_data.csv")
```
:::

---

## Exploring the per-Country data

Drawing on our exploration of the global data (which we had in a local file), let's explore the pre-country data. The only difference this time is that the data is coming from a web resource rather than a file resource.

::: {.cell .code}
```python
# https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2020/BEL/Belgium
import csv

bel_data = []
with request.urlopen("https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/bel_data_orig.csv") as bel_data_manager:
    read_data = bel_data_manager.read().splitlines()
    reader = csv.DictReader(read_data)
    
    for reading in reader:
        bel_data = bel_data + [reading]

bel_data[:5]
```
:::

**An Error!** This one is a bit difficult to decipher without introducing you to another data type: `bytes`.

Very often the files on your computer (or on remote computers) aren't just plain text (like CSV is), instead their data is
serialised (stored) as binary numbers that have to be interpreted differently than text.

* Here is a number as we would write it in base 10 (decimal): `65`.
* Here is that number as it is written in a string: `"65"`.
* Here is that number as a computer would write it in base 2 (binary): `01000001`
* If I interpret this pattern of bytes as a character I get, `" "`
* Here is that number as a computer would see the string representation without interpreting the data as text: `0011011000110101`
* If I interpret this pattern of bits as a decimal number I get: `13877` 

At some level, all you're doing as a programmer is interpreting patterns of bytes. The data you read has no interpretation other
than what you impose on in, you must tell the computer how we want to interpret it:

::: {.cell .code}
```python
bin(65) # Binary representation of the decimal integer 32
```
:::

::: {.cell .code}
```python
int(65).to_bytes(1, byteorder='big').decode() # The integer 32 interpreted as a string
```
:::

::: {.cell .code}
```python
int.from_bytes("65".encode(), byteorder='big') # The string "32" interpreted as an integer
```
:::

Hopefully this gives you some sense of what the `Error: iterator should return strings, not bytes (did you open the file in text mode?)`
means. The Python `CSV` library expects text but we're trying to give it uninterpreted bytes. So the solution now seems rather
trivial: add a `.decode()`!

::: {.cell .code}
```python
# https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2020/BEL/Belgium
import csv 
bel_data = []
with request.urlopen("https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/bel_data_orig.csv") as bel_data_manager:
    text_data = bel_data_manager.read().decode().splitlines()
    reader = csv.DictReader(text_data)
    
    for reading in reader:
        bel_data = bel_data + [reading]

bel_data[:5]
```
:::

---

### Exercise 8-4: Clean the data!

Write a function to clean the country data we read from the web. The input to your function will be a dictionary like this:

```python
{
  'Temperature - (Celsius)': '5.76',
  'Year': '1901',
  'Statistics': 'May Average',
  'Country': 'Belgium',
  'ISO3': 'BEL'
}
```
The output of your function should look like this:

```python
{
  'Time': datetime.datetime(1901, 5, 1, 0, 0),
  'Temperature': 5.76
}
```

::: {.cell .code}
```python
def clean_country_data(data):
    ""
    return _

assert clean_country_data(bel_data[0]) == {'Time': datetime(1901, 1, 1, 0, 0), 'Temperature': 4.04}
```
:::

---

### Exercise 8-5: Load country data

Write a function that accepts a URL and returns a list of dictionaries containing 'Time' and 'Temperature' keys. Use the second
code cell to save the cleaned data using the `save_data()` function you wrote earlier.

::: {.cell .code}
```python
def country_data(url):
    ""
    return _

assert country_data("https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/bel_data_orig.csv")[4] == {'Time': datetime(1901, 5, 1, 0, 0),'Temperature': 9.15}
assert country_data("https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/rus_data_orig.csv")[4] == {'Time': datetime(1901, 5, 1, 0, 0),'Temperature': 2.01}
assert country_data("https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/aus_data_orig.csv")[4] == {'Time': datetime(1901, 5, 1, 0, 0),'Temperature': 18.02}
```
:::

::: {.cell .code}
```python

```
:::

---

## Chapter Review

In this chapter we started working with files. We learned how to open a file and read its contents. We also learned how
to write data to a file.

1. What does the `open()` function do?
<details>
    <summary>Answer</summary>
    It makes an external resource such as a file or remote web URL available for <code>read()</code>ing and <code>write()</code>ing.
</details>


2. If you open a file with the mode argument set to `"w"`, can you read data from the file?
<details>
    <summary>Answer</summary>
    No. <code>"w"</code> means you can only <em>write</em> to the file.
</details>


3. If you open an existing file with `mode="w"` and write to it, what happens to the original data?
<details>
    <summary>Answer</summary>
    It's gone.
</details>


4. How do you read the entire contents of a file into a string?
<details>
    <summary>Answer</summary>
    Run the <code>read()</code> function on the context manager.
</details>


5. How would you access line 5 of a file?
<details>
    <summary>Answer</summary>
    Call the <code>readline()</code> function 5 times, ignoring the returned string the first 4 times.
</details>

6. What is the difference between <code>bytes</code> and <code>str</code> types?
<details>
    <summary>Answer</summary>
    <code>bytes</code> are uninterpreted bits if computer memory. <code>str</code> are those bytes interpreted as text.
</details>

## Next session

Go to our [next chapter](09_Plotting.ipynb).
