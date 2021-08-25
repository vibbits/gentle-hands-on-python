# Day 2: Getting to grips with Python

## Objectives

1. Understand the purpose and basic use of the most common collection types in Python: List, Tuple, Dictionary
1. Understand iteration and iteration using collection types
1. Write new functions with less help
1. Fix existing code
1. Reflect on code being written. Can it be improved? Does it need to be improved?

## Materials

1. Notebook chapters 5, 6, 7
1. The "How to Design Programs" textbook

## Procedure

### 9:20

**CMD**: Start greeting students as they arrive

### 9:30

**CMD**: Brief introduction while we wait for late students

**SAY**: Today we will get more in-depth with Python. We will finally play a complete game of FizzBuzz.
         We'll also introduce a new problem to work on. (dum dum dum!!!! It's a secret they'll find out later)

### 9:40

**CMD**: Most late students should arrive by now, start the refresher quiz

**QUIZ**: Load `day2_intro.pdf` into Big Blue Button.

### 10:00

**CMD**: Check the status of the projects. Students should have started.

**CMD**: Go round students asking if they had a chance to work on projects during the week. Any issues they've faced.
         They may switch projects if the one they're working on has lost their interest.

### 10:10

**CMD**: Start topic: Collections of Python values

**SAY**: Using values like a number, text, an image, etc are great and useful. But often we need to collect many of these values
         together. For example, to compute statistics on experimental observations, we need a collection of multiple observations.
         Looking at each observation individual is not useful in this case.

**SAY**: Python gives us a number of ways to store collections of values together. Each with their own characteristics. In this
         session we will look at the **List**, **Tuple**, and **String** collections and apply them to improving our Fizz Buzz
         game.

**SAY**: Let us begin with lists. In your mind this might conjure shopping lists or todo lists. These are very useful metaphores.
         Your shopping list is ordered, that is, it is meaningful to ask what the first item on your shopping list is. So are Python
         lists. Your shopping list can be "nested", for example you might have an item label "Dinner" with a sub-list for items
         you want to use to make dinner tonight. (See example in notebook)

**CMD**: Demo how to write the shopping list example in Python

**SAY**: Here are some other examples of Python lists.

**SAY**: We can use lists to help us with the Fizz Buzz game by using them to represent the progress of the game.

**CMD**: Refresher on the Fizz Buzz game.

**EXERCISE** 5-1

### 10:30

**CMD**: Topic: Slicing

**SAY**: Last week maybe you noticed the use of the _indexing_ operator. If you remember back to the second lesson
         on Functions you used the functions `first` and `rest` on strings. `first` returned the first character of
         a string, and `rest` returned the whole string except the first character. These were implemented using the
         _indexing_ operator (square brackets after a value containing an index). So the first character in a string
         (or first value in a list) is at index 0 and so on.

**SAY**: Well, slicing is a generalisation of indexing. So if you're not confident you understand indexing, don't worry.
         We will practice with it a lot now.

**CMD**: Demo indexing into a list using a few indexes. How to talk about indexes vs the nth element.

**CMD**: Describe slicing from a start-index to an end-index using the examples in the notebook.

**CMD**: Describe indexing and slicing with negative indexes using examples.

**CMD**: Demonstrate the slicing shorthand for "begginning" and "end".

**CMD**: Demo the "step" value in slicing.

**CMD**: Demo replacing values in a slice.

**SAY**: No doubt this seems very confusing. Trying to actually use this technique can help you understand it so lets do an exercise!

**EXERCISE** 5-2

**SAY**: The last attempt we made at writing a function to play Fizz Buzz wasn't very interesting. In order to play to larger numbers
         we would have to type out a longer and longer list. This negates the power of your computer if you can't get to to compute
         for you. So let's have another attempt using slicing. This time well replace the right numbers with either "Fizz" or "Buzz".

**EXERCISE** 5-3

## 11:10

**CMD**: Break

### 11:20

**CMD**: Back from break quiz

**QUIZ**: Load `day2_morning_break.pdf` into Big Blue Button

### 11:25

**CMD**: Topic: Operating on Lists

**SAY**: Python has a rich _standard library_ (a collection of re-usable definitions). You've already used some of this library:
         `abs()`, `print()`, etc are examples of these. This is only scratching the surface though, many more general purpose
         definitions are available to you through the use of `import`.

**SAY**: In the next section we will use the `operator` library. This library provides functions that do the same thing as built in Python
         operators like `+`, `*`, or `[]`.

**CMD**: Run the cell to `import operator`.

**SAY**: In this section we will look at the `sorted()` function, the `in` operator, and the `itemgetter()` function from
         the `operator` library. As the course progresses you will see more of the standard library and the huge array of
         facilities it provides, however we encourage you to explore and see what useful functionality exists. Let's begin now to
         try to understand what these functions and operators do...

**SAY**: Before you run the cells try to guess what the result will be.

**SAY**: The `sorted()` function takes 2 optional arguments that customise its behaviour: `key` is a function used to access the key
         to sort on. And `reverse` is used to sort in reverse order.

**CMD**: Read and demo from notebook about the `key` argument.

**SAY**: Once again, here is a chance to try to understand how to use these functions by putting them to use.

**EXERCISE** 5-4, 5-5

### 12:00

**CMD**: Topic: Tuples and Strings

**SAY**: Practically, tuples are almost exactly like lists except that they're _immutable_. Meaning that, once they're defined you
         cannot change them. As you might imagine this simple difference has all sorts of consequences but they're out of scope for this
         course.

