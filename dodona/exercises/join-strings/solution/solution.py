def joining(values: list[str], connector: str) -> str:
    "Join a list of strings together seperated by a connector."
    result = ""
    for val in values[:-1]:
        result = result + val + connector

    if len(values) > 0:
        result = result + values[-1]
    return result


def test_joining():
    "Tests for the joining function."
    assert joining([], "!") == ""
    assert joining(["Hello"], "+++") == "Hello"
    assert joining(["My", "name", "is"], "--") == "My--name--is"
    assert joining(["1", "+", "3"], ", ") == "1, +, 3"
    assert joining(["a", "b", "c", "d"], " ~ ") == "a ~ b ~ c ~ d"
    assert joining(["A", "B", "C", "D"], "") == "ABCD"
    return "Success"
