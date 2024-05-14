def lookup_three_letter_codes(single_letter_code: str) -> str:
    "Return the three-letter-code for the input single-letter-code."
    three_letter_codes = {
        "A": "Ala",
        "C": "Cys",
        "D": "Asp",
        "E": "Glu",
        "F": "Phe",
        "G": "Gly",
        "H": "His",
        "I": "Ile",
        "K": "Lys",
        "L": "Leu",
        "M": "Met",
        "N": "Asn",
        "P": "Pro",
        "Q": "Gln",
        "R": "Arg",
        "S": "Ser",
        "T": "Thr",
        "V": "Val",
        "W": "Trp",
        "Y": "Tyr",
    }
    if single_letter_code in three_letter_codes:
        return three_letter_codes[single_letter_code]

    return


def one_to_three_letter_code(sequence: str) -> list[str]:
    result = []
    for element in sequence:
        three_letter_code = lookup_three_letter_codes(element)
        if three_letter_code != None:
            result = result + three_letter_code

    return result


def test_one_to_three_letter_code():
    "Tests for the one_to_three_letter_code function."
    assert one_to_three_letter_code("") == []
    assert one_to_three_letter_code("FIK") == ["Phe", "Ile", "Lys"]
    assert one_to_three_letter_code("W") == ["Trp"]
    assert one_to_three_letter_code("bat") == []
    assert one_to_three_letter_code("Wat!") == ["Trp"]
    assert one_to_three_letter_code("Met") == ["Met"]
    return "Success"
