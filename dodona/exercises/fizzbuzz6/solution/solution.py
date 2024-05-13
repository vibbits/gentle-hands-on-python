def fizzbuzz(up_to: int) -> list[str]:
    "Play the fizzbuzz game."
    game = []
    for number in range(1, up_to + 1):
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
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    assert fizzbuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "Fizz Buzz",
    ]
    assert fizzbuzz(0) == []
    assert fizzbuzz(-1) == []
    assert fizzbuzz(10) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
    ]
    assert fizzbuzz(30) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "Fizz Buzz",
        "16",
        "17",
        "Fizz",
        "19",
        "Buzz",
        "Fizz",
        "22",
        "23",
        "Fizz",
        "Buzz",
        "26",
        "Fizz",
        "28",
        "29",
        "Fizz Buzz",
    ]
    return "Success"
