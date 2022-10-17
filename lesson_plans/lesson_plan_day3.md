# Day 3: Getting comfortable with Python

## Links

* https://www.climate4you.com/DataSmoothing.htm
* https://climateknowledgeportal.worldbank.org/download-data
* https://hadleyserver.metoffice.gov.uk/hadcrut5/
* https://crudata.uea.ac.uk/cru/data/temperature/

## Objectives

## Materials

1. Notebook chapters 7, 8, 9, 10
1. The "How to Design Programs" textbook
1. [Belgium climate data](https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/bel_data_orig.csv)
1. [Australia climate data](https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/aus_data_orig.csv)
1. [Russia climate data](https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/rus_data_orig.csv)

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

**QUIZ**: Load `day3_intro.pdf`

### 9:50 (START: INSTRUCTOR 1)

**SAY**: To help you get back in the groove, lets try an extercise that you can already solve before we tackle
         any new topics.
         
**EXERCISE**: Open special Revision notebook.

**CMD**: Topic: dictionaries

**SAY**: Now that we're finished implementing the Fizz Buzz game, we can tackle a more realistic problem.
         Here is the scenario: we've been comissioned to produce comparative plots of temperature data for
         3 countries and globally from 1901 to 2020: Belgium, Russia, and Australia.

**SAY**: The data we need is publicly available on the internet but from different sources so we will need
         to "clean" it (e.g. ensure dates and times are written in the same way, remove missing data, etc.),
         and align on dates and temperature offsets (and units). You will also need to perform some smoothing
         and finally generate the plots.

**SAY**: This is an ambitious project for new Pythonistas! But I promise we can do it together, with the help
         of Python and it's standard library, one step at a time.

**SAY**: One of the first things we should think about is how to model our data. That is, how to represent
         our data in our program so that it is easy to work with. You might already be thinking about storing
         temperatures in a list, that's not a bad idea. We will need 4 lists: one for each country and 1 for
         the global data. This idea can get very messy though: if we want to add a new country in the future
         we will need another list and modify every function we write to deal with these data. Aligining the
         data on date/time will require us to combine the lists together.

**SAY**: So we could immediately combine the data for a date/time together into a list of tuples perhaps like this:
         `[(BEL1, RUS1, AUS1, GLO1), (BEL2, RUS2, AUS2, GLO2),...]` and so on. Of course we will have to remember
         the ordering ourselves. And if we add another country then that will make remembering order even
         more difficult. We're going in the right direction though. We really need a collection that will allow
         us to associate a name, say "BEL" with a temperature. A tuple does not do this for us but a Python
         dictionary does!

**CMD**: Talk through the image for syntax of a dictionary. Also how to use indexing and the `in` operator. Link
         to how other collections work (e.g. lists from day 2). Also explicitly talk about how to change values
         and add new key/value pairs.

**EXERCISE** 7-1, 7-2

### 10:20

**CMD**: Break

### 10:30 (SWAP TO: INSTRUCTOR 2)

**CMD**: Return from break

**CMD**: Demonstrate looping over a dictionary and the special functions `.items()` and `.values()`

**CMD**: When talking through solutions to exercise 7-3 you can discuss a progression from naive
         solution, to `collections.defaultdict(int)` to `collections.Counter()`.

**EXERCISES**: 7-3, 7-4

**CMD**: Chapter review

### 12:00

**CMD**: Lunch break

### 13:00 (SWAP TO: INSTRUCTOR 1)

**CMD**: Back from lunch

**CMD**: Topic: Fetching and storing data

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

### 14:00

**CMD**: Break

### 14:10 (SWAP TO: INSTRUCTOR 2)

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

**CMD**: Tell Google collab users to download their saved cleaned data files.

### 14:55

**CMD**: Chapter review

### 15:00

**CMD**: Break

### 15:10

**CMD**: Back from break quiz

**QUIZ**: Load `day3_morning_break.pdf` into Big Blue Button.

### 15:15 (SWAP TO: INSTRUCTOR 1)

**CMD**: Topic: Visualising data

**SAY**: At the beginning of the course 2 weeks ago you installed a third-party library called "matplotlib".
         This is probably the most popular library for plotting in Python, though certainly not the only one.
         We can use it to display interactive plots in Jupyter using some special sauce...
         
**CMD**: Run the Jupyter magic code cell: `%matplotlib widget`. If this does not work, ensure students have
         `matplotlib` and `ipympl` packages installed and accessible for Jupyter Lab.

**SAY**: Matplotlib provides a `pyplot` library which is a set of MATLAB like commands for generating plots.
         So the first thing we need to do is import the library.

**SAY**: Now you're ready to create a basic plot.

**CMD**: Explain simple example. Then explain the more complicated samples. Ask students to notice the
         similarities between them.

**CMD**: Explain that there are more plot types available and students
         should look at the matplotlib documentation and examples websites for inspiration.

**SAY**: Now that you understand the basics of using matplotlib for plotting let us try to plot the climate data.
         Luckily, you saved your cleaned climate data earlier so now you can load it and plot it directly...

**CMD**: Read from the notebook...

**SAY**: This looks good so far, but it would be nice to notice long term trends using smoothed data...

**EXERCISE**: 9-1, 9-2

### 16:00

**CMD**: Chapter review

### 16:05

**CMD**: Break and work on projects.

**SAY**: At 16:30 we will begin looking through the projects and ask 2 or 3 of you to present your work.
         If you would like to volunteer to present your work that would be very welcome, please tell one of the
         instructors.

### 16:30

**CMD**: Allow students to present their project work. Possibly work through solutions as necessary.
         This can be a group exercise.

### 16:55

**CMD**: Final word and conclusion of course. Wish everyone good luck. Talk through the conclusion notebook.

### 17:00

**CMD**: Fin
