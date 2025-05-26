DNA sequencing machines not only produce the predicted DNA
sequence, but also a "[quality score](https://en.wikipedia.org/wiki/Phred_quality_score)".

In order for bioinformaticians to be able to share these data, the
[FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) data format is commonly used. In this exercise you will parse a FASTQ file, then
extract the length of the longest subsequence with the highest 
quality score.

For example, given these quality scores:

```python
scores = [0, 12, 8, 16, 16, 4, 9, 16, 9]
```

The highest quality score is `16` and it occurs 3 times in 2 contiguous regions: `[16, 16]` and `[16]`. The longest of those regions is `2`. So your function should return 2.

Write a function called `best_subsequence_length` that accepts a
previously opened file (or anything that can be `.read()`) to
`bytes`. It should return the length of the longest contiguous region of maximum
quality score **and** the maximum score value. You can find documentation for
the FASTQ file format [here](https://en.wikipedia.org/wiki/FASTQ_format).

If the length of the sequence does not match the length of the quality scores
you should raise a `ValueError("Quality scores do not match")`. If you find a
quality score lower than 33 you should raise a `ValueError("Quality score too low")`. If you find a quality score higher than 126 then you should raise a
`ValueError("Quality score too high")`. If there are not 4 lines in the file
then you should raise `ValueError("Invalid FASTQ data")`

Here is an example input FASTQ file:

```
@SEQUENCE
GGTATTGCCACTGGC
+
!''*((((***+))%
```

Given this input, your function:

```python
from pathlib import Path

with Path("test.fastq").open() as resource:
  best_subsequence_length(resource)
```

should evaluate to:
```python
[43, 1]
```

You can use this template for your function:

```python
import typing

def best_subsequence_length(data: typing.TextIO) -> list[int]:
  ...
```

Don't forget to include a docstring and a test function
called `test_best_subsequence_length` that returns `"Success"` if the `best_subsequence_length` function passes all tests.

## Example

```python
from pathlib import Path

def test_best_subsequence_length():
    path = Path("temporary.fastq")
    with path.open(mode="w") as setup:
        setup.write("@SEQ\nATGC\n+\nA2YY")

    with path.open() as resource:
        assert [89, 2] == best_subsequence_length(resource)
```
