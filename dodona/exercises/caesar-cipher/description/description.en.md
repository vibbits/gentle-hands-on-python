I've left a secret message for you in a text file [here](media/secret.txt). Because it's very
secret I've encrypted it using a Caesar cipher.

Your task is to write a function to decrypt Caesar ciphertext. First let's understand what a Caesar
cipher does with an example:

Here is some text to encrypt: `"I CAN HAZ CHEESEBURGER"`. The Caesar cipher also needs a "key" which is a number
between 1 and 26. This number is used to "rotate" the plaintext input characters. For this example,
the key is `1`.

The first letter is `"I"`. `"I"` "rotated" by `1` is the letter after `"I"` which is `"J"`. So the
encrypted ciphertext is `"J"` so far.

The next letter is `" "`. Spaces are not changed by encryption and decryption so the encrypted
ciphertext is now: `"J "`.

The same logic applies to all lettes in the string up until `"Z"`. At this point the plaintext,
`"I CAN HA"` has been encryped to `"J DBO IB"`. To encrypt a `"Z"` you count back again from the
beginning of the alphabet. So the plaintext `"Z"` is encrypted to `"A"`.

This is why it's called a "rotation". If you write the latin alphabet, A...Z on a circular piece of
paper. Then again on a slightly smaller piece of paper. Rotate one of the circular pieces of paper by
the key and this gives the mapping between plaintext letters and ciphertext letters.

![Caesar cipher](https://gkaccess.com/wp-content/uploads/2020/01/Caesar_Cipher_GateKeeper_security_compliance_proximity_authentication_2fa_mfa-768x803.jpg)

The final encryption of the string `"I CAN HAZ CHEESEBURGER"` with a key of `1` is then:
`"J DBO IBA DIFFTFCVSHFS"`.

Your task is to write a function to decode caesar ciphers called `decrypt`. You can use this template:

```python
def decrypt(ciphertext: bytes, key: int) -> str:
  ...
```


You should also `print()` my message to the console using your `decrypt` function.
You can use a key of `13` to decode my message. The message is in a file called, `"secret.txt"`.

## Example

```console?lang=python&prompt=>>>
>>> decrypt(b'B NFTTBHF', 1)
"A MESSAGE"
>>> decrypt(b'', 12)
""
>>> decrypt(b'QBUN CM SIOL HUGY', 6)
"WHAT IS YOUR NAME"
>>> decrypt(b'HELLO WORLD', 26)
"HELLO WORLD"
```


Do not forget to include a docstring on your `decrypt` function and a test function called
`test_decrypt` that returns `"Success"` if the `decrypt` function passes all tests.
