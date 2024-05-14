def summing(ns: list[int | float]) -> int | float:
    "Compute the sum of a list of numbers."
    result = 0
    for i in ns:
        result = result + i

    return result


def test_summing():
    "Tests for the summing function."
    assert summing([]) == 0
    assert summing([1]) == 1
    assert summing([2]) == 2
    assert summing([1, 2, 3]) == 6
    assert summing([18, -4, 6, 4]) == 24
    assert summing([-10, -5, -2, 1, 7, 11]) == 2
    return "Success"
