# An initial attempt at plotting the global temperature data.


In order to follow along, you will need the global temperature loading function you built earlier.

A simple plotting function provided by `matplotlib` is called `bar()`. It has a lot of options but
you can start simply by passing it a list of x-values and a list of height-values
(e.g. some global temperature anomaly numbers).

```python
temperatures = []
for observation in global_data:
    temperatures = temperatures + [observation['Temperature']]
```

```python
plt.bar(x=range(len(temperatures)), height=temperatures)
```

We could also pass the list of dates to get useful x-axis markings.

```python
dates = []
for observation in global_data:
    dates = dates + [observation['Time']]
```

```python
plt.bar(x=dates, height=temperatures)
```

<img src="media/plot-output.png" alt="Bar plot output" style="width:80;height:auto">


This is not very satisfying though, and it's not the correct type of plot.
An alternative might be a `scatter()`.
