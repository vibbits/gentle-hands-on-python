In order to understand how to use the data in a file, you need to understand what's in it. As you
saw earlier, the `read()` function reads all the data from the file. The
[global data file](media/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv) is probably
quite large though so let's try to see just the beginning.
You have 2 options: The `readline()` function will read up to a new line character, or you could pass
an argument to the `read()` function that is the number of characters to read.


```python
with open("HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv") as global_data_manager:
    first_line = global_data_manager.readline()
    second_line = global_data_manager.readline()
    
print(first_line + second_line)
```

As you might guess from the filename extension (`.csv`) this is a Comma Seperated Values (CSV)
formatted file. CSV is a tabular data serialization format that uses commas (`","`) to seperate
columns and newlines (`"\n"`) to seperate rows of data.

In this exercise, your task is to write a function called `parse_csv` to parse the first row of data
from a CSV formatted file. Your function should take a single argument, the file name. And it
should output a dictionary. The dictionary should be keyed by the CSV column headers and the values
should come from the first row of data.

Here is an example CSV file:

```
Header1,Header2
123,456
```

Given this file as input, your function should produce:

```python
{"Header1": 123, "Header2": 456}
```

<details>
  <summary>Hint: A useful function for this exercise</summary>
  You can "split" a string by a delimiter (for example a <code>","</code> character) you can use the
  <code>.split()</code> method on strings like this: <code>"123,456".split(",") == ["123", "456"]</code>
</details>

You can use this template:

```python
def parse_csv(filename: str) -> dict[str, str]:
  ...
```

You do not need to write a test for this function. Can you think of why it is difficult to test?
How would you change the function interface to make it more easily testable?
