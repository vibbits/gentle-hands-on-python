def fizzbuzz(numbers: list[int]) -> list[str]:
    "Play the fizzbuzz game."
    game = []
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            game += ["Fizz Buzz"]
        elif number % 3 == 0:
            game += ["Fizz"]
        elif number % 5 == 0:
            game += ["Buzz"]
        else:
            game += [str(number)]

    return game


def test_fizzbuzz():
    "Tests for the fizzbuzz function."
    assert fizzbuzz([1, 2, 3]) == ["1", "2", "Fizz"]
    assert fizzbuzz([4, 5, 6, 15]) == ["4", "Buzz", "Fizz", "Fizz Buzz"]
    assert fizzbuzz([]) == []
    return "Success"
