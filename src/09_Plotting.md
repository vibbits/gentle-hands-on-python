---
title: "Plotting"
jupyter:
  nbformat: 4
  nbformat_minor: 5
  kernelspec:
    display_name: "Python 3 (ipykernel)"
    language: "python"
    name: "python3"
  language_info:
    codemirror_mode:
      name: "ipython"
      version: 3
    file_extension: ".py"
    mimetype: "text/x-python"
    name: "python"
    nbconvert_exporter: "python"
    pygments_lexer: "ipython3"
    version: "3.11.0"
---

# Visualising data

> _"[...] the most important part of [...] research [is] being able to successfully communicate [...] results to clinicians"_
>
> -- Dr. Matthias Stahl<sup><a href="#References">1</a></sup>

This chapter will be your first taste of the enormous "ecosystem" of Python third-party libraries outside of the standard library
that comes packaged with Python itself. We will start out introducing how to plot in general then move on to creating the plots
for the climate data.

`matplotlib` is a one of several Python plotting libraries but is possibly the most commonly used. When you began thid course
you installed the library already so you don't need to worry about installing it.

`matplotlib.pyplot` is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes
some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area,
decorates the plot with labels, etc. In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps
track of things like the current figure and plotting area, and the plotting functions are directed to the current subplot.

What we first have to do is importing the library of course.

::: {.cell .code}
```python
import matplotlib.pyplot as plt
```
:::

## Loading the cleaned data

At this point we can load the data we saved in the previous chapter and explore various ways of plotting it.

::: {.cell .code}
```python
import csv
from datetime import datetime

def load_data(filename):
    with open(filename) as file_resource:
        reader = csv.DictReader(file_resource)
    
        data = []
        for reading in reader:
            data = data + [{'Time': datetime.fromisoformat(reading['Time']), 'Temperature': float(reading['Temperature'])}]
    
    return data

global_data = load_data("data/global_data.csv")
bel_data = load_data("data/bel_data.csv")
rus_data = load_data("data/rus_data.csv")
aus_data = load_data("data/aus_data.csv")
```
:::

A simple plotting function provided by `matplotlib` is called `bar()`. It has a lot of options but you can start simply
by passing it a list of x-values and a list of height-values (e.g. some global temperature anomaly numbers).

::: {.cell .code}
```python
temperatures = []
for observation in global_data:
    temperatures = temperatures + [observation['Temperature']]
```
:::

::: {.cell .code}
```python
plt.bar(x=range(len(temperatures)), height=temperatures)
```
:::

We could also pass the list of dates to get useful x-axis markings.

::: {.cell .code}
```python
dates = []
for observation in global_data:
    dates = dates + [observation['Time']]
```
:::

::: {.cell .code}
```python
plt.bar(x=dates, height=temperatures)
```
:::

This is not very satisfying though, and it's not the correct type of plot. An alternative might be a `scatter()`.


---

### Exercise 9-1: Scatter plot

Plot the global climate data using a scatter plot.

::: {.cell .code}
```python

```
:::

---

### Exercise 9-2: Add axis labels and a title

Plot the global climate data using a scatter plot and add axis labels with `xlabel()`, `ylabel()` and `title()`.

::: {.cell .code}
```python

```
:::

---

This is getting closer to the result we want. But it's still not the right kind of plot. We need a line plot.

---

### Exercise 9-3: A line plot

