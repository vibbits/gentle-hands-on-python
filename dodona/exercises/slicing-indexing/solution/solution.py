def reverse_second(arg):
    "Reverse the second element of a nested list."
    if len(arg) >= 2:
        return [arg[0], arg[1][::-1]] + arg[2:]
    else:
        return arg


def test_reverse_second():
    "Tests for the reverse_second function."
    assert reverse_second([[1]]) == [[1]], "Expected [[1]], got: " + str(
        reverse_second([[1]])
    )
    assert reverse_second([[1], [2]]) == [[1], [2]], "Expected [[1], [2]], got: " + str(
        reverse_second([[1], [2]])
    )
    assert reverse_second([[1, 5], [10, 9, 8]]) == [
        [1, 5],
        [8, 9, 10],
    ], "Expected [[1, 5], [8, 9, 10]], got: " + str(
        reverse_second([[1, 5], [10, 9, 8]])
    )
    assert reverse_second([1, ["h", "e", "l", "l", "o"], 2]) == [
        1,
        ["o", "l", "l", "e", "h"],
        2,
    ], "Expected [1, ['o', 'l', 'l', 'e', 'h'], 2], got: " + str(
        reverse_second([1, ["h", "e", "l", "l", "o"], 2])
    )
    return "Success"
