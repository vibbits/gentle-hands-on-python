def truncate(text: str, max_len: int) -> str:
    "Truncate a string to at most max_len characters."
    ellipses = 3
    if 3 >= max_len:
        ellipses = max_len

    if len(text) > max_len:
        return text[: max_len - ellipses] + ("." * ellipses)

    return text


def test_truncate():
    "Tests for the truncate function."
    assert truncate("Hello World!", 11) == "Hello Wo..."
    assert truncate("Python", 10) == "Python"
    assert truncate("Python3", 7) == "Python3"
    assert truncate("Nina?", 4) == "N..."
    assert truncate("", 2) == ""
    assert truncate("Test", 3) == "..."
    assert truncate("Test", 2) == ".."
    assert truncate("Test", 1) == "."
    return "Success"
