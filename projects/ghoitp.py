"""
A general purpose library of functions for the Gentle Hands-on Introduction
To Python course.
"""

import math


def expect(boolean, expected, received):
    """
    Error when boolean is TRUE: prints outputs
    Returns true on success and false otherwise
    """
    if boolean:
        print(f"Test FAILED: I expected {received} to be {expected}")
    else:
        print("Test PASSED")
    return not boolean


def expect_equal(expected, received):
    "Assert that expected should be equal to received"
    return expect(expected != received, expected, received)


def expect_close(expected, received):
    "Assert that two floating-point numbers are close in value"
    return expect(
        not math.isclose(expected, received), f"close to {expected}", received
    )


def expect_not_none(received):
    "Assert the a received valuer IS NOT None"
    return expect(received is None, "not None", received)
