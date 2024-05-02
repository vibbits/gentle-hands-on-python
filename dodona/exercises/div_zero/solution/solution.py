def safe_div(dividend: float, divisor: float) -> float:
    "Divide numbers without crashing the program."
    if divisor == 0:
        return "You cannot divide by zero"

    return dividend / divisor


def test_safe_div():
    "Tests for the safe_div function."
    assert "You cannot divide by zero" == safe_div(5, 0)
    assert 2.5 == safe_div(5, 2)
    assert abs(1.4 - safe_div(7, 5)) < 0.00001
    return "Success"
