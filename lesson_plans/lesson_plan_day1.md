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

1. "Types", "Functions", and "Conditions" notebooks
1. The "How to Design Programs" textbook.

## Procedure

### 09:00

**CMD**: Instructors meet to check tech and setup

### 09:20

**CMD**: Start greeting students as they arrive

**CMD**: If they haven't filled out the pre-course questionnaire: https://forms.vib.be/anon/#/forms/8482af4b-072a-4f8b-a062-2849b5b41ba7

### 09:30 (START: INSTRUCTOR 1)

**CMD**: Slow Introduction. Introduce the course.

**CMD**: Show the charts from VIB forms and set expectations based on those charts.

### 09:40

**CMD**: Most late students should arrive by now. Start proper now.

**CMD**: Guided tour of learning platform.
         - https://buzz.vib.be (polls, Q&A)
         - Online students may privately ask for help via Jitsi and receive 1-on-1 help in a breakout room.
         - If you cannot make Jitsi work you can follow online via YouTube (see welcome email for links).
         - If Jitsi has technical problems we will fail-over to another interactive platform (either Google Meet or Zoom; both accessible with a web browser).

**CMD**: Explain that online learning is different from classroom learning.
         It's difficult for trainers to notice that students are struggling and it's difficult to
         interact like we might in a classroom. Therefore we would like to get as much interaction
         as possible through Buzz, voice, and video.

**CMD**: Introduce online and offline students. Ask online students to turn on their microphones and cameras and introduce themselves. Name individual
         students one-by-one and ask them to introduce themselves in text that you can read aloud.
         - name
         - why you're here
         - what you want to do with python
         - a cool fact, funny joke, or something interesting about yourself

### 10:00

**CMD**: Talk about how to set up a learning environment with VSCodium or Google Colab (refer to the email)
**NOTE**: Dependencies are: `matplotlib ipympl`
**NOTE**: Special alternatives: Idle with a regular Python install, replit.com (whatever student is comfortable with).

### 10:30 (SWITCH INSTRUCTORS TO INSTRUCTOR 2)

**CMD**: Start on the basics of programming and computing.

**SAY**: By way of providing you with some background. Our objective
         today is to provide you with a way of thinking about programming and computing in general.
         Most of the ideas we will present to you apply to all of programming and programming languages
         even though we will be using Python for examples. So for those of you who are already familiar
         with R or other programming languages, we hope you will still find these 2 sessions useful.
     
**SAY**: A note for those of you who are already confident programmers. Today
         may feel slow for you. We're covering the basics. Feel free to read ahead and try to complete some
         exercises. There are links to more advanced exercises in several places. You're welcome to attempt these
         and ask questions about them.
         If you are a new programmer there are a lot of new concepts that we
         will cover today and you will feel exhausted soon enough. You might feel left behind at some point.
         If this happens please tell us! We are not in a hurry and telling us you need more time or help
         will not ruin the course for anyone else.

**SAY**: This morning we will start with a programming environment called "Hedy".
         This will allow you to start experimenting with simple programming concepts in
         a fun and interactive way.

**CMD**: Use the 01_Introduction notebook as a reference to demonstrate Hedy. Ask students to read
         through the "Introduction" tab then attempt some exercises. (repeat of a level or 2; students
         can proceed at their own pace).

### 11:00
**CMD**: Break for 10 minutes

### 11:10

**QUIZ**: Load `day1_morning_break.pdf`

### 11:15 (SWITCH INSTRUCTORS TO INSTRUCTOR 1)

**CMD**: Continue with Hedy

### 12:25

**CMD**: Review: what was learned with Hedy?

**SAY**: By now you should have a picture of what the "building blocks"
         of programming are. The building blocks we've seen so far are numbers, text, and variables values
         and various operations on them.
         This is a lot of ideas crammed into one morning. So well done to all of you.
         If you feel like you're struggling you're probably not alone. Please let us know
         and we'll do anything we can to help you out.