**CMD**: Run through demos of tuple indexing and conversion

**SAY**: Practically, strings are almost exactly like tuples except you cannot store arbitrary values in strings: no, you can only store
         characters. This is just a different way of looking at text data that allows you to see that indexing and slicing also make sense.

**EXERCISE** 5-6

### 12:20

**CMD**: Chapter review

### 12:30

**CMD**: Lunch break

### 13:30

**CMD**: Return from lunch break quiz

**QUIZ**: Load `day2_after_lunch.pdf` into Big Blue Button

### 13:35

**CMD**: Topic: for-each loops

**SAY**: Think about a time you had to repeat a set of instructions many times. For example, you're pipetting
         and writing down measurements or renaming files according to a naming scheme. How easy is it to make
         a mistake? How focused did you need to be? How quickly did you become tired or bored of the repetition?
         This is a problem computers do not have. Provided you, the programmer, have described the steps correctly,
         a computer will execture them quickly, and accurately for as long as necessary.

**SAY**: The Fizz Buzz game we've been trying to play requires the computer to count up to some maximum number.
         Each of our implementations so far has required you, the programmer, to write down the steps for every
         single number. We've not used this special power that computers have: to repeat steps.

**SAY**: This is how you might expect to be able to describe the Fizz Buzz game to a computer:

**CMD**: Say this...
```
STEP  1: SET VARIABLE COUNTER TO 1
STEP  2: CHECK IF COUNTER IS A MULTIPLE OF 5 OR 3
STEP  3: IF SO, SAY "FIZZ BUZZ"
STEP  4: CHECK IF COUNTER IS A MULTIPLE OF 3
STEP  5: IF SO, SAY "FIZZ"
STEP  6: CHECK IF COUNTER IS A MULTIPLE OF 5
STEP  7: IF SO, SAY "BUZZ"
STEP  8: CHECK IF WE HAVE FINISHED COUNTING
STEP  9: IF SO, STOP
STEP 10: INCREMENT COUNTER
STEP 11: GO TO STEP 2
```

**SAY**: The only part we're still mmissing is the ability to say, `GO TO STEP 2`. This is what a _loop_ does.
         You can think `GO TO STEP 2` as creating a control-flow loop. Steps 2-9 are looped until the stop
         condition is met.

**SAY**: The loop construct we'll be looking at with here is known as the _for-each loop_. It's called this
         because it allows us to repeat a set of instructions _for each_ member of a collection. For example,
         here we have a list of numbers...

**CMD**: Explain the syntax of a **for** loop. Then explain the loop by unrolling it.

**SAY**: Now try to implement Fizz Buzz using your new loop knowledge.

**EXERCISE** 6-1

**SAY**: You might think it was unfair of me to say that a loop will save you having to explicitly tell
         the computer what to do at each step since you had to literally type out all of the numbers
         that need to be counted. Well at least you didn't write out 15 `if`/`elif`/`else` blocks so you
         can be more confident that your logic is correct. But it is unfortunate that you needed to
         write out the numbers your game is supposed to count. So let's fix that next...

**SAY**: The `range()` function from the standard library generates a range of numbers for you. Let's
         experiment with using `range()` in a for-each loop.

**CMD**: Run through the examples and describe each parameter as they are used. It may be useful
         to draw the analogy between `range()` arguments and slicing.

**SAY**: Finally, you now have everything you need to satisfyingly implement a program that plays
         Fizz Buzz...

**EXERCISE** 6-2

### 14:20

**CMD** Break

### 14:30

**QUIZ**: Load `day2_afternoon.pdf` into Big Blue Button.

### 14:40

**SAY**: In order to practice using and reading for-each loops, try to solve the next 3 exercises.

**EXERCISES** 6-3, 6-4, 6-5

### 15:20

**SAY** Before we finish up with loops I want to introduce you to one more member of the Python
        standard tool belt: "ZIP"! What problem does this solve?
        Imagine you have 2 collections with element you wish to process in your loop at the same time...

**CMD**: Walk through description in the notebook and sequence identity example

**EXERCISES**: 6-6, 6-7

### 15:50

**CMD**: Chapter review

### 16:00

**CMD**: Topic: dictionaries

**SAY**: Now that we're finished implementing the Fizz Buzz game, we can tackle a more realistic problem.
         Here is the scenario: we've been comissioned to produce comparative plots of temerature data for
         3 countries and globally from 1901 to 2020: Belgium, Russia, and Australia.

**SAY**: The data we need is publicly available on the internet but from different sources so we will need
         to "clean" it (e.g. ensure dates and times are written in the same way, remove missing data, etc.),
         and align on dates and temperature offsets (and units). You will also need to perform some smoothing
         and finally generate the plots.

**SAY**: This is an abbitious project for new Pythonistas! But I promise we can do it together, with the help
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
         to how other collections work.

**EXERCISE** 7-1, 7-2

**CMD**: Demonstrate looping over a dictionary and the special functions `.items()` and `.values()`

**EXERCISES**: 7-3, 7-4, 7-5

### 16:50

**CMD**: Chapter review

**SAY**: Another very big day today. We've covered a lot of very new concepts. Please tell one of us instructors
         if you are struggling. Next week we will continue to work on this climate plotting project. We will
         also share your work on the other projects. Please try to spend a couple of hours this week working on them
         before the next session.

### 17:00

**CMD**: Fin
