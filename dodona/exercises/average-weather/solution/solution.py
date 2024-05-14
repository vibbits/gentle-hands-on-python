def average_temperature(observations: list[dict[str, float]]) -> dict[str, float]:
    "Compute the average temperature from observations in region keys."
    sums = {}
    counts = {}
    for observation in observations:
        for region in observation:
            if region in sums:
                sums[region] = sums[region] + observation[region]
            else:
                sums[region] = observation[region]

            if region in counts:
                counts[region] = counts[region] + 1
            else:
                counts[region] = 1

    average = {}
    for region in sums:
        average[region] = sums[region] / counts[region]

    return average


def test_average_temperature():
    "Tests for the average_temperature function."
    assert average_temperature([]) == {}
    assert average_temperature([{"ABC": 2.0}, {"XYZ": -2.0}]) == {
        "ABC": 2.0,
        "XYZ": -2.0,
    }
    assert average_temperature(
        [{"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1}]
    ) == {"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1}
    assert average_temperature(
        [
            {"BEL": 5.7, "RUS": -12.8, "AUS": 42.6, "GLO": 22.1},
            {"BEL": 10.2, "RUS": -2.0, "AUS": 37.8, "GLO": 21.2},
            {"BEL": 14.7, "RUS": 1.3, "AUS": 18.3, "GLO": 23.6},
        ]
    ) == {"BEL": 10.2, "RUS": -4.5, "AUS": 32.9, "GLO": 22.3}
    assert average_temperature([{}, {"A": 1.5}, {"B": 0.5}, {"A": 2.5}]) == {
        "A": 2.0,
        "B": 0.5,
    }
    return "Success"
