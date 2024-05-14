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


def test_lookup_three_letter_codes():
    "Tests for the lookup_three_letter_code function."
    assert lookup_three_letter_codes("A") == "Ala"
    assert lookup_three_letter_codes("F") == "Phe"
    assert lookup_three_letter_codes("W") == "Trp"
    assert lookup_three_letter_codes("") == None
    assert lookup_three_letter_codes("WAT") == None
    assert lookup_three_letter_codes("Met") == None
    return "Success"
