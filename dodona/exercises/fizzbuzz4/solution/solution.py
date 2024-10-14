def fizzbuzz(counted: list[int]) -> list[int | str]:
    "Check an answer for the fizzbuzz game."
    counted[2::3] = ["Fizz"] * (len(counted) // 3)
    counted[4::5] = ["Buzz"] * (len(counted) // 5)
    return counted


def test_fizzbuzz():
    "Tests for the fizzbuzz function."
    assert fizzbuzz([]) == []
    assert fizzbuzz([1, 2, 3, 4, 5]) == [1, 2, "Fizz", 4, "Buzz"]
    assert fizzbuzz(['a', 'b', 'c', 'd', 'e']) == ['a', 'b', "Fizz", 'd', "Buzz"]
    return "Success"

if __name__ == "__main__":
    test_fizzbuzz()
