# Dictionaries

<div style="display:flex; align-items:center; justify-content:center; width:100%; height: 15rem; background-color:lightsteelblue">
Video placeholder
</div>

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

> _"Complex is better than complicated."_ [^1]

What you might refer to as a _dictionary_ is often a book in which you can quickly lookup the
definition of a word. You can generalise this notion of a dictionary to anything that allows
you to quickly lookup a _key_ (the word) to find the _associated value_ (the definition).

It is best to think of a dictionary as a set of `key: value` pairs. The keys in a dictionary
are _unique_ and <abbr title="This is not strictly true">_unordered_</abbr>. The syntax for
creating dictionaries is: `{}`, and each `key:value` pair is separated with a comma. You will
often see strings as keys, but many other values can also be keys, as long as they're
<abbr title="You cannot change the value">_immutable_</abbr>.

<img src="media/myDictionary-cropped.png" alt="A Python dictionary" style="width:95%;height:auto">

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

There are 3 major _operations_ that you might want to perform on a **Dictionary**:

 1. Lookup a definition, given a word (lookup a value, given a key),
 2. Check if a word is in the dictionary (check if a key exists in the dictionary), and
 3. Change the definition or add a new word with a definition to the dictionary (change the value for a key or add a new key and associated value to the dictionary).

To lookup a value you can use a familiar operator: `[]` the indexing operator. But instead of giving
it a numeric index, you must give it a key that you know exists in the dictionary. Like so,

```python
three_letter_codes['A']
```

If you try to lookup a key that does not exist in the dictionary then this happens:

```python
three_letter_codes['X']
```

Therefore, it is often a very good idea to _check_ that a key exists in your dictionary before trying to lookup the associated value:

```python
'A' in three_letter_codes
```

```python
if 'X' in three_letter_codes:
    print("The associated value for X is: " + three_letter_codes['X'])
else:
    print("The key X does not exist in the dictionary")
```

Finally, you can _update_ a dictionary by assigning to a lookup with the index operator. For instance, if we want to add the
key `'X'` with the value, `"Unknown"` to out `three_letter_codes` dictionary:

```python
three_letter_codes['X'] = "Unknown"
three_letter_codes
```

You can also use this pattern to modify an existing value:

```python
three_letter_codes['A'] = "This has been modified"
three_letter_codes
```

But let us change this back to `"Ala"` for now...

```python
three_letter_codes['A'] = "Ala"
three_letter_codes
```

[^1]: [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
