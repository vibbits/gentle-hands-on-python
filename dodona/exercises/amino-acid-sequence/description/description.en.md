Write a function called `one_to_three_letter_code` that accepts a single-letter amino-acid code sequence
(as a string) input argument and returns the list of associated three-letter-codes. If your user
supplies an invalid single-letter-code in the sequence you should skip that value in the resulting list.

```python
def one_to_three_letter_codes(sequence: str) -> list[str]:
    ...
```

You can should copy your solution from the previous exercise ("Dictionary lookup";  or any other
previous solutions you might find helpful) and use that function in your solution to this exercise.

Here are some example executions. Do not forget to include a docstring and a test function
called `test_one_to_three_letter_codes` that returns `"Success"` if the `one_to_three_letter_codes`
function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> one_to_three_letter_codes('')
[]
>>> one_to_three_letter_codes('EIKGGQ')
['Glu', 'Ile', 'Lys', 'Gly', 'Gly', 'Gln']
>>> one_to_three_letter_codes('AXG')
['Ala', 'Gly']
>>> one_to_three_letter_codes('James')
[]
```
