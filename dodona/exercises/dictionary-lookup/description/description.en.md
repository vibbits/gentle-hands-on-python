Write a function called `lookup_three_letter_code` that accepts a single-letter amino-acid code as
an input argument and returns the associated three-letter-code. If your user supplies an invalid
single-letter-code you should return `None`.

```python
def lookup_three_letter_code(single_letter_code: str) -> str:
    ...
```

You can use the `three_letter_codes` dictionary from earlier:

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
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_lookup_three_letter_code` that returns `"Success"` if the `lookup_three_letter_code`
function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> lookup_three_letter_code('A')
'Ala'
>>> lookup_three_letter_code('R')
'Arg'
>>> lookup_three_letter_code('X') == None
True
>>> lookup_three_letter_code('James') == None
True
```
