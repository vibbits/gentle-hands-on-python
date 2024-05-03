import operator


def second_highest(citations: list[list[str | float]]) -> str | None:
    "Find the contry with the second most average citations per citable document."
    if len(citations) < 2:
        return None

    return sorted(citations, key=operator.itemgetter(1), reverse=True)[1][0]


def test_bronze_medal():
    "Tests for the bronze_medal function."
    assert second_highest([]) == None
    assert second_highest([["Barbados", 33.28]]) == None
    assert second_highest([["A", 1.0], ["B", 1.5]]) == "A"
    assert second_highest([["A", 1.5], ["B", 1.0]]) == "B"
    assert second_highest([["A", 1.0], ["B", 1.5], ["C", 1.2]]) == "C"
    assert second_highest([["Belgium", 31.34], ["Sweden", 33.23]]) == "Belgium"
    assert (
        second_highest(
            [["Canada", 30.53], ["Singapore", 29.78], ["United Kingdom", 29.92]]
        )
        == "United Kingdom"
    )
    return "Success"
