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

1. Jupyter and the "Basics", "Functions", and "Conditions" notebooks: https://github.com/vibbits/gentle-hands-on-python/releases/download/2021-08-day1/ghop_day1.zip
1. The "How to Design Programs" textbook.

## Procedure

### 09:00

**CMD**: Instructors meet to check tech and setup

### 09:20

**CMD**: Start greeting students as they arrive

**CMD**: If they haven't filled out the pre-course questionnaire: https://vib.formstack.com/forms/pythonprecoursequestionnaire

### 09:30 (START: INSTRUCTOR 1)

**CMD**: Slow Introduction. Introduce the course.

**CMD**: Show the charts from VIB forms and set expectations based on those charts.

### 09:40

**CMD**: Most late students should arrive by now. Start proper now.

**CMD**: Guided tour of learning platform. How to use the chat functionality. How to send a private message to an
         instructor, how to answer a poll/quiz.
         Shift+Enter to send multiline messages.

**CMD**: Explain that online learning is different from classroom learning.
         It's difficult for trainers to notice that students are struggling and it's difficult to
         interact like we might in a classroom. Therefore we would like to get as much interaction
         as possible via voice and video.

**CMD**: Ask students to turn on their microphones and cameras and introduce themselves. If not, name individual
         students one-by-one and ask them to introduce themselves in text that you can read aloud.
         - name
         - why you're here
         - what you want to do with python
         - a cool fact, funny joke, or something interesting about yourself

### 10:00

**CMD**: Talk about how to set up a learning environment (refer to the email)
**NOTE**: Dependencies are: `matplotlib ipympl pillow`
**NOTE**: Anaconda download link: https://www.anaconda.com/products/individual
* If students are running Windows or Apple OSX (and have at least 5 GiB available disk space):
  Demonstrate downloading and installing Anaconda and starting Jupyter Labs. Video: https://youtu.be/hmI8YIejVcQ
* Otherwise, introduce Google Collab for those with a google account: https://colab.research.google.com/
* GNU/Linux users need not use Anaconda. Just `pip install jupyterlab matplotlib ipympl pillow`.
* Special alternative: Idle with a regular Python install, replit.com (whatever student is comfortable with). Python can be installed
  from the Microsoft store on Windows 10:  https://www.youtube.com/watch?v=yXfCq4xzrrI&t=19s (Be careful: says Python 3.7)

### 10:30 (SWITCH INSTRUCTORS TO INSTRUCTOR 2)

**CMD**: Start on the basics of programming and computing.

**SAY**: By way of providing you with some background. Our objective for the first 2 sessions
         today is to provide you with a way of thinking about programming and computing in general.
         Most of the ideas we will present to you apply to all of programming and programming languages
         even though we will be using Python for examples. So for those of you who are already familiar
         with R or other programming languages, we hope you will still find these 2 sessions useful.
     
**SAY**: A note for those of you who are already confident programmers. This morning
         may feel slow for you. We're covering the basics. Feel free to read ahead and try to complete some
         exercises. There are links to more advanced exercises in several places. You're welcome to attempt these
         and ask questions about them in the chat, but we will not be covering solutions.
         If you are a new programmer please follow along with me. There are
         a lot of new concepts that we will cover today and you will feel exhausted
         soon enough. We do not need to rush.

**CMD**: Read out the quote from "How to Design Programs"

> When you were a small child, your parents taught you to count
> and perform simple calculations with your fingers [..]. They
> would ask "what's 3 + 2?" and you would count off the fingers
> on one hand. They programmed and you computed. And in some
> way, that's really all there is to programming and computing.

**SAY**: Now we're going to do some programming in the same way. We'll
         ask some simple arithmetic questions, and the computer will compute
         the answers and print the results. That's how simple programming is.
         You ask questions of your programming environment (in this case, Python),
         and it computes for you.
     
**RUN**: With the students, explain again how to execute a cell and verify each answer.
         Also explain what `abs()` is doing.
     
**SAY**: The first cell here just contains a number. Run it. What happens? Yes, numbers
         evaluate to themselves. `1` evaluates to `1`. `256` evaluates to `256`. When you
         execute a cell containing a more complicated expression, like `3 + 2` a similar thing
         happens. First the left-hand operand (`3`) is evaluated, it evaluates to itself in this
         case. Then the right-hand operand is evaluated (`2`), then the operation (`+`) is
         evaluated with the evaluated operands. Continue to evaluate these cells and convince
         yourself that you understand what each operator is doing. Modify the operands as you wish.
     
**EXERCISE** 2-1

