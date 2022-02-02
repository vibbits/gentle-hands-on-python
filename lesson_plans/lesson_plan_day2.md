# Day 2: Getting to grips with Python

## Objectives

1. Understand the purpose and basic use of the most common collection types in Python: List, Tuple
1. Understand iterating over collection types
1. Write new functions with less help
1. Fix existing code
1. Reflect on code being written. Can it be improved? Does it need to be improved?

## Materials

1. Notebook chapters 5, 6
1. The "How to Design Programs" textbook

## Procedure

### 9:20

**CMD**: Start greeting students as they arrive

### 9:30

**CMD**: Brief introduction while we wait for late students

**SAY**: Today we will get more in-depth with Python. We will finally play a complete game of FizzBuzz.
         We'll also introduce a new problem to work on. (dum dum dum!!!! It's a secret they'll find out later)

### 9:40

**CMD**: Check the status of the projects. Students should have started.

**CMD**: Go round students asking if they had a chance to work on projects during the week. Any issues they've faced.
         They may switch projects if the one they're working on has lost their interest.

### 9:50

**CMD**: Most late students should arrive by now, start the refresher quiz

**QUIZ**: Load `day2_intro.pdf` into Big Blue Button.

### 10:00

**CMD**: Start topic: Collections of Python values

**SAY**: Using values like a number, text, an image, etc are great and useful. But often we need to collect
         many of these values together. For example, to compute statistics on experimental observations, we
         need a collection of multiple observations. Looking at each observation individually is not useful
         in this case.

**SAY**: Python gives us a number of ways to store collections of values together. Each with their own
         characteristics. In this session we will look at the **List**, **Tuple**, and **String** collections
         and apply them to improving our Fizz Buzz game.

**SAY**: Let us begin with lists. In your mind this might conjure shopping lists or todo lists. These are
         very useful metaphores. Your shopping list is ordered, that is, it is meaningful to ask what the
         first item on your shopping list is. So are Python lists. Your shopping list can be "nested", for
         example you might have an item label "Dinner" with a sub-list for items you want to use to make
         dinner tonight. (See example in notebook)

**CMD**: Demo how to write the shopping list example in Python

**SAY**: Here are some other examples of Python lists.

**SAY**: You can combine the assignment operator and the addition operator together as a shorthand for addition and
         then assignment.

**SAY**: We can use lists to help us with the Fizz Buzz game by using them to represent the progress of the game.

**CMD**: Refresher on the Fizz Buzz game.

**EXERCISE** 5-1

### 10:20

**CMD**: Topic: Slicing

**SAY**: Slicing is a generalisation of indexing. So if you're not confident you understand indexing, don't worry.
         We will practice with it a lot now.

**CMD**: Demo indexing into a list using a few indexes. How to talk about indexes vs the nth element.

**CMD**: Describe slicing from a start-index to an end-index using the examples in the notebook.

**CMD**: Describe indexing and slicing with negative indexes using examples.

**CMD**: Demonstrate the slicing shorthand for "beginning" and "end".

**CMD**: Demo the "step" value in slicing.

**CMD**: Demo replacing values in a slice.

**SAY**: No doubt this seems very confusing. Trying to actually use this technique can help you understand it so lets do an exercise!

**EXERCISE** 5-2

**SAY**: The last attempt we made at writing a function to play Fizz Buzz wasn't very interesting. In order
         to play to larger numbers we would have to type out longer and longer lists. This negates the power
         of your computer if you can't get to to compute for you. So let's have another attempt using slicing.
         This time we'll replace the right numbers with either "Fizz" or "Buzz".

**EXERCISE** 5-3

## 11:00

**CMD**: Break

### 11:10

**CMD**: Back from break quiz

**QUIZ**: Load `day2_morning_break.pdf` into Big Blue Button

### 11:15

**CMD**: Topic: Operating on Lists

**SAY**: Python has a rich _standard library_ (a collection of re-usable definitions). You've already used
         some of this library: `abs()`, `print()`, etc are examples of these. This is only scratching the
         surface though, many more general purpose definitions are available to you through the use of `import`.

