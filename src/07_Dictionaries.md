---
title: "Dictionaries"
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

# Dictionaries

> _"Complex is better than complicated."_<sup><a href="#References">1</a></sup>

What you might refer to as a _dictionary_ is often a book in which you can quickly lookup the definition of a word.
You can generalise this notion of a dictionary to anything that allows you to quickly lookup a _key_ (the word) to
find the _associated value_ (the definition).

It is best to think of a dictionary as a set of `key: value` pairs. The keys in a dictionary are _unique_ and
<abbr title="This is not strictly true">_unordered_</abbr>. The syntax for creating dictionaries is: `{}`,
and each `key:value` pair is separated with a comma. You will often see strings as keys, but many other values
can also be keys, as long as they're <abbr title="You cannot change the value">_immutable_</abbr>.


![A Python dictionary](images/myDictionary-cropped.png)

::: {.cell .code}
```python
three_letter_codes = {
    'A': 'Ala',
    'C': 'Cys',
    'D': 'Asp',
    'E': 'Glu',
    'F': 'Phe',
    'G': 'Gly',
    'H': 'His',
    'I': 'Ile',
    'K': 'Lys',
    'L': 'Leu',
    'M': 'Met',
    'N': 'Asn',
    'P': 'Pro',
    'Q': 'Gln',
    'R': 'Arg',
    'S': 'Ser',
    'T': 'Thr',
    'V': 'Val',
    'W': 'Trp',
    'Y': 'Tyr'
}
three_letter_codes
```
:::

There are 3 major _operations_ that you might want to perform on a **Dictionary**:

 1. Lookup a definition, given a word (lookup a value, given a key),
 2. Check if a word is in the dictionary (check if a key exists in the dictionary), and
 3. Add a new word with a definition to the dictionary (add a new key and associated value to the dictionary).

To lookup a value you can use a familiar operator: `[]` the indexing operator. Instead of giving it a numeric index, though, you
must give it a key that you know exists in the dictionary. Like so,

::: {.cell .code}
```python
three_letter_codes['A']
```
:::

If you try to lookup a key that does not exist in the dictionary then this happens:

::: {.cell .code}
```python
three_letter_codes['X']
```
:::

Therefore, it is often a very good idea to _check_ that a key exists in your dictionary before trying to lookup the associated value:

::: {.cell .code}
```python
'A' in three_letter_codes
```
:::

::: {.cell .code}
```python
if 'X' in three_letter_codes:
    print("The associated value for X is: " + three_letter_codes['X'])
else:
    print("The key X does not exist in the dictionary")
```
:::

Finally, you can _update_ a dictionary by assigning to a lookup with the index operator. For instance, if we want to add the
key `'X'` with the value, `"Unknown"` to out `three_letter_codes` dictionary:

::: {.cell .code}
```python
three_letter_codes['X'] = "Unknown"
three_letter_codes
```
:::

You can also use this pattern to modify an existing value:

::: {.cell .code}
```python
three_letter_codes['A'] = "This has been modified"
three_letter_codes
```
:::

But let us change this back to `"Ala"` for now...

::: {.cell .code}
```python
three_letter_codes['A'] = "Ala"
three_letter_codes
```
:::

## A new project

During the course of the previous chapters we wrote a program to play the childrens "Fizz Buzz" game. Now that you're more
familiar with Python we can write a more interesting program together. This time, imagine that you've been commisioned to
generate plots from temperature data for 3 countries and a global plot to compare against:

  - Belgium
  - Russia
  - Australia

