# Parsing data formats

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

You will likely need to work with various data formats; tabular data (e.g. CSV or Excel), image
data (e.g. PNG or TIFF), structured data (e.g. JSON or YAML), or a multitude of other possibilities.

While you could (as in it is possible) to write your own programs to parse any data format you
might encounter, this isn't a reasonable expectation and probably not the best use of your time.
Instead, your programming language is likely to provide a module that you can use.

In the previous section you parsed CSV formatted data, Python provides a standard library module
called `csv` for reading and writing CSV data. There are many third-party modules for working with
other formats too. But those are out of scope for this course. If you need to work with another
data format we encourage you to contact us for pointers.

## Global climate data

The [HadCRUT](https://www.metoffice.gov.uk/hadobs/hadcrut5/) website describes what the CSV file you
parsed contains. The column headers are:

  1. Year-Month labels
  2. 'Best-estimate' computed monthly means from 200 ensemble measurements as difference from 1961-1990 reference period.
  3. 2.5% confidence from 200 ensemble measurements.
  4. 97.5% confidence from 200 ensemble measurements.

Although CSV is a conceptually simple data format it can be difficult to read and write _correctly_.
The Python standard library provides a module (called `csv`) to help you to easily read and write
this format. Let's use this library to read the global data (you can type or paste the code below into
the console above):

```python
#### You DO NOT need to understand this part ####
# It is here only to make this example work in  #
# the web console. If you're running this       #
# in VSCodium you should not copy this area!    #
#      THIS IS ONLY FOR THE WEB CONSOLE         #
from pyodide.http import open_url
def open(filename):
    return open_url(f"https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/{filename}")
#################################################
# Everything after here you can run on your     #
# laptop with VSCodium.                         #

import csv

global_data = []
with open("HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv") as global_data_manager:
    read_data = global_data_manager.read().splitlines()
    reader = csv.DictReader(read_data)
    
    for reading in reader:
        global_data = global_data + [reading]

global_data[:5]
```

The output contains the first 5 data rows of the global data table. You should notice that it's a list
of dictionaries similar to what you produced yourself in the last exercise!

The `csv` module provides a `DictReader` function that accepts anything that can be looped over to
produce _rows_ from the CSV data. So I first read all the data from the file resource, then
I turned it into a list of strings with `splitlines()`, one string for each line of the file.
These lines are the _rows_ that `DictReader` needs. I can then loop over the `reader` which gives
me a dictionary for each row of the data. These dictionaries I add to a list of data.

This is a great start. The next step is to clean these data up a little. Here are a few things we
can do to make them easier to work with:

1. Convert the temperature values from strings to numbers
1. Use a `datetime` object to record the time rather than a string
1. The confidence interval is not interesting for us at the moment so we can discard those.

## Parsing date and time data

First, what is a `datetime` object? Python provides a module for dealing with dates, times,
timezones, and differences between times in the standard library. See the documentation
[here](https://docs.python.org/3/library/datetime.html). Or especially
the section on format codes
[here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

```python
from datetime import datetime

# An example of a date from the data is the string "1901-5"
date1 = datetime.strptime("1901-05", "%Y-%m")
print("Year:", date1.year, "Month:", date1.month, "Day:", date1.day, "day of the week:", date1.weekday()) # Monday is 0
```

```python
# An example of a date from the data is the string "1901-May"
date1 = datetime.strptime("1901-May", "%Y-%b")
print("Year:", date1.year, "Month:", date1.month, "Day:", date1.day, "day of the week:", date1.weekday()) # Monday is 0
```

```python
# An example of a parsing error:
datetime.strptime("May 1901", "%Y-%b")
```