**SAY**: Remember the order of operations. In school I learned a mnemonic (BODMAS): first
         brackets, then functions, then divide and multiply, and finally add and subtract.
         This order of operations also applies in computer programming to ensure that
         expressions are evaluated correctly.
     
**EXERCISE** 2-2

**SAY**: Don't worry, there's more to programming than mathematics. So if the maths
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
     
**RUN**: Let students run the examples and find out what these operations do for themselves.

**EXERCISE** 2-3

**SAY**: The final building blocks we will explore in this section are the logical (Boolean; named 
         after the self-taught English mathematician [George Boole](https://en.wikipedia.org/wiki/George_Boole))
         values and comparison operators. The logical values are `True` and `False`. Like numbers and strings,
         they evaluate to themselves. There are several logical operators: locical conjunction
         performed with the `and` operator in Python. Logical disjunction performed with the
         `or` operator in Python. Finally, logical not performed with the `not` operator in
         Python.
     
**CMD**: Show truth tables in from [link](https://philosophy.lander.edu/logic/conjunct.html).
         Then allow students to predict the outcome of each cell.

**EXERCISES** 2-4
     
**SAY**: Beyond arithmetic on values a useful operation is comparison of values. You can read comparison
         expressions as questions. For example you can read the expression, `3 < 5` as "Is 3 less than 5?"
         The outcome of a comparison operation is a Boolean value. `True` is a "Yes" answer, and "False"
         is a "No" answer. You can ask questions like, "Are these values the same?", "Are these values different?",
         "Is this value less than this other value?", or "Is this value equal to or larger than this other value?"

**EXERCISE** 2-5, 2-6

**SAY**: Now you've done some programming. And your computer has done some computing. You've earned a break.
         I'll start again in 10 minutes. If you have questions during the break, one of your instructors will be here.
         If at any point you feel lost or left behind please tell one of us instructors, either in the public chat or
         by private message. We have a lot to cover and many (if not all) of the concepts we talk about will
         be new to you. There is no shame in asking for help. Because we're not all in a room together
         we cannot see if you are struggling or not.

### 11:00
**CMD**: Break for 10 minutes

### 11:10

**QUIZ**: Load `day1_morning_break.pdf`

### 11:15 (SWITCH INSTRUCTORS TO INSTRUCTOR 1)

**CMD**: Start the Variables section.

**SAY**: Now that we're familiar with some of the building blocks of programming. Variables provide us
         a way to start gluing these building blocks together into larger parts.
         You can think of a variable as a box for a value, and that box has a name, e.g. _mySequence_.
         You put something into the box using the special _assignment operator_ that Python has kindly
         provided for us. You can get that value back out simply by evaluating the box.

**SAY**: Let's examine an example in detail: We create a box called "my_var" and put the value `5` in it
         using the assignment operator. Then we want to evaluate the expression `my_var + my_var`. To do
         so Python first evaluates the left-hand operand, it opens the box and looks at the value inside,
         it's `5`. So the left-hand operand evaluates to `5`. The same happens for the right-hand operand.
         Python opens the box and finds `5` inside. Then Python can reduce the expression to `5 + 5`.
         If you evaluate this cell, Python should compute the result `10`.
     
**SAY**: What do you expect the second cell to evaluate to?

**CMD**: Read the text in the notebook.

**SAY**: So you can evaluate expressions containing variables in the same way we say earlier with values.
         Run each of the cells and convince yourself you understand by predicting the output for each cell.

**SAY**: Notice that the cell containing assignments to the `x` and `y` variables did not evaluate to
         anything. This is because assignment is a _statement_, not an _expression_. The difference is that
         expressions evaluate to something, statements do not.

**CMD**: Briefly describe shorthand arithmentic-assignment expressions and allow students to experiment with them.

### 11:25

**CMD**: Introduce basic Input and Output (I/O)

**SAY**: Programming wouldn't be very useful if there were no way of interacting with the world
         outside of your program. Otherwise the only effect your program would have is to
         [slightly warm up your computer](https://www.youtube.com/watch?v=iSmkqocn0oQ&t=205)!
         There are many ways to interact with the outside world,
         displaying things on the screen, reacting to user input from the keyboard or mouse,
         responding to network requests, among many, many more.
     
**SAY**: I/O is a deep and complicated topic so we will only just scratch the surface for now.

**CMD**: Read the text in the notebook (second paragraph).

**EXERCISES** 2-7, 2-8

**SAY**: Now you've been introduced to the basics try to explore what you have already learned in
         the coming exercises...

**EXERCISES** 2-9, 2-10, 2-11

**CMD**: Describe what comments are and why they're useful.

**CMD**: Talk about modules/packages/libraries. Python is "batteries included" with a lot of libraries "built-in".
         But there is a universe of third-party libraries too that can be used. Some of which students
         already installed for this course ;)

### 11:55

**CMD**: Review the Chapter: what was learned?

**SAY**: OK. By now you should have a picture of what the "building blocks"
         of programming are. The building blocks we've seen so far are numbers, text, and logical values
         and various operations on them. We've talked about variables and the assignment operator.
         This is a lot of ideas crammed into one morning. So well done to all of you. I appologise to those
         who are familiar with these ideas, things will get more interesting for you in the afternoon.
         If you feel like you're struggling you're probably not alone. Please let us know either in
         the chat or via private message and we'll do anything we can to help you out.

**SAY**: Go through the chapter review questions yourself. Please try to answer each one. There are a few
         tricky ones, please don't feel disheartened if you don't know the answer. Just ask in the chat.
         After you've finished please have a break and eat some lunch. We'll be back at 13h00.


### 12:00

**CMD**: Lunch break for 1 hour

### 13:00

**CMD**: Return from break quiz

**QUIZ**: Load `day1_after_lunch.pdf`

### 13:05 (SWITCH INSTRUCTORS TO INSTRUCTOR 2)

**CMD**: New topic: Functions

**SAY**: Before lunch we explored the first-half of programming. The building blocks. In this section we will
         explore the glue we use to build up a whole program. In fact, we've already touched on one of
         these "glue" constructions. This chapter is all about functions.
     
**SAY**: So what is a function? If your program is a list of instructions for computing something, then
         you can think of a function as a sub list that "hides" some perhaps less interesting details.
         Do this for a simple everyday task in the next exercise.

**EXERCISE**: 3-1

**SAY**: It would be nice to be able to write these sub-lists of instructions somewhere else so that
         your friend can ignore them if they don't need them but look them up if they do. That's
         basically what we do as programmers. We write our sub-lists (called functions from now on)
         somewhere else and only refer to them by name.

**SAY**: That's one way to think about functions but the analogy is imperfect because a function can
         sdo things that a simple list of instructions cannot do! Imagine you have a function that runs
         a centrifuge. It would be very inconvenient if you had to write a new centrifuge running function
         to run the centrifuge for different durations or speeds. Thankfully functions can be parameterised:
         they can adjust their behaviour at your request! They can also perform computations and give you
         responses. A centrifuge running function may respond with whether the centrifuge is broken or not.
     
**SAY**: In fact, you've already been using some functions! `abs()` is a function. You give it a number
         and it responds with the absolute value of that number. `len()` is a function. You give it a
         string and it responds with the length of that string. This is called _function application_.
         The function called `len` is applied to some argument with a string data type within a
         single pair of parentheses: `len("hello")`. It is the parentheses that are important here.
         They're what tell Python to _apply_ the function before them to whatever is between them.

**CMD**: Run first 2 code cells to demo function application.
     
**SAY**: So that's function _application_, you've seen that already. The real meat of this chapter is defining your own
         functions so let's do that now.

**CMD**: Read from section 1.2

**EXERCISE**: 3-2

**SAY**: We have to talk a little about Python syntax at this point. Python code is organised into
         "blocks" that are noticable visually because of _equal indentation_. Each line of code
         within a block _must_ be equally indented. Thankfully,
         Jupyter is very helpful but problems can still happen if you are not careful.

**CMD**: Demonstrate unequal indentation. Ask students what happens when they try to run the
         cell with unequal indentation. Ask them to fix it.

**SAY**: In the next 2 exercises you will practise indentation, feel free to use your ENTER key liberally.
         You will also elplore what it means to `return` a value from a function.

**EXERCISE**: 3-3

**SAY**: In this exercise you hopefully noticed that your functions can sometimes return this `None` value.
         This is a special marker that Python uses to represent the absence of a value. Yes, it probably
         seems like a weird concept but it can be useful. Let's see what else functions can `return`.

**EXERCISE**: 3-4

**SAY**: A lot of what you do as a programmer will be debugging: your program will fail in some way and
         it is up to you to diagnose what the problem is and fix it. If you're getting an error message
         then pasting the error message into a search engine is an excellent idea, many problems are
         easily solved doing this. But be careful, don't just blindly paste the first "solution" you
         find into your code. Make sure you understand it to the extent that you're confident it fixes
         your problem.
     
**SAY**: A worse situation is when you're getting no error message but your program is producing
         incorrect results. There are many processes you can use to help you in this situation, but
         I will only briefly mention one of them here: testing. Among the many benefits of testing
         is that it can reveal logical problems in your program early and ensure they do not
         reoccur. When you test in real life you will use a testing framework, but for now we will just
         show you the basics.

**CMD**: Read from the notebook about testing section 3.


**CMD**: At exercise 3-0 introduce "tests" and how to write a function that satisfies the test cases.
         Then allow everyone to complete the first exercise (3-1).
     
**EXERCISES**: 3-5, 3-6, 3-7

## 13:45 (SWITCH INSTRUCTORS TO INSTRUCTOR 1)

**CMD**: Function composition

**SAY**: At the beginning of this section we talked about functions as the "combining parts" of programs.
         Well this wouldn't be very useful if we couldn't combine functions themselves together.

**CMD**: Talk through section 4 on function composition

**EXERCISE**: 3-8

**SAY**: Now you've covered all of the really fundamental concepts in programming. You're already writing
         and testing complete programs. The remainder of this course, in some sense, are just details
         of what we've covered already.

**SAY**: Please spend some time to attempt the review questions then take a break. Feel free to ask
         questions in the chat.

### 14:25

**CMD**: Chapter review

### 14:30

**CMD**: Break

### 14:40

**QUIZ**: Load `day1_afternoon_break.pdf`

### 14:45

**CMD**: New topic: Conditions

**SAY**: Today we have already covered the fundamental concepts of programming: the building blocks
         and how to stitch them together into larger, more useful parts with variables and functions.

**SAY**: We will start this by writing a program to play the childrens game called "FizzBuzz". FizzBuzz is
         a counting game where each player takes it in turns to count up from 1. The twist is that
         when a player would say a number that is a multiple of 3 they have to say "Fizz" instead.
         When a multiple of 5, say "Buzz" and when a multiple of 3 AND 5, say "Fizz Buzz".

**CMD**: Use the flowchart in Figure 4-1 to describe how to play.

**CMD**: Trainers play the game live up to 15.

**SAY**: In this session, you will write a program to play the core part of this game. Next week you will
         write a program to play the whole game.

**SAY**: To be able to implement a program to play this game, clearly we need to be able to make
         _decisions_. For example, we might have our program ask the question, "Is the number
         a multiple of 3?". If the answer to that question is "YES" then we want to say "Fizz" etc etc.

**SAY**: Python gives us a special decision making _statement_ called **if**. **If** the answer to a
         question is "YES" (or `True`), then execute some code that wouldn't be executed if the
         answer were "NO" (or `False`). Of course Python requires you write this in a specific way...

**CMD**: Explain syntax of an `if` block including indentation.

**CMD**: Walk through the code cell explaining in the terms used already. Comments may help.
         Ask students to run the block and experiment with what happens when they modify it.

**SAY**: You might be surprised that you already know enough to begin implementing a FizzBuzz program.

**EXERCISE** 4-1

**SAY**: For extra points, why is "Fizz Buzz" returned first?

### 15:00

**SAY**: You can also get the decision making process of your program mixed up when you are not careful
         about indentation. Remember that the indented block of code guarded by an **if** statement is only
         executed if the contition is `True`. So it is important to ensure that all of the code you wish to
         be conditionally executed is indented under the `if`. To demonstrate an example of such a problem,
         try the next exercise...

**EXERCISE** 4-2

**SAY**: Exercises 4-3 and 4-4 are intended for you to practise using **if**. Try to complete
         these exercises too.

**EXERCISES**: 4-3, 4-4

### 15:50

**CMD**: Break

### 16:00 (SWITCH INSTRUCTORS TO INSTRUCTOR 2)

**CMD**: Final topic: `else` and `elif`

**SAY**: We have already provided an _alternative_ result for when an **if** condition is not `True`.
         `else` and `elif` are explicit alternatives that guard their respective code blocks.

**CMD**: Read and explain what's in the notebook.

**CMD**: Explain the code in the code cell. Run it. Ask students to modify and experiment with each cell
         until they are confident they understand what `else` and `elif` mean.

**SAY**: Now you understand enough to extend your earlier version of the FizzBuzz game.

**EXERCISE** 4-5

### 16:15

**CMD**: Chapter Review

### 16:20

**SAY**: During this course you will work on a large scale project. You can select a project
         to work on from the `projects/` folder. Each one is intended to be interesting and
         challenging but possible to complete in about 4-6 hours. You may think that you're
         not yet ready but you will be surprised what you can accomplish after this course!

**SAY**: Today has been a long day and I expect you're feeling overwhelmed.
         You don't need to start working on a project right now but do try to work on
         one before the next session on %DATE%. We (trainers) will be here until 5PM if you have any
         questions or concerns please feel free to ask us. If you are feeling lost or left behind
         please tell us, there is no shame in feeling left behind given the number of new
         concepts and ideas that we've covered in a single day!

**CMD**: Have students browse through the projects

### 17:00

**CMD**: Fin