### 12:30

**CMD**: Lunch break for 1 hour

### 13:30

**CMD**: Return from break quiz

**QUIZ**: Load `day1_after_lunch.pdf`

### 13:05 (SWITCH INSTRUCTORS TO INSTRUCTOR 2)

**SAY**: I hoped you all enjoyed getting to grips with the very basics of programming with
         Hedy this morning. If you want to continue using Hedy after the course you may do
         so. It will eventually build up to Python. But, for now, we're finished with it.
         Instead, we will use the Python programming language for the remainder of the course.

**CMD**: Students should open the `02_Types` notebook in their environment of choice.

**SAY**: The remainder of today will focus on some _concepts_ that are broadly applicable to
         all programming and programming languages. Firstly the concept of "data types".
         
**CMD**: Read through the notebook.

**EXERCISE**: 2-1, 2-2, 2-3, 2-4

### 14:25

**CMD**: Chapter review

### 14:30

**CMD**: 10 minute Break

### 14:40

**QUIZ**: Load `day1_afternoon_break.pdf` (first 2 questions)

### 14:45

## 14:30 (SWITCH INSTRUCTORS TO INSTRUCTOR 1)

**CMD**: New topic: Functions

**SAY**: So far today, we explored the first-half of programming. The building blocks.
         In this section we will explore the "glue" we use to build up a whole program.
         In fact, we've already touched on one of these "glue" constructions. This
         chapter is all about "functions".
     
**SAY**: So what is a function? If your program is a list of instructions for
         computing something, then you can think of a function as a sub-list
         that "hides" some perhaps less interesting details.
         Do this for a simple everyday task in the next exercise.

**EXERCISE**: 3-1 SKIP THIS EXERCISE!!!!

**SAY**: It would be nice to be able to write sub-lists of instructions
         somewhere else so that we can ignore them if they don't need
         them but look them up when we do. That's basically what we do
         as programmers. We write our sub-lists (called functions from now on)
         somewhere else and only refer to them by name.

**SAY**: That's one way to think about functions but the analogy is imperfect
         because a function can also do things that a simple list of instructions
         cannot do! Imagine you have a function that runs a centrifuge. It would
         be very inconvenient if you had to write a new centrifuge running function
         to run the centrifuge for different durations or speeds. Thankfully functions
         can be parameterised: they can adjust their behaviour at your request!
         They can also perform computations and give you responses. A centrifuge
         running function may respond with whether the centrifuge is broken or not.
     
**SAY**: Here are 2 functions you can use right now: `abs()` is a function that computes
         the absolute value of a number, and `len()` is a function that computes
         the length of its argument, say a string. "Using" a function is
         called _function application_.
         The function called `len` is applied to some argument with a string data type within a
         single pair of parentheses: `len("hello")`. It is the parentheses that are important here.
         They're what tell Python to _apply_ the function.

**SAY**: You can think of a function as a transforming box with an opening to put things in
         at the top, and an opening for things to come out at the bottom. I can put a string
         into the function box labeled `len` and out will pop an integer.

**CMD**: Run first 2 code cells to demo function application.
     
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
         

### 15:30

**CMD**: Break

### 15:40

**QUIZ**: Load `day1_afternoon_break.pdf` (skip first 2 questions)

**CMD**: continue from notebook at testing.

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

**CMD**: Before exercise 3-4 introduce "tests" and how to write a function that satisfies the test cases.
     
**EXERCISE**: 3-4

**SAY**: Now you've covered all of the really fundamental concepts in programming. You're already writing
         and testing complete programs. The remainder of this course, in some sense, are just details
         of what we've covered already.

**SAY**: Please spend some time to attempt the review questions then take a break. Feel free to ask
         questions in the chat.

### 16:25

**CMD**: Chapter review

### 16:30

**CMD**: Introduce the projects as homework.

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
