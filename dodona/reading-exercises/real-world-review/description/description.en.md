# Review

In this section you set up a programming environment, learned how to safely perform I/O operations on
files and network resources, and did some plotting using the third-party `matplotlib` library.
You used all of the skills you have developed in the course to create line plots of global and
selected regional climate data.

## Review Questions

<details>
  <summary>What does the `open()` function do?</summary>
  It makes an external resource such as a file or remote web URL available for <code>read()</code>ing and <code>write()</code>ing.
</details>

<details>
  <summary>If you open a file with the mode argument set to `"w"`, can you read data from the file?</summary>
  No. <code>"w"</code> means you can only <em>write</em> to the file.
</details>

<details>
  <summary>If you open an existing file with `mode="w"` and write to it, what happens to the original data?</summary>
  It's gone.
</details>

<details>
  <summary>How do you read the entire contents of a file into a string?</summary>
  Run the <code>read()</code> function on the context manager.
</details>

<details>
  <summary>How would you access line 5 of a file?</summary>
  Call the <code>readline()</code> function 5 times, ignoring the returned string the first 4 times.
</details>

<details>
  <summary>What is the difference between <code>bytes</code> and <code>str</code> types?</summary>
  <code>bytes</code> are uninterpreted bits if computer memory. <code>str</code> are those bytes interpreted as text.
</details>

<details>
  <summary>What is the name of the function used to create line plots?</summary>
  <code>plot()</code>
</details>

<details>
  <summary>Is it possible to change the plot colour?</summary>
  Yes, using the <code>color</code> argument to <code>plot()</code>
</details>

<details>
  <summary>Can you use <code>matplotlib</code> to plot a histogram?</summary>
  <a href="https://matplotlib.org/stable/gallery/statistics/hist.html">Yes.</a>
</details>
