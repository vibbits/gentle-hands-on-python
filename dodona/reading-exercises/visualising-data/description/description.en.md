# Visualising data

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

<div id="plot-output" style="width: 100%; min-height: 200px"></div>

<br>

> _"[...] the most important part of [...] research [is] being able to successfully communicate [...] results to clinicians"_
>
> -- Dr. Matthias Stahl [^1]

This will be your first taste of the enormous "ecosystem" of Python third-party libraries outside of
the standard library that comes packaged with Python itself. We will start out introducing how to
plot in general then move on to creating the plots
for the climate data.

Unfortunately you will need a development environment set up on you own computer in order to see the
results. If this isn't possible for you for whatever reason, please contact one of the course teachers
for alternative options.

`matplotlib` is a one of several Python plotting libraries but is possibly the most commonly used.

You can install it by running the command:

```bash
pip install matplotlib
```

`matplotlib.pyplot` is a collection of command style, plotting related functions that make matplotlib
work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates
a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps
track of things like the current figure and plotting area, and the plotting functions are directed to
the current subplot.

What we first have to do is importing the library of course.

```python
# You can do this in the console above
import matplotlib.pyplot as plt

```

[^1]: [Matthias Stahl's personal website](https://www.higsch.com/about/)
