import sys

import matplotlib.pyplot as plt
from datetime import datetime
import csv


def scatter_plot_global_data(data: list[dict[str, float | datetime]]) -> None:
    dates = []
    temps = []
    for observation in data:
        dates = dates + [observation["Time"]]
        temps = temps + [observation["Temperature"]]

    plt.scatter(dates, temps)
    plt.xlabel("Date")
    plt.ylabel("Temperature Anomaly")
    plt.title("Global Average Temperature Anomaly")
    plt.savefig("output.png")


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        data = []
        for reading in reader:
            data = data + [
                {
                    "Time": datetime.fromisoformat(reading["Time"]),
                    "Temperature": float(reading["Temperature"]),
                }
            ]

    scatter_plot_global_data(data)
