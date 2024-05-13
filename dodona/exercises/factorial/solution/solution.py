import math
import random


def factorial(n: int) -> int:
    "Compute the factorial of n."
    result = 1
    for i in range(2, n + 1):
        result = result * i

    return result


def test_factorial():
    "Tests for the factorial function."
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(6) == 720
    for _ in range(20):
        n = random.randint(1, 100)
        assert factorial(n) == math.factorial(n)
    return "Success"
