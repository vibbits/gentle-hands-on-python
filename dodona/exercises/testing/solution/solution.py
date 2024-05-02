def fractional_part(number: float) -> float:
    """Find the fractional part of an input floating point number."""
    int_part = int(number)
    frac_part = number - int_part
    return abs(frac_part)


def test_fractional_part():
    assert fractional_part(0.0) == 0.0
    assert abs(fractional_part(5.2) - 0.2) < 0.00001
    assert abs(fractional_part(-2.26) - 0.26) < 0.00001
    assert abs(fractional_part(-0.111) - 0.111) < 0.00001
