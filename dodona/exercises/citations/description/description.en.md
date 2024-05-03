Write a function called `second_highest` that takes a list as input. Each value in the input
list is another list containing 2 values:

 1. The name of a country (a `str`), and
 2. The average number of citations per citable document produced within that country (a `float`).
 
 Your function should return the name of the country with the **second highest** number
 of average citations. If there are fewer than 2 values in the input list then your function
 should return `None`.
 
 <details>
   <summary>Data source</summary>
   Data sourced from <a href="https://www.scimagojr.com/countryrank.php?order=cd&ord=desc">here</a>.
 </details>

You can use this template:

```python
def second_highest(citations: list[list[str | float]]) -> str | None:
```

## Example

```console?lang=python&prompt=>>>
>>> second_highest([["Belgium", 31.34], ["Sweden", 33.23]])
"Belgium"
>>> second_highest([["Canada", 30.53], ["Singapore", 29.78], ["United Kingdom", 29.92]])
"United Kingdom"
>>> second_highest([["Barbados", 33.28]])

```

Do not forget to include a docstring and a test function called `test_second_highest` that returns `"Success"` if the `second_highest` function passes all tests.
