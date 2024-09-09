# Binary Data

<iframe style="width: 100%; height:380px; position:sticky; top:30px" src="https://vibbits.github.io/gentle-hands-on-python/"></iframe>

Your computes stores data as binary `1`'s and `0`'s. You can think of your computer memory as a really
big list of binary digits. As a programmer, it's your job to interpret and manipulate this big list
of binary digits. Everything you have done so far and everything you will do it just binary digits.

Computers usually don't operate on a single bit at a time though. Adjacent bits can be grouped,
8 bits at a time, into something called a _byte_. A byte is the smallest unit of data that your computer
reads and writes to it's memory.

Lets look at some examples. First some raw binary data. In some sense your job as a programmer is to
interpret and manipulate these patterns of bits. I've grouped this bit pattern into groups of 8
bits each. This bit pattern has a size of 4 bytes.

```python
# The '0b' prefix is to tell Python that this is raw binary data.
0b11110000_10011111_10011000_10001010
```

If you enter that into the console above you'll see the decimal number `4036991114`. This is how
that bit pattern is interpretted as an integer by the computer.

```python
# Binary representation of the the decimal integer 4036991114
bin(4036991114)
```

But, you can also tell the computer to interpret that bit pattern as a string.

```python
# String representation of the same bit pattern
0b11110000_10011111_10011000_10001010.to_bytes(4).decode()
```

I first re-interpreted the binary integer as raw (uninterpreted) binary data, then I
re-interpreted those raw bytes again as a string. So whenever you see 😊 you'll know that these
bits are being used to represent that emoji 😊.

## Text encoding

Earlier in the course we described strings as strings of characters and character as simply numbers
that are interpreted as letters. This is what we meant. Unfortunately for us there are
[many](https://www.iana.org/assignments/character-sets/character-sets.xhtml) ways people have
invented to assign numbers to characters (encode). Fortunately for us there is a single encoding
that is overwhelmingly common now, called [UTF-8](https://en.wikipedia.org/wiki/UTF-8). This is
what maps the number `403699114` to the 😊 character. I could have used a different encoding...

```python
# String representation of the same bit pattern
0b11110000_10011111_10011000_10001010.to_bytes(4).decode("latin_1")
```

Which produced nonsense. Clearly this text is not encoded with the
[Latin-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) encoding scheme.

