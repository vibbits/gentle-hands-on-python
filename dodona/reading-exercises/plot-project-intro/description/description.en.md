# A new project

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://pyodide.org/en/stable/console.html"></iframe>

During the course so far, you wrote a program to play the childrens "Fizz Buzz" game.
You have outgrown this project. Now that you're more familiar with Python you can write a more
interesting programs. This time, imagine that you've been commisioned to
generate plots from temperature data for 3 countries and a global plot to compare against:

  - Belgium
  - Russia
  - Australia

You have some data sources:

  * [Global](https://hadleyserver.metoffice.gov.uk/hadcrut5/data/current/download.html)
  * [Belgium](https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.05/crucy.2103081329.v4.05/countries/tmp/crucy.v4.05.1901.2020.Belgium.tmp.per)
  * [Russia](https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.05/crucy.2103081329.v4.05/countries/tmp/crucy.v4.05.1901.2020.Russia.tmp.per)
  * [Australia](https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.05/crucy.2103081329.v4.05/countries/tmp/crucy.v4.05.1901.2020.Australia.tmp.per)

At the end of this project you will produce a plot like this one:

<img src="media/global_climate_plot.png" alt="Global temperature anomally 1961-90" style="width: 100%;height:auto">

The task essentially breaks down into these high-level steps:

1. Model the data
1. Fetch the data
1. Clean the data
1. Align the data
1. Average/smooth the data
1. Plot the data

You will perform all of these steps in Python to explore some deeper practical aspects of programming.
Your first task is to model the data.
