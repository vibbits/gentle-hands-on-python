def decrypt(ciphertext: bytes, key: int) -> str:
    """Decrypt text encoded by a Caesar cipher."""
    alphabet_start = int.from_bytes(b'A')
    alphabet_end = int.from_bytes(b'Z')
    alphabet_size = alphabet_end - alphabet_start + 1
    space = int.from_bytes(b' ')
    plaintext = []

    for letter in ciphertext:
        if letter == space:
            plaintext += [" "]
        else:
            index_of_encrypted = letter - alphabet_start
            index_of_decrypted = (index_of_encrypted - key) % alphabet_size
            decrypted = index_of_decrypted + alphabet_start
            plain = decrypted.to_bytes().decode()
            plaintext += [plain]

    return "".join(plaintext)

def test_decrypt():
    "Test Caesar cipher decryption."
    assert decrypt(b'', 1) == ""
    assert decrypt(b'PGSKY', 6) == "JAMES"
    return "Success"

with open("secret.txt", mode="rb") as secret:
    message = secret.read()

print(decrypt(message, 13))