You have some data sources:

  * [Global](https://hadleyserver.metoffice.gov.uk/hadcrut5/data/current/download.html)
  * [Belgium](https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/bel_data_orig.csv)
  * [Russia](https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/rus_data_orig.csv)
  * [Australia](https://gist.github.com/MaybeJustJames/4a604c9d9dcff2c999496ec5def1d6ce/raw/caf3df0d47b1523e347df01ed8db2cc3726b1bdc/aus_data_orig.csv)

<!-- Original country data source: https://climateknowledgeportal.worldbank.org -->

<img src="images/global_climate_plot.png" alt="Global temperature anomally 1961-90" style="width: 600px">

The task essentially breaks down into these high-level steps:

1. Model the data
1. Fetch the data
1. Clean the data
1. Align the data
1. Average/smooth the data
1. Plot the data

Today, you will perform all of these steps in Python. You will use this scenario to explore some other useful aspects of Python.
Your first task is to model the data.

---

### Exercise 7-1: A climate observation

Construct a dictionary containing the keys, "BEL", "RUS', "AUS", and "GLO" and decimal numbers for values
(You can pick any number you like).

::: {.cell .code}
```python

```
:::

A list of these dictionaries could represent a time-series of observations for each of the territories we need to eventually plot.

---

Now that you are comfortable with the syntax for defining a dictionary in Python it is time to start practising the common operations:

---

### Exercise 7-2: Look it up in a dictionary

Write a function that takes a single letter amino acid code as an argument and returns a three letter code. If the argument is not
a valid single letter code then you should return the string `"Unknown"`. **You should use the `three_letter_codes`
dictionary we defined earlier without modifying it.**

::: {.cell .code}
```python
def lookup_three_letter_code(code: str) -> str:
    ...

assert "Ala" == lookup_three_letter_code("A"), "Expected 'Ala', got: " + str(lookup_three_letter_code("A"))
assert "Unknown" == lookup_three_letter_code("X"), "Expected 'Unknown', got: " + str(lookup_three_letter_code("X"))
assert "Unknown" == lookup_three_letter_code("Belgium"), "Expected 'Unknown', got: " + str(lookup_three_letter_code("Belgium"))
assert "Unknown" == lookup_three_letter_code("m"), "Expected 'Unknown', got: " + str(lookup_three_letter_code("m"))
assert "Met" == lookup_three_letter_code("M"), "Expected 'Met', got: " + str(lookup_three_letter_code("M"))
```
:::

[Advanced question](Advanced%20Exercises.ipynb#7-2)

---

### Exercise 7-3: Amino-acid sequence

Write a function that takes a sequence of amino-acids represented by their single letter code. Return a list of three-letter-codes.
For example, given the input: `"EIKGGQ"` return `['Glu', 'Ile', 'Lys', 'Gly', 'Gly', 'Gln']`. **You should use the `three_letter_codes`
dictionary we defined earlier without modifying it.**

::: {.cell .code}
```python
def one_to_three_letter_code(sequence):
    ...

assert one_to_three_letter_code("") == [], "Did not expect " + str(one_to_three_letter_code(""))
assert one_to_three_letter_code("EIKGGQ") == ['Glu', 'Ile', 'Lys', 'Gly', 'Gly', 'Gln'], "Did not expect " + str(one_to_three_letter_code('EIKGGQ'))
assert one_to_three_letter_code("PRAPY") == ['Pro', 'Arg', 'Ala', 'Pro', 'Tyr'], "Did not expect " + str(one_to_three_letter_code('PRAPY'))
```
:::

---

### Exercise 7-4: Frequency

Write a function that accepts an amino-acid sequence and returns a dictionary keyed by the amino-acid single-letter-code and the
value is the frequency of observation (number of times that letter appears) of that amino-acid in the sequence.

::: {.cell .code}
```python
def frequencies(sequence: str):
    ...

assert frequencies("AACD") == {"A": 2, "C": 1, "D": 1}, "Unexpected " + str(frequencies('AACD'))

sequence = "SFTMHGTPVVNQVKVLTESNRISHHKILAIVGTAESNSEHPLGTAITKYCKQELDTETLGTCIDFQVVPGCGISCKVTNIEGLLHKNNWNIEDNNIKNASLVQIDASNEQSSTSSSMIIDAQISNALNAQQYKVLIGNREWMIRNGLVINNDVNDFMTEHERKGRTAVLVAVDDELCGLIAIADT"
expected = {'A': 12, 'C': 5, 'D': 10, 'E': 12, 'F': 3, 'G': 11, 'H': 6, 'I': 18, 'K': 9, 'L': 14, 'M': 4, 'N': 18, 'P': 3, 'Q': 8, 'R': 5, 'S': 14, 'T': 14, 'V': 15, 'W': 2, 'Y': 2}
assert frequencies(sequence) == expected, "Unexpected " + str(frequencies(sequence))
```
:::

---

The final operation that you will often perform on dictionaries is to loop over them. Thankfully this operation will feel
very familiar to you.

---

### Exercise 7-5: Weather, averaged over time, is climate
Write a function that accepts a list of observations (See the dictionary you created in Exercise 7-1) and returns a dictionary with the same structure but the values are the averages of the input. For example, consider these input observations:

```python
[
    {"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1},
    {"BEL": 10.2, "RUS": -2.0, "AUS": 37.8, "GLO": 21.2},
    {"BEL": 14.7, "RUS": 1.3, "AUS": 18.3, "GLO": 23.6}
]
```

The output of your function should be:
```python
{"BEL": 10.2, "RUS": -4.5, "AUS": 32.9, "GLO": 22.3}
```

::: {.cell .code}
```python
def average_temperature(observations):
    ...

example = [
    {"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1},
    {"BEL": 10.2, "RUS": -2.0, "AUS": 37.8, "GLO": 21.2},
    {"BEL": 14.7, "RUS": 1.3, "AUS": 18.3, "GLO": 23.6}
]

assert average_temperature([]) == {}, "Expected {}, got: " + str(average_temperature([]))
assert average_temperature(example) == {"BEL": 10.2, "RUS": -4.5, "AUS": 32.9, "GLO": 22.3}, "Got " + str(average_temperature(example))
```
:::

[Advanced question](Advanced%20Exercises.ipynb#7-5)

---

## Chapter Review
In this chapter you've learned about the Python _dictionary_. It's a special collection that stores an association (or mapping)
between _keys_ and _values_. Due to this, the keys must be unique.

### Review Questions

1. How is an empty dictionary written?
<details>
    <summary>Answer</summary>
    <code>{}</code> or <code>dict()</code>
</details>

1. Can any data type be a value in a dictionary?
<details>
    <summary>Answer</summary>
    Yes!
</details>

1. When you loop over a dictionary, what does the loop variable contain?
<details>
    <summary>Answer</summary>
    The <em>key</em>, not the <em>value</em>.
</details>

1. Can a list be a key in a dictionary?
<details>
    <summary>Answer</summary>
    No. Lists are <em>mutable</em> (they can be modified after you create them) so they cannot be stable keys.
</details>

1. How can you access a key you're not sure is in the dictionary?
<details>
    <summary>Answer</summary>
    If the key is not in the dictionary you cannot access it. But you can check that it is <code>in</code> the dictionary first.
</details>

## References

1. Zen of Python: https://www.python.org/dev/peps/pep-0020/

## Supporting material
* [Automate the Boring Stuff with Python, Chapter 5](http://automatetheboringstuff.com/2e/chapter5/)
* [Real Python: Dictionaries](https://realpython.com/python-dicts/)


Click [here](08_Files.ipynb) to go to the next chapter.