Use the documentation [here](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html), and the plot gallery
[here](https://matplotlib.org/stable/gallery/), to draw a line plot of the global temperature anomaly data. Make sure you
add axis labels and a title. Experiment with adding and changing line colours with the `color` parameter.

::: {.cell .code}
```python

```
:::

---

Beautiful! However there is a lot of noise, it might be useful to display smoothed data<sup>2</sup>. One way of
smoothing these data is by taking a moving average over a window of, say, 2 years (24 months). So let's do that now.
The first function we need is something you've done before: compute an average observation.

::: {.cell .code}
```python
def average_observation(observations):
    temp_sum = 0
    for observation in observations:
        temp_sum = temp_sum + observation['Temperature']
    
    return {
        'Temperature': temp_sum / len(observations),
        'Time': observations[len(observations) // 2]['Time']
    }

assert { 'Temperature': 1.1, 'Time': datetime(2022, 12, 1) } == average_observation([{ 'Temperature': 1.1, 'Time': datetime(2022, 12, 1) }])
assert { 'Temperature': 0, 'Time': datetime(2000, 1, 1) } == average_observation([
    { 'Temperature': -5, 'Time': datetime(1990, 5, 1) },
    { 'Temperature': 5, 'Time': datetime(2000, 1, 1) }
])
```
:::

Since our `average_observation()` function computes the average for an entire list of observations
we need a way to _select_ all overlapping sub-lists and pass them along to our function. This is
a _moving window_.

::: {.cell .code}
```python
def moving_window(data, window_size: int):
    windows = []
    for window_begin in range(len(data) - window_size + 1):
        windows = windows + [data[window_begin:(window_begin + window_size)]]
    
    return windows

assert moving_window([], 5) == []
assert moving_window("ABCDEFG", 4) == ["ABCD", "BCDE", "CDEF", "DEFG"]
```
:::

Finally we need to apply `average_observation()` to each of the windows we get
from `moving_window()`.

::: {.cell .code}
```python
def smoothed(data, window_size: int):
    smooth = []
    windows = moving_window(data, window_size)
    for window in windows:
        smooth = smooth + [average_observation(window)]
    
    return smooth
```
:::

Now we can use this function to plot the original data and a smoothed line on top of it. But first,
splitting the data is a little awkward and repetitive so lets write a little function to do that.

::: {.cell .code}
```python
def split_data(data):
    temps = []
    dates = []
    for observation in data:
        temps = temps + [observation['Temperature']]
        dates = dates + [observation['Time']]
    
    return { 'Temperatures': temps, 'Dates': dates}
```
:::

Now we're finally ready to create a plot for the global temperature data.

---

### Exercise 9-4: Plot global temperature anomaly

Create a plot of the global temperature anomaly. Include the un-smoothed and smoothed data in
a line plot. Label axes and include a plot title.

::: {.code .cell}
```python

```
:::

---

### Exercise 9-5: Plot per-region data

Create plots for each region (Belgium, Russia, and Australia) in the same way as you did for
the global data. Once you do this, you will see that it is difficult to see any trend in
these plots due to the noise. So limit the range of the y-axis around the smoothed plot, do you
see a pattern now?

::: {.cell .code}
```python

```
:::

::: {.cell .code}
```python

```
:::

::: {.cell .code}
```python

```
:::

---

## Chapter Review

In this chapter you learned how to use you first third-party library in Python: `matplotlib`.
You used it to create bar and scatter plots with axes labeled and plot titles. Finally you
created line plots of global and selected regional climate data.

### Review Questions

1. What is the name of the function used to create line plots?
<details>
    <summary>Answer</summary>
    <code>plot()</code>
</details>

2. Is it possible to change the plot colour?
<details>
    <summary>Answer</summary>
    Yes, using the <code>color</code> argument to <code>plot()</code>
</details>

3. Can you use <code>matplotlib</code> to plot a histogram?
<details>
    <summary>Answer</summary>
    <a href="https://matplotlib.org/stable/gallery/statistics/hist.html">Yes.</a>
</details>

## References

1. [Matthias Stahl's personal website](https://www.higsch.com/about/)
2. [Data smoothing](https://www.climate4you.com/DataSmoothing.htm)

## Supporting material

* [Become a Python Data Analyst](https://www.packtpub.com/eu/big-data-and-business-intelligence/become-python-data-analyst)
* [Add confidence interval on barplot](https://python-graph-gallery.com/8-add-confidence-interval-on-barplot/)
* [Matplotlib Cheatsheets](https://github.com/matplotlib/cheatsheets#cheatsheets)

## Next session

Go to our [next chapter](10_Conclusion.ipynb). 
