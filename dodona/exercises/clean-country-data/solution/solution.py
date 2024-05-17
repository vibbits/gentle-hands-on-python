from datetime import datetime


def clean_country_data(observation: dict[str, str]) -> dict[str, float | datetime]:
    "Clean up the data in a country data observation."
    return {
        "Time": datetime.strptime(
            observation["Year"] + observation["Statistics"], "%Y%b Average"
        ),
        "Temperature": float(observation["Temperature - (Celsius)"]),
    }


def test_clean_country_data():
    "Test the clean_country_data function."
    assert clean_country_data(
        {
            "Temperature - (Celsius)": "-5.76",
            "Year": "2002",
            "Statistics": "Feb Average",
            "Country": "Belgium",
            "ISO3": "BEL",
        }
    ) == {
        "Time": datetime(2002, 2, 1),
        "Temperature": -5.76,
    }
    return "Success"
