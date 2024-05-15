Write a function called `clean_global_data` that accepts a dictionary (row from the global data
CSV file) and returns a new dictionary containing "Time" (value as a `datetime`) and "Temperature"
(value as a `float`) keys.

Here is an example input dictionary:

```python
{
  'Time': '1901-05',
  'Anomaly (deg C)': '-0.24934465',
  'Lower confidence limit (2.5%)': '-0.44425672',
  'Upper confidence limit (97.5%)': '-0.05443258'
}
```

Given this input dictionary, your function should return:

```python
{
  'Time': datetime(1901, 5, 1, 0, 0),
  'Temperature': -0.24934465
}
```

You can use this template for your function:

```python
def clean_global_data(observation: dict[str, str]) -> dict[str, float | datetime]:
  ...
```

Here is an example execution of the function. Don't forget to include a docstring and a test function
called `test_clean_global_data` that returns `"Success"` if the `clean_global_data` function passes
all tests.

## Example

```console?lang=python&prompt=>>>
>>> clean_global_data({'Time': '1901-05','Anomaly (deg C)': '-0.24934465','Lower confidence limit (2.5%)': '-0.44425672','Upper confidence limit (97.5%)': '-0.05443258'})
{'Time': datetime(1901, 5, 1, 0, 0),'Temperature': -0.24934465}
```
