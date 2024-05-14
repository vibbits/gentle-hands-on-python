def frequencies(text: str) -> dict[str, int]:
    "Count the frequency of letters in the input string."
    freq = {}
    for letter in text:
        if letter in freq:
            freq[letter] = freq[letter] + 1
        else:
            freq[letter] = 1

    return freq


def test_frequencies():
    "Tests for the frequencies function."
    assert frequencies("") == {}
    assert frequencies("M") == {"M": 1}
    assert frequencies("Yes") == {"Y": 1, "e": 1, "s": 1}
    assert frequencies("Waat!") == {"W": 1, "a": 2, "t": 1, "!": 1}
    assert frequencies(
        "SFTMHGTPVVNQVKVLTESNRISHHKILAIVGTAESNSEHPLGTAITKYCKQELDTETLGTCIDFQVVPGCGISCKVTNIEGLLHKNNWNIEDNNIKNASLVQIDASNEQSSTSSSMIIDAQISNALNAQQYKVLIGNREWMIRNGLVINNDVNDFMTEHERKGRTAVLVAVDDELCGLIAIADT"
    ) == {
        "A": 12,
        "C": 5,
        "D": 10,
        "E": 12,
        "F": 3,
        "G": 11,
        "H": 6,
        "I": 18,
        "K": 9,
        "L": 14,
        "M": 4,
        "N": 18,
        "P": 3,
        "Q": 8,
        "R": 5,
        "S": 14,
        "T": 14,
        "V": 15,
        "W": 2,
        "Y": 2,
    }
    return "Success"
