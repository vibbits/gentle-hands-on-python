# Introduction to programming and Python

## Objectives

1. Begin to understand programming and computing. What are "building blocks"? How are building blocks "glued" together?
1. Evaluate some simple Python expressions on various data types.
1. Recognise error messages, comprehend them, and fix the problem they're describing.
1. Understand what a variable is how how to use them.
1. How are non-integer real numbers represented. Understand that using them can be dangerous.
1. How to perform type conversions.
1. How to perform some simple I/O with `input()` and `print()`.

## Materials

1. Jupyter and the "Basics", "Functions", and "Conditions" notebooks.
1. The "How to Design Programs" textbook.

## Procedure

**10:05** The basics of programming and computing.

SAY: By way of providing you with some background. Our objective for the first 2 sessions
     today is to provide you with a way of thinging about programming and computing in general.
     The ideas we want to present you with apply to all programming and programming languages
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
     
SAY: Remember the order of operations. In school I learned as mnemonic (BODMAS): first
     brackets, then functions, then divide and multiply, and finally add and subtract.
     This order of operations also applies in computer programming to ensure mathematical
     expressions are evaluated correctly.
     
SAY: Don't worry, there's more to programming than mathematics. So if the maths
     scares you fear not for there is very little in this course. Maths is just useful
     when showing you the _building blocks_, the fundamental units used for constructing
     your programs and primitive operations on these building blocks (+, *, /, abs(), etc.).
     One of those units (or types) are _numbers_, another is _text_,
     _images_, signals from _key presses_, or _mouse movements_, and many many more.
     Let's look at another one of these types, TEXT. Units of text are often called
     _strings_ because the computer represents them as a series of _characters_ strung
     together.
     What do you think the primitive `+` operation does when applied to strings? What
     about `*`? Let's find out...
     
RUN: Let students run the examples and find out what these operations do for themselves.

SAY: The final building blocks we will explore in this section are the logical (Boolean; named 
     after the self-taught English mathematician [George Boole](https://en.wikipedia.org/wiki/George_Boole))
     values and comparison operators. The logical values are `True` and `False`. Like numbers and strings,
     they evaluate to themselves. There are several logical operators: locical conjunction
     performed with the `and` operator in Python. Logical disjunction performed with the
     `or` operator in Python. Finally, logical not performed with the `not` operator in
     Python.
     
CMD: Show truth tables in from [link](https://philosophy.lander.edu/logic/conjunct.html).
     Then allow students to predict the outcome of each cell.
     
SAY: The outcome of a comparison operation is a Boolean value. These operations can be read
     as questions: Is `5` less than `10`? "Yes", or `True`.

CMD: Complete the exercises

SAY: Now you've done some programming. And your computer has done some computing. You've earned a break.
     I'll start again in 10 minutes. If you have questions during the break, Tuur and I will be here.
     If at any point you feel lost or left behind please tell Tuur or myself either in the public chat or
     by private message. We have a lot to cover and many (if not all) of the concepts we talk about will
     be new to you. There is no shame in asking for help. Unfortunately we're not all in a room together
     so we cannot see if you are struggling or not.

**10:30** Break

**10:40** Variables.

SAY: Now that we're familiar with some of the building blocks of programming. Variables provide us
     a way to start gluing them together into larger parts.
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
     
SAY: So far the "numbers" we've encountered are _integers_ or whole numbers. Sometimes, however,
     you will need to represent continuous values, _real numbers_. A very common way of _approximating_
     real numbers (a way that is used in most computing hardware) is a _floating point representation_.
     You can give Python a floating point number by typing a number with a decimal point.
     
SAY: I won't go into the details of binary representation of decimal numbers in this course. But I
     want to emphasise that you should be extra careful when using floating point numbers.
     
**11:00** A short intermezzo: Simple Input and Output (I/O)
SAY: Programming wouldn't be very useful if there were no way of interacting with the world
     outside of your program. Otherwise the only effect your program would have is to
     [slightly warm up your computer](https://www.youtube.com/watch?v=iSmkqocn0oQ&t=205)!
     There are many ways to interact with the outside world,
     displaying things on the screen, reacting to user input from the keyboard or mouse,
     responding to network requests, among many, many more.
     
SAY: I/O is a deep and complicated topic so begin with, we'll just show you how to interact with
     your console.
CMD: Read the text in the notebook.

**11:10** Data type conversions
SAY: Data type conversions are a common task in programming. A good example is reading data from the console.
     You and your users can type any string of characters available on their keyboards but you may need them to
     give you, e.g. an integer.
     
SAY: Because it is such a common task, Python provides you with some easy-to-use function for converting values
     to strings (`str()`), or to integers (`int()`), or to floating point numbers (`float()`).
CMD: Walk through examples in code cells.

SAY: While operating on data interactively you may wish to find out what data type you're dealing with.
     This is less common when you're dealing with primitive types like integers and floats but will
     become more useful as you create larger aggregated data structures.
     
**11:40** None
SAY: The final data type we'll talk about is a bit special. It's an ugly duckling, not like the others.
     It's `None`. A so-called "sentinal" value. A sentinal value is in-band data with out-of-band semantics.
     That may not clarify anything for you. Let me try to illustrate with an example:

> Imagine you're watching a movie with your friend. The room is dark and you hold a bucket of popcorn.
> Every few minutes your friend asks for a handful of popcorn. Being a good friend you give your friend
> a handful of popcorn. But what do you do when the bucket is empty?

SAY: This is what `None` is for. Typically, you should always give your friend back some popcorn, but sometimes
     you may have to give back `None` (in-band data). That `None` though is a special value, obviously its not
     popcorn, it _means_ something special: there's no more popcorn (out-of band semantics).
CMD: Execute the examples in the notebook to illustrate this point.

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

* Mention Curry-Howard Isomorphism

**14:00** Break

**14:15** Conditions

**16:00** Break

**16:15** Select and work on your project.

## Assessment
