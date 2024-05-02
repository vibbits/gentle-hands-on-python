# Review

In this chapter you learned about the most important fundamental concepts for building and understanding
programs: building blocks (values and variables) and combining parts (functions). You also delved
into some techniques to make programs easier to understand, less complicated, and more trustworthy
(types, documentation, and testing).

You learned how to write code that simplifies the task of understanding a program by
_abstracting away_ details. Functions are a fundamentally important part of programming, indeed they
even correspond to mathematical proofs! [^1]

If you are new to programming then it is very likely this will seem overwhelming. Learning to program
requires you to understand many new concepts. It is ok if you feel overwhelmed, the remaining chapters
are here to help you practice. In some sense they are just more details of what we have already covered. [^2]

## Review Questions

<details>
  <summary>What is a <code>str</code>?</summary>
  A <code>str</code> is the <em>data type</em> of all text. The word "string" is a historical artifact
  that comes from the idea that letters are "strung" together.
</details>

<details>
  <summary>Is it possible to use the <code>+</code> operator when the operands are both <code>int</code> data types?</summary>
  Yes. This would be addition of numbers.
</details>

<details>
  <summary>Does Python check type annotations?</summary>
  No. Like comments, they are for people reading your code.
  There are separate programs that will check your types but these
  are out of scope for this course.
</details>

<details>
    <summary>What is a function?</summary>
    A <em>function</em> is a block of re-usable code with a name, that can be called using that name.
</details>

<details>
    <summary>What is the result of evaluating a function called?</summary>
    The <em>return value</em>. Or the value <em>returned by the function</em>. Or the <em>result</em>.
</details>

<details>
    <summary>What are docstrings? How do you access them?</summary>
    Docstrings are documentation that can be accessed using the <code>help()</code> function.
</details>

<details>
    <summary>What is meant by "function application"?</summary>
    Function application is synonymous with function "call" or "use". A function is applied to its arguments (or arguments are "passed" to the function) and evaluated to produce results.
    In Python, the function application operator is <code>()</code>.
</details>

[^1]: [The Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)

[^2]: Hoare, C.A.R. (1969) _[An Axiomatic Basis for Computer Programming](https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf)_. Communications of the ACM, 12(10):576-580 and 583.
