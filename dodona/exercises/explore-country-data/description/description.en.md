Now that you have the global temperature data in a form that's useful, you can turn your attention
to the temperature data for each country you will plot.

This time though, the data is not stored in a file. Instead you will have to access it over the
internet via a url. The same context manager patter applies though.

When you wrote your first version of the `parse_csv` function, you accepted a filename argument. You
discovered that writing the function this way made it hard to test and so more difficult to be
confident in it's correctness. This time, you will write a better, more testable version of
`parse_csv` which accepts any resource (from which you can `.read()`) OR a string and returns
a list of dictionaries keyed by column header and with values from each row of data in the CSV source.

This is a more generic version of `parse_csv`. It can read CSV data from a file, the internet, or
any resource that it is are provided. If it is provided a `str` then the data is CSV formatted data
for it to parse directly.

Here is an example CSV file:

```
Header1,Header2
123,456
```

Given this file as input, your function should produce:

```python
[{"Header1": 123, "Header2": 456}]
```

You can use this template:

```python
import csv

def parse_csv(csv_source) -> list[dict[str, str]]:
  ...
```

<details>
    <summary>Hint</summary>
    You should be prepared to handle 3 possible types of input:
    <ul>
        <li>
            A resource that you can read <code>bytes</code> from (which you will need to decode into a <code>str</code>),
        </li>
        <li>
            A resource that you can read <code>str</code> data from, or
        </li>
        <li>
            A <code>str</code>.
        </li>
    </ul>
    
    You can check the type of a variable by using the <code>type()</code> function like this:
    <code>type(variable_name) == bytes</code>
</details>

You can experiment with your code using these country URLS:

Belgium
: [https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/bel_data_orig.csv](https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/bel_data_orig.csv)

Russia
: [https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/rus_data_orig.csv](https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/rus_data_orig.csv)

Australia
: [https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/aus_data_orig.csv](https://cdn.jsdelivr.net/gh/vibbits/gentle-hands-on-python/data/aus_data_orig.csv)

In the sandbox use this to open the internet resource:
```python
from pyodide.http import open_url
open_url(url)
```

If you're using VSCodium you can use this to open the internet resource:
```python
from urllib import request
request.urlopen(url)
```
