# Review

In this chapter you've learned about the Python _dictionary_. It's a special collection that
stores an association (or mapping) between _keys_ and _values_. Due to this, the keys must be unique.



## Review Questions


<details>
    <summary>How is an empty dictionary written?</summary>
    <code>{}</code> or <code>dict()</code>
</details>

<details>
    <summary>Can any data type be a value in a dictionary?</summary>
    Yes!
</details>

<details>
  <summary>When you loop over a dictionary, what does the loop variable contain?</summary>
  The <em>key</em>, not the <em>value</em>.
</details>

<details>
    <summary>Can a list be a key in a dictionary?</summary>
    No. Lists are <em>mutable</em> (they can be modified after you create them) so they cannot be stable keys.
</details>

<details>
  <summary>How can you access a key you're not sure is in the dictionary?</summary>
  If the key is not in the dictionary you cannot access it. But you can check that it is <code>in</code> the dictionary first.
</details>

## Supporting material
* [Automate the Boring Stuff with Python, Chapter 5](http://automatetheboringstuff.com/2e/chapter5/)
* [Real Python: Dictionaries](https://realpython.com/python-dicts/)
