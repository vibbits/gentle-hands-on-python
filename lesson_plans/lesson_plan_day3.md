# Day 3: Getting comfortable with Python

## Links

* https://www.climate4you.com/DataSmoothing.htm
* https://climateknowledgeportal.worldbank.org/download-data
* https://hadleyserver.metoffice.gov.uk/hadcrut5/
* https://crudata.uea.ac.uk/cru/data/temperature/

## Objectives

## Materials

## Procedure

### 9:20

**CMD**: Start greeting students as they arrive

### 9:30

**CMD**: Brief introduction while we wait for late students

**SAY**: Today you will become more comfortable with Python. You will continue to use and practice
         everything you've learned so far. We will complete the climate plotting challenge together
         and review your projects.

### 9:40

**CMD**: Most late students should arrive by now, start the refresher quiz

**QUIZ**: Load `day2_intro.pdf` into Big Blue Button.

### 9:50

**CMD**: Start topic: Fetching and storing data

**SAY**: Last week we started working on a new project: plotting climate data. We've been asked
         to plot global climate data, as well as climate data for 3 specific countries: Belgium,
         Russia, and Australia.

**SAY**: The global data is available in a file on your computer, the per-country data is only
         available from a website. In this session we will fetch these data, "clean" it, and
         store the cleaned data.

**SAY**: In order to do any of this though, we have to deal with the strange and scary "outside world".
         The world outside of our Python program. Luckily, Python gives us some mechanisms to help
         working with this frightening place.

**CMD**: Read from the notebook and run and explain the examples.

**SAY**: An important thing to notice here is that, after you have a context manager, the way you
         work with it is the same. If you have a context manager for a file resource, you `read()`
         from it in exactly the same way as you do a web resource.

**SAY**: Let's use this knowledge to explore what the global climate data looks like. To begin with,
         we can expect the file to be quite large, so let's not immediately print the entire contents
         to the screen. Instead let's read a small amount of data (say the first line) using the
         `readline()` function.

**CMD**: Run and explain the example.

**CMD**: Explain the general structure of CSV formatted data.

**CMD**: Read the text description of the data in the notebook. Then run and explain reading the global
         data with `csv`.

**SAY**: This is a great start. You will notice there are a few issues though...

**CMD**: Read from the notebook. Discuss the benefits of using a Python type for representing the date.
         Run the examples and discuss. Also compute a difference between `datetime` objects (to demo
         an advantage of `datetime`): e.g. `datetime(year=2021, month=9, day=1) - datetime(year=1066, month=3, day=1)`

**SAY**: Now you know everything you need to write cleaning and loading functions for the global
         climate data...

**EXERCISE** 8-1, 8-2

**SAY**: The opposite of reading data from a file is, of course, saving the data to a file. In programming
         speak this is known as "writing" to a file (as opposed to "reading" from a file). This is
         accomplished in a very similar way as reading...

**CMD**: Run and explain the example

**SAY**: Naturally, Python's CSV library has a convenient mechanism to write data in correct CSV
         format which we can use to save out cleaned data.

**CMD**: Run and explain writing CSV using `DictWriter`

**SAY**: Now it's your turn to implement a general--purpose function to save our cleaned data...

***EXERCISE**: 8-3

### 11:00

**CMD**: Break

### 11:10

**CMD**: Back from break quiz

**QUIZ**: Load `day3_morning_break.pdf` into Big Blue Button

### 11:15

**CMD**: Topic: Loading data from a web resource

**SAY**: Based on what you've seen already you might consider reading data from a web resource to be
         very straightforward. And you would be right. With one small exception. See if you can spot it.
         
**CMD**: Run (BUT DON'T EXPLAIN YET) the example

**SAY**: Deciphering this error will require us to make a small detour. We will try to exaplain this as well
         as we can but ultimately this is a niche area of programming. You can simply remember the
         phrasing of the error message and apply the trivial fix... when we tell you what that is ;)

**CMD**: Explain the difference between raw bytes and interpretations.

**SAY**: So after all that the fix seems trivial doesn't it? Just pop a `decode()` on the end!

**CMD**: There's also another `splitlines()` added. You can explain about this if time permits:
         `DictReader()` takes a file object or an iterable, so if you pass a string you get results
         single character by character.

**SAY**: So at this point you can implement data cleaning and loading functions for per-country data!

**EXERCISE**: 8-4, 8-5

### 11:30

**CMD**: Topic: data serialisation

**SAY** Before lunch, let's explore data serialisation a little. This morning you've enountered a general-purpose
        data serialisation format that's very popular for tabular structured data. Of course there are many other
        data formats, some general purpose (like CSV or JavaScript Object Notation; JSON) and some special purpose
        like (Word processor documents for storing structured text, executable programs for storing the binary
        representation of programs, or FASTA for storing nucleic acid or amino acid sequences).

**SAY**: Like with CSV, the Python standard library provides a library to help us read and write JSON formatted data.

**CMD**: Run through and explain the examples.

**EXERCISE**: 8-6

**SAY**: The Python standard library does not provide a library to deal with the special purpose FASTA format. Though
         there are of course third-party libraries to do so. Instead you're going to write your own reader for FASTA
         and use the result of your reader to compute GC content.

**CMD**: Explain the structure of FASTA formatted data.

**EXERCISE**: 8-7

### 11:55

**CMD**: Chapter review

### 12:00

**CMD**: Lunch break

### 13:00

**CMD**: Return from lunch

**CMD**: Topic: Visualising data

**SAY**: This is the last section of "theory" in this course, and the first taste of the enormous third-party
         Python "ecosystem". If you're coming from R, you will be familiar with third party packages coming
         from CRAN. In Python, third-party packages generally come from the Python Package Index (PyPI).

**SAY**: At the beginning of the course 2 weeks ago you installed a third-party library called "matplotlib".
         This is probably the most popular library for plotting in Python, though certainly not the only one.
