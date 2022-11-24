---
title: "Introduction"
jupyter:
  nbformat: 4
  nbformat_minor: 5
  kernelspec:
    display_name: "Python 3 (ipykernel)"
    language: "python"
    name: "python3"
  language_info:
    codemirror_mode:
      name: "ipython"
      version: 3
    file_extension: ".py"
    mimetype: "text/x-python"
    name: "python"
    nbconvert_exporter: "python"
    pygments_lexer: "ipython3"
    version: "3.11.0"
---

# Introduction

Welcome. Learning how to write programs is a daunting but extremely useful skill and you've all
taken the first step. It will be a long journey but you will soon notice that the skills you
acquire along the way can already be put to good use. This course is designed as an introduction
to programming for those with no experience at all. We happen to use the Python language but the skills
you aquire will be useful with a broad range of languages. Python itself is often used broadly
in biological research and bioinformatics so it it likely to be directly applicable to your work.
We do not expect you to be able to weild Python independently after this course, but have a solid
foundation from which to continue learning and applying your new skills.

## Hedy

Hedy is a "gradual" programming language in that you will start with very simple programs and
Hedy will gradually introduce new concepts to you. In fact each "level" introduces new ideas and
commands. Today we will work through the first 4 levels of Hedy in order to understand the basics of
programming.

> Please use the link shared by your instructor to join the class on Hedy.

![Hedy interface](images/hedy_1.png)

Within the Hedy interface you will find an area for writing program code:

![Hedy interface with text editing area highlighted](images/hedy_2.png)

A place for your program to display text:

![Hedy interface with the output area highlighted](images/hedy_3.png)

In order to run the program that you type in, you can press the "Run Code" button:

![Hedy interface with the Run Code button highlighted](images/hedy_run_code.png)

Read the introductory description. Three commands are introduced: `print`, `ask`, and `echo`.
Using these thre commands you can print text to the output area. Once you have tried writing
a program to print text to the output area with Hedy, explore some challenges in the tabs here:

![Hedy interface with the challenge tabs highlighted](images/hedy_4.png)

Finally, once you have solved a few challenges and you feel comfortable with this level you can
move onto the next level by pressing this button:

![Hedy interface with the next level button highlighted](images/hedy_next_level.png)

## Comments

In their seminal book, _Structure and Interpretation of Computer Programs_, Abelson and Sussman claim that,

> Programs must be written for people to read, and only incidentally for machines to execute.

It is often the case that programs need explanation beyond the code you have typed out in order for others
(or even yourself) to understand them. This is what _commenting_ is for.

```python
# This is a comment
x is ask "What is x?" # This is also a comment
```

Comments are text that is ignored by the program so you can write whatever you need. Sometimes it can
even be useful to draw diagrams in comments!

```python
#       _
#      | |
#      | | __ _ _ __ ___   ___  ___
#  _   | |/ _` | '_ ` _ \ / _ \/ __|
# | |__| | (_| | | | | | |  __/\__ \
#  \____/ \__,_|_| |_| |_|\___||___/
```

## Chapter Review

This morning you have learned that programs are ordered sequences of precise instructions,
somewhat like a recipe. You can print text, ask the user of your program to enter text,
"save" values into "variables", and use quote _syntax_ to distinguish literal text from
variables.

At the end of each "chapter" will be a series of questions to check against your understanding.
These are for your own use and should prompt you to remember important ideas. These questions
will start in the next chapter.

Click [here](02_Types.ipynb) to go to the next chapter.
