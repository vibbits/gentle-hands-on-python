# Day 1: Introduction to programming and Python

## Links

* Custom video explaining setup: https://youtu.be/hmI8YIejVcQ
* Anaconda install: https://www.youtube.com/watch?v=5mDYijMfSzs
* Jupyter Notebook tutorial: https://youtu.be/p1PKGDz0Y6A

## Objectives

1. Understand what the "building blocks" or programming are, and how they are "glued" together?
1. Evaluate some simple Python expressions on various data types.
1. Recognise error messages, comprehend them, and fix the problem they're describing.
1. Understand what a variable is how how to use them.
1. How to perform some simple I/O with `input()` and `print()`.

## Materials

1. Jupyter and the "Basics", "Functions", and "Conditions" notebooks.
1. The "How to Design Programs" textbook.

## Procedure

**09:20** Start greeting students as they arrive

**09:30** Slow Introduction. Introduce trainers, the course, what to expect.

**09:40** Most late students should arrive by now.

CMD: Explain that online learning is different from classroom learning. It's difficult for trainers to notice that students are struggling
     and it's difficult to interact like we might in a classroom. Therefore we would like to get as much interaction as possible via voice
     and video. Ask students to turn on their microphones and cameras and introduce themselves.
    

**10:00** Learning environment setup

CMD: Demonstrate downloading and installing Anaconda and starting Jupyter Labs. Video: https://youtu.be/hmI8YIejVcQ
     Otherwise, introduce Google Collab for those with a google account.
     Special mention if anyone is using GNU/Linux: they need not use anaconda. Just `pip install jupyterlab matplotlib ipympl`.
     Special alternative: Idle with a regular Python install, replit.com (whatever student is comfortable with). Python can be installed
       from the Microsoft store on Windows 10:  https://www.youtube.com/watch?v=yXfCq4xzrrI&t=19s (Be careful: says Python 3.7)
    

**10:20** The basics of programming and computing.

SAY: By way of providing you with some background. Our objective for the first 2 sessions
     today is to provide you with a way of thinking about programming and computing in general.
     The ideas we want to present to you apply to all programming and programming languages
     even though we will be using Python for examples. So for those of you who are already familiar
     with R or other programming languages, we hope you will still find these 2 sessions useful.
     
SAY: A note for those of you who are already confident programmers. This morning
     may feel slow for you. We're covering the basics. Feel free to read ahead and complete the advanced
     exercises. If you are a new programmer please follow along with me. There are
     a lot of new concepts that we will cover today and you will feel exhausted
     soon enough. We need not rush.

CMD: Read out the quote from "How to Design Programs"

> When you were a small child, your parents taught you to count
> and perform simple calculations with your fingers [..]. They
> would ask "what's 3 + 2?" and you would count off the fingers
> on one hand. They programmed and you computed. And in some
> way, that's really all there is to programming and computing.

SAY: Now we're going to do some programming in the same way. We'll
     ask some simple arithmetic questions, and the computer will compute
     the answers and print the results. That's how simple programming is.
     You ask questions of your programming environment (in this case, Python),
     and it computes for you.
     
RUN: With the students, explain again how to execute a cell and verify each answer.
     Also explain what `abs()` is doing.
     
SAY: The first cell here just contains a number. Run it. What happens? Yes, numbers
     evaluate to themselves. `1` evaluates to `1`. `256` evaluates to `256`. When you
     execute a cell containing a more complicated expression, like `3 + 2` a similar thing
     happens. First the left-hand operand (`3`) is evaluated, it evaluates to itself in this
     case. Then the right-hand operand is evaluated (`2`), then the operation (`+`) is
     evaluated with the evaluated operands. Continue to evaluate these cells and convince
     yourself that you understand what each operator is doing. Modify the operands as you
     wish.
     
EXERCISE

SAY: Remember the order of operations. In school I learned a mnemonic (BODMAS): first
     brackets, then functions, then divide and multiply, and finally add and subtract.
     This order of operations also applies in computer programming to ensure that
     expressions are evaluated correctly.
     
EXERCISE

