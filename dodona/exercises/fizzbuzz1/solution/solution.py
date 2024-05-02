def fizzbuzz(number: int) -> str:
    "Check an answer for the fizzbuzz game."
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"


def test_fizzbuzz():
    "Tests for the fizzbuzz function."
    assert "Fizz" == fizzbuzz(33), 'Expected: "Fizz", got: ' + str(fizzbuzz(33))
    assert "Fizz Buzz" == fizzbuzz(30), 'Expected: "Fizz Buzz", got: ' + str(
        fizzbuzz(30)
    )
    assert "Buzz" == fizzbuzz(20), 'Expected: "Buzz", got: ' + str(fizzbuzz(20))
    return "Success"
