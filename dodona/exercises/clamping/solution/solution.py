def clamp(number: int, lower: int, upper: int) -> int:
    "Ensure a number fits within a range between defined inclusive lower and upper bounds."
    if number < lower:
        return lower
    if number > upper:
        return upper

    return number


def test_clamp():
    "Tests for the clamp function."
    assert 0 == clamp(-5, 0, 10), "Input: -5, expected:  0, got: " + str(
        clamp(-5, 0, 10)
    )
    assert 0 == clamp(0, 0, 10), "Input:  0, expected:  0, got: " + str(clamp(0, 0, 10))
    assert 5 == clamp(5, 0, 10), "Input:  5, expected:  5, got: " + str(clamp(5, 0, 10))
    assert 10 == clamp(10, 0, 10), "Input: 10, expected: 10, got: " + str(
        clamp(10, 0, 10)
    )
    assert 10 == clamp(11, 0, 10), "Input: 11, expected: 10, got: " + str(
        clamp(11, 0, 10)
    )
    return "Success"
