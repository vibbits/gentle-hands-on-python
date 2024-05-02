def odd_or_even(num: int) -> str:
    "Check if a number is odd or even."
    if num % 2 == 0:
        return "even"

    return "odd"


def test_odd_or_even():
    "Tests for the odd_or_even function."
    assert "even" == odd_or_even(0)
    assert "odd" == odd_or_even(1)
    assert "even" == odd_or_even(-2)
    return "Success"
