# Introduction to programming and Python

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

**09:30** Introduction. Introduce trainers and ask students to turn on their microphones and cameras and introduce themselves.
    Demonstract downloading and installing Anaconda and starting Jupyter Labs.
    Introduce Google Collab for those with a google account.

**10:05** The basics of programming and computing.

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

**10:40** Break

**10:50** Variables.

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
     
**11:00** Input and Output (I/O)
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

CMD: At exercise 3.2.0 introduce "tests" and how to write a function that satisfies the test cases.
     Include a joke that breaks the second test. Then allow everyone to complete the first exercise.

SAY: Now you've covered all of the really fundamental concepts in programming. You're already writing
     and testing complete programs. The remainder of this course, in some sense, are just details
     of what we've covered already. You're now, officially, programmers :)
     That doesn't mean you should ignore the rest of the course. Having a theoretical understanding of
     programming is very different from being able to practically and usefully use Python.
     Please spend some time to attempt the review questions then take a break. Feel free to ask
     questions in the chat. Tuur will take over after the break and I will take his place
     handing out internet points.

**14:00** Break

**14:15** Conditions

**16:00** Break

**16:15** Select and work on your project.

## Assessment