SAY: Don't worry, there's more to programming than mathematics. So if the maths
     scares you fear not for there is very little in this course. Maths is just useful
     when showing you the _building blocks_, the fundamental units used for constructing
     your programs and operations on these building blocks (+, *, /, abs(), etc.).
     One of those units (or types) are _numbers_, other are _text_,
     _images_, signals from _key presses_, or _mouse movements_, and many many more.
     Let's look at another one of these types, TEXT. Units of text are often called
     _strings_ because the computer represents them as a series of _characters_ strung
     together.
     What do you think the primitive `+` operation does when applied to strings? What
     about `*`? Let's find out...
     
RUN: Let students run the examples and find out what these operations do for themselves.

EXERCISE

SAY: The final building blocks we will explore in this section are the logical (Boolean; named 
     after the self-taught English mathematician [George Boole](https://en.wikipedia.org/wiki/George_Boole))
     values and comparison operators. The logical values are `True` and `False`. Like numbers and strings,
     they evaluate to themselves. There are several logical operators: locical conjunction
     performed with the `and` operator in Python. Logical disjunction performed with the
     `or` operator in Python. Finally, logical not performed with the `not` operator in
     Python.
     
CMD: Show truth tables in from [link](https://philosophy.lander.edu/logic/conjunct.html).
     Then allow students to predict the outcome of each cell.
     
EXERCISE
     
SAY: Beyond arithmetic on values a useful operation is comparison of values. You can read comparison
     expressions as questions. For example you can read the expression, `3 < 5` as "Is 3 less than 5?"
     The outcome of a comparison operation is a Boolean value. `True` is a "Yes" answer, and "False"
     is a "No" answer. You can ask questions like, "Are these values the same?", "Are these values different?",
     "Is this value less than this other value?", or "Is this value equal to or larger than this other value?"

EXERCISE

SAY: Now you've done some programming. And your computer has done some computing. You've earned a break.
     I'll start again in 10 minutes. If you have questions during the break, Tuur and I will be here.
     If at any point you feel lost or left behind please tell Tuur or myself either in the public chat or
     by private message. We have a lot to cover and many (if not all) of the concepts we talk about will
     be new to you. There is no shame in asking for help. Because we're not all in a room together
     we cannot see if you are struggling or not.

**11:00** Break

**11:10** Variables.

SAY: Now that we're familiar with some of the building blocks of programming. Variables provide us
     a way to start gluing these building blocks together into larger parts.
     You can think of a variable as a box for a value, and that box has a name, e.g. _mySequence_.
     You put something into the box using the special _assignment operator_ that Python has kindly
     provided for us. You can get that value back out simply by evaluating the box.

SAY: Let's examine an example in detail: We create a box called "myVar" and put the value `5` in it
     using the assignment operator. Then we want to evaluate the expression `myVar + myVar`. To do
     so Python first evaluates the left-hand operand, it opens the box and looks at the value inside,
     it's `5`. So the left-hand operand evaluates to `5`. The same happens for the right-hand operand.
     Python opens the box and finds `5` inside. Then Python can reduce the expression to `5 + 5`.
     If you evaluate this cell, Python should compute the result `10`.
     
SAY: What do you expect the second cell to evaluate to?
CMD: Read the text in the notebook.

SAY: So you can evaluate expressions containing variables in the same way we say earlier with values.
     Run each of the cells and convince yourself you understand by predicting the output for each cell.
     
**11:10** Input and Output (I/O)
SAY: Programming wouldn't be very useful if there were no way of interacting with the world
     outside of your program. Otherwise the only effect your program would have is to
     [slightly warm up your computer](https://www.youtube.com/watch?v=iSmkqocn0oQ&t=205)!
     There are many ways to interact with the outside world,
     displaying things on the screen, reacting to user input from the keyboard or mouse,
     responding to network requests, among many, many more.
     
SAY: I/O is a deep and complicated topic.
CMD: Read the text in the notebook.

EXERCISES

**11:50** Chapter review.
SAY: OK. By now you should have a picture of what the "building blocks"
     of programming are. The building blocks we've seen so far are numbers, text, and logical values
     and various operations on them. We've talked about variables and the assignment operator.
     This is a lot of ideas crammed into one morning. So well done to all of you. I appologise to those
     who are familiar with these ideas, things will get more interesting for you in the afternoon.
     If you feel like you're struggling you're probably not alone. Please let Tuur or I know either in
     the chat or via private message and we'll do anything we can to help you out.

SAY: Go through the chapter review questions yourself. Please try to answer each one. There are a few
     tricky ones, please don't feel disheartened if you don't know the answer. Just ask in the chat.
     After you've finished please have a break and eat some lunch. We'll be back at 13h00.


**12:00** Lunch

**13:00** Functions
SAY: Before lunch we explored the first-half of programming. The building blocks. In this section we will
     explore the glue we use to build up a whole program. In fact, we've already touched on one of
     these "glue" constructions. This chapter is all about functions: function application, function
     definition, and function composition.
     
SAY: So what is a function? You can think of a function as a black box. You feed input into the box
     and it gives you some output in return. Kind of like a bread making machine: you put in the
     ingredients and the bread making function gives you back a fresh loaf of bread.
     
SAY: In fact, you've already been using some functions! `abs()` is a function. You give it a number
     and it responds with the absolute value of that number. `len()` is a function. You give it a
     string and it responds with the length of that string. This is called _function application_.
     The function called `len` is applied to some argument with a string data type within a
     single pair of parentheses: `len("hello")`. It is the parentheses that are important here.
     They're what tell Python to _apply_ the function before them to whatever is between them.
     
SAY: So that's function _application_, what about function definition.
CMD: Read from the notebook.

SAY: A lot of what you do as a programmer will be debugging: your program will fail in some way and
     it is up to you to diagnose what the problem is and fix it. If you're getting an error message
     then pasting the error message into a search engine is an excellent idea, many problems are
     easily solved doing this. But be careful, don't just blindly paste the first "solution" you
     find into your code. Make sure you understand it to the extent that you're confident it fixes
     your problem.
     
SAY: A worse situation is when you're getting no error message but your program is producing
     incorrect results. There are many processes you can use to help you in this situation, but
     I will only briefly mention one of them here: testing. Among the many benefits of testing
     is that it can reveal logical problems in your program early and ensure they do not
     reoccur. When you test in real life you will use a testing framework, not the toy testing
     we're using here. But the examples below are a great illustration of testing.

CMD: At exercise 3-0 introduce "tests" and how to write a function that satisfies the test cases.
     Include a joke that breaks the second test. Then allow everyone to complete the first exercise.
     
EXERCISES: 3-1, 3-2

**13:20** Break

**13:30**

EXERCISES: 3-3, 3-4, 3-5

SAY: Now you've covered all of the really fundamental concepts in programming. You're already writing
     and testing complete programs. The remainder of this course, in some sense, are just details
     of what we've covered already. You're now, officially, programmers :)
     That doesn't mean you should ignore the rest of the course. Having a theoretical understanding of
     programming is very different from being able to practically and usefully use Python.
     Please spend some time to attempt the review questions then take a break. Feel free to ask
     questions in the chat. Tuur will take over after the break and I will take his place
     handing out internet points.
     
**13:50** Chapter review

**14:00** Break

**14:10** Conditions chapter

SAY: Today we have already covered the fundamental concepts of programming: the building blocks
     and how to stitch them together into larger, more useful parts with variables and functions.
     Although all programming _can_ be done with values and functions, in practice each language
     provides _syntax_ and _semantic_ conveniences tailored to a specific method of formulating
     solutions to computational problems (Your language shapes the way you think). In this
     chapter we begin to focus on Python and its unique qualities.

SAY: We will start this by writing a program to play the childrens game called "FizzBuzz". FizzBuzz is
     a counting game where each player takes it in turns to count up from 1. The twist is that
     when a player would say a number that is a multiple of 3 they have to say "Fizz" instead.
     When a multiple of 5, say "Buzz" and when a multiple of 3 AND 5, say "Fizz Buzz".

CMD: Use the flowchart in Figure 4-1 to describe how to play.

CMD: Trainers play the game live up to 15.

SAY: In this session, you will write a program to play the core part of this game. Next week you will
     write a program to play the whole game.

SAY: To be able to implement a program to play this game, clearly we need to be able to make
     _decisions_. For example, we might have our program ask the question, "Is the number
     a multiple of 3?". If the answer to that question is "YES" then we want to say "Fizz" etc etc.

SAY: Python gives us a special decision making _statement_ called **if**. **If** the answer to a
     question is "YES" (or `True`), then execute some code that wouldn't be executed if the
     answer were "NO" (or `False`). Of course Python requires you write this in a specific way...

CMD: Explain syntax of an `if` block including indentation.
     Indentation problems are talked about in the next section.

CMD: Walk through the code cell explaining in the terms used already. Comments may help.
     Ask students to run the block and experiment with what happens when they modify it.

SAY: You might be surprised that you already know enough to begin implementing a FizzBuzz program.

CMD: Students solve Exercise 4-1

CMD: Explain the solution to Exercise 4-2

**14:30** Break

**14:40** Back from break Quiz

QUIZ: A block of code is a series of Python statements executed together?
      - True
      - False

QUIZ: What is the result of `abs(-5) + 1 == 6`?
      - `True`
      - `true`
      - `t`
      - `6`
      - `YES`

QUIZ: Python cares about the blank spaces in your code.
      - Yes
      - No

**14:45** Indentation

SAY: Python code is organised into "blocks" that are noticable visually because of
     _equal indentation_. Each line of code within a block _must_ be equally indented. Thankfully,
     Jupyter is very helpful but problems can still happen if you are not careful.

CMD: Demonstrate unequal indentation. Ask students what happens when they try to run the
     cell with unequal indentation. Ask them to fix it.

SAY: You can also get the decision making process of your program mixed up when you are not careful
     about indentation. Remember that the block of code guarded by an **if** statement is only
     executed if the contition is `True`. To demonstrate an example of such a problem, try the next
     exercise...

CMD: Students solve Exercise 4-2

CMD: Explain the solution to Exercise 4-2

SAY: Exercises 4-3 and 4-4 are intended for you to practise using **if**. Try to complete
     these exercises too. Exercise 4-5 is an extension exercise which requires more knowledge than
     what we've presented you so far. If the exercises so far are too easy you're welcome to
     try it. Ask one of the trainers when you struggle so we can tell you what you need to know
     to solve it.

CMD: After most students have solved 4-3 and 4-4. Go over the solution to 4-3, 4-4, and 4-5.

SAY: It is ok if you do not understand the solution to Exercise 4-5. We have not covered what is
     happening here yet. It is still useful to expose you to more Python syntax though, and when
     we cover this topic you might recognise it.

**15:10** Break

**15:20** Back from Break Quiz

QUIZ: What is the result of `True and False`?
      - `True`
      - `False`

QUIZ: What is the result of `5 = 6`?
      - `False`
      - `True`
      - `SyntaxError`
      - Nothing

QUIZ: What is the result of `5 != 6`?
      - `False`
      - `True`
      - `SyntaxError`
      - Nothing

**15:25** `else` and `elif`

SAY: We have already provided an _alternative_ result for when an **if** condition is not `True`.
     `else` and `elif` are explicit alternatives that guard their respective code blocks.

CMD: Read and explain what's in the notebook.

CMD: Explain the code in the code cell. Run it. Ask students to modify and experiment with each cell
     until they are confident they understand what `else` and `elif` mean.

SAY: Now you understand enough to extend your earlier version of the FizzBuzz game.

CMD: Students solve Exercise 4-6.

CMD: Explain the solution of Exercise 4-6.

**15:50** Chapter Review

**16:00** Break

**16:10** Back from break Quiz

QUIZ: Does `"Python" == "python"`?
      - Yes
      - No

QUIZ: Is `'z' < 'a'`?
      - Yes
      - No

QUIZ: What is the result of `len("Python")`?
      - "Python"
      - 7
      - True
      - 6

**16:15** Select and work on your project.

SAY: During this course you will work on a large scale project. You can select a project to work on from the `projects/` folder.
     Each one is intended to be interesting and challenging but possible to complete in about 4-6 hours. You may think that you're
     not yet ready but you will be surprised what you can accomplish after this course!

**17:00** Fin
