Write a function called `clean_country_data` that accepts a dictionary (row from the global data
CSV file) and returns a new dictionary containing "Time" (value as a `datetime`) and "Temperature"
(value as a `float`) keys.

Here is an example input dictionary:

```python
{
  'Temperature - (Celsius)': '5.76',
  'Year': '1901',
  'Statistics': 'May Average',
  'Country': 'Belgium',
  'ISO3': 'BEL'
}
```

Given this input dictionary, your function should return:

```python
{
  'Time': datetime(1901, 5, 1, 0, 0),
  'Temperature': 5.76
}
```

You can use this template for your function:

```python
def clean_country_data(observation: dict[str, str]) -> dict[str, float | datetime]:
  ...
```

Here is an example execution of the function. Don't forget to include a docstring and a test function
called `test_clean_country_data` that returns `"Success"` if the `clean_country_data` function passes
all tests.

## Example

```console?lang=python&prompt=>>>
>>> clean_country_data({'Temperature - (Celsius)': '5.76', 'Year': '1999', 'Statistics': 'Nov Average',
'Country': 'Belgium', 'ISO3': 'BEL'})
{'Time': datetime(1999, 11, 1, 0, 0), 'Temperature': 5.76}
```
