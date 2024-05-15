from datetime import datetime


def clean_global_data(observation: dict[str, str]) -> dict[str, float | datetime]:
    "Clean up the data in a global data observation."
    return {
        "Time": datetime.strptime(observation["Time"], "%Y-%m"),
        "Temperature": float(observation["Anomaly (deg C)"]),
    }


def test_clean_global_data():
    "Test the clean_global_data function."
    assert clean_global_data({"Time": "2021-05", "Anomaly (deg C)": -1.5}) == {
        "Time": datetime(2021, 5, 1),
        "Temperature": -1.5,
    }
    return "Success"
