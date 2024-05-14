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


def one_to_three_letter_codes(sequence: str) -> list[str]:
    "Translate a sequence of single-letter amino acid codes to a sequence of three-letter codes."
    result = []
    for element in sequence:
        three_letter_code = lookup_three_letter_codes(element)
        if three_letter_code != None:
            result = result + [three_letter_code]

    return result


def test_one_to_three_letter_codes():
    "Tests for the one_to_three_letter_code function."
    assert one_to_three_letter_codes("") == []
    assert one_to_three_letter_codes("FIK") == ["Phe", "Ile", "Lys"]
    assert one_to_three_letter_codes("W") == ["Trp"]
    assert one_to_three_letter_codes("bat") == []
    assert one_to_three_letter_codes("Wat!") == ["Trp"]
    assert one_to_three_letter_codes("Met") == ["Met"]
    return "Success"
