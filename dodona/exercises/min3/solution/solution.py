def min3(a, b, c):
    "Return the least of all 3 arguments."
    if a < b:
        if a < c:
            return a
        return c

    if b < c:
        return b

    return c


def test_min3():
    "Tests for the min3 function."
    assert min3(3, 6, 9) == 3
    assert min3(-1, -5, 7) == -5
    assert min3(-1, -12, -47) == -47
    assert min3(-2, 1, -19) == -19
    assert min3(11, 55, 0) == 0
    assert min3(-100, -293, -551) == -551
    return "Success"
