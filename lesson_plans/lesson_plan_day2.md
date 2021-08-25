# Day 2: Getting to grips with Python

## Links

## Objectives

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

**CMD**: Topic: Looping: Doing something repeatedly

