def bronze_medal(scores: list[int]) -> int | None:
    "Find the score of the bronze medal winner."
    if len(scores) < 3:
        return None

    return sorted(scores, reverse=True)[2]


def test_bronze_medal():
    "Tests for the bronze_medal function."
    assert bronze_medal([]) == None
    assert bronze_medal([9, 15]) == None
    assert bronze_medal([20, 4, 17]) == 4
    assert bronze_medal([21, 15, 9, 19]) == 15
    assert bronze_medal([54, 56, 2, 1, 5223, 6, 23, 57, 3, 7, 3344]) == 57
    return "Success"
