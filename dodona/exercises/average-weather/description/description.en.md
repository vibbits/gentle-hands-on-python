Write a function called `average_temperature` that accepts a list of observation dictionaries as input
and computes the average value for each key over all observations.
Your function should return an observation with the average values for each key. This is a dictionary
with the union of all keys in the input dictionaries. You should not make any assumptions about
which keys (if any) exist in the observation dictionaries.

To complete this exercise you will need to loop over dictionaries. Thankfully this operation will
feel very familiar to you because it works the same way as with lists. The loop variable gets
the keys from the dictionary.

You can use this template:

```python
def average_temperature(observations: list[dict[str, float]]) -> dict[str, float]:
    ...
```

Here are some example executions. Do not forget to include a docstring and a test function
called `test_average_temperature` that returns `"Success"` if the `average_temperature`
function passes all tests.

## Example

```console?lang=python&prompt=>>>
>>> average_temperature([])
{}
>>> average_temperature([{"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1}])
{"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1}
>>> average_temperature([{"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1}, {"BEL": 10.2, "RUS": -2.0, "AUS": 37.8, "GLO": 21.2}, {"BEL": 14.7, "RUS": 1.3, "AUS": 18.3, "GLO": 23.6}])
{"BEL": 10.2, "RUS": -4.5, "AUS": 32.9, "GLO": 22.3}
>>> average_temperature([{"ABC": 12.3}, {"XYZ": 1.8}])
{"ABC": 12.3, "XYZ": 1.8}
```