**SAY**: In the next section we will use the `operator` library. This library provides functions that do
         the same thing as built in Python operators like `+`, `*`, or `[]`.

**CMD**: Run the cell to `import operator`.

**SAY**: In this section we will look at the `sorted()` function, the `in` operator, and the `itemgetter()`
         function from the `operator` library. As the course progresses you will see more of the standard
         library and the huge array of facilities it provides, however we encourage you to explore and see
         what useful functionality exists. Let's begin now to try to understand what these functions and
         operators do...
         
**SAY**: Before you run the cells try to guess what the result will be.

**CMD**: Run the example cells.

**SAY**: The `sorted()` function takes 2 optional arguments that customise its behaviour: `key` is a
         function used to access the key to sort on. And `reverse` is used to sort in reverse order,
         it should be `True` or `False`.

**CMD**: Read and demo from notebook about the `key` argument.

**SAY**: Once again, here is a chance to try to understand how to use these functions by putting them to use.

**EXERCISE** 5-4, 5-5

### 11:45

**CMD**: Topic: Tuples and Strings

**SAY**: Practically, tuples are almost exactly like lists except that they're _immutable_. Meaning that,
         once they're defined you cannot change them. As you might imagine this simple difference has all
         sorts of consequences but they're out of scope for this course.

**CMD**: Run through demos of tuple indexing and conversion

**SAY**: Practically, strings are almost exactly like tuples except you cannot store arbitrary values in
         strings: no, you can only store characters. This is just a different way of looking at text data
         that allows you to see that indexing and slicing also make sense.

**EXERCISE** 5-6, 5-7

### 11:55

**CMD**: Chapter review

**SAY**: The supporting material at the end of each chapter is there to support your own learning.
         Make sure you take some time to browse through it, especially if you're having trouble
         understanding any part of what we're explaining.

### 12:00

**CMD**: Lunch break

### 13:00

**CMD**: Return from lunch break quiz

**QUIZ**: Load `day2_after_lunch.pdf` into Big Blue Button

### 13:05

**CMD**: Topic: for-each loops

**SAY**: Think about a time you had to repeat a set of instructions many times. For example, you're pipetting
         and writing down measurements or renaming files according to a naming scheme. How easy is it to make
         a mistake? How focused did you need to be? How quickly did you become tired or bored of the repetition?
         This is a problem computers do not have. Provided you, the programmer, have described the steps correctly,
         a computer will execture them quickly, and accurately for as long as necessary.

**SAY**: The Fizz Buzz game we've been trying to play requires the computer to count up to some maximum number.
         Each of our implementations so far has required you, the programmer, to write down the steps for every
         single number. We've not used this special power that computers have: to repeat steps.

**SAY**: The loop construct we'll be looking at here is known as the _for-each loop_. It's called this
         because it allows us to repeat a set of instructions _for each_ member of a collection.
         For example, here we have a list of numbers...

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

### 14:30

**CMD** Break

### 14:40

**QUIZ**: Load `day2_afternoon.pdf` into Big Blue Button.

**SAY**: In order to practice using and reading for-each loops, try to solve the next 3 exercises.

**EXERCISES** 6-3, 6-4, 6-5

**SAY** Before we finish up with loops I want to introduce you to one more member of the Python
        standard tool belt: "ZIP"! What problem does this solve?
        Imagine you have 2 collections with elements you wish to process in your loop at the same time...

**CMD**: Walk through description in the notebook and sequence identity example.

**EXERCISES**: 6-6, 6-7

### 16:45

**CMD**: Chapter review

**SAY**: Another very big day today. We've covered a lot of very new concepts.
         Please tell one of us instructors if you are struggling. Next week we
         will continue to work on this climate plotting project. We will
         also share your work on the other projects. Please try to spend a
         couple of hours this week working on them before the next session.

**SAY**: By the way. You can now, officially, call yourselves programmers :) That doesn't
         mean you should ignore the rest of the course. But you should now know enough
         to build useful programs.
         
### 17:00

**CMD**: Fin
