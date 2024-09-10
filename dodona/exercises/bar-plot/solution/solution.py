import csv
from datetime import datetime

import matplotlib.pyplot as plt

def clean_global_data(raw: dict[str, str]) -> dict:
    return {
        "time": datetime.strptime(raw["Time"], "%Y-%m"),
        "temperature": float(raw["Anomaly (deg C)"])
    }

def parse_global_data(filename: str) -> list[dict]:
    data = []
    with open(filename) as raw:
        reader = csv.DictReader(raw)
        for row in reader:
            data.append(clean_global_data(row))

def times(data: list[dict]) -> list[datetime]:
    t = []
    for obs in data:
        t.append(obs["time"])

    return t

def temperatures(data: list[dict]) -> list[float]:
    t = []
    for obs in data:
        t.append(obs["temperature"])
    return t

def bar_plot_global(filename: str):
    data = parse_global_data(filename)
    xaxis = times(data)
    yaxis = temperatures(data)

    return plt.bar(x=xaxis, height=yaxis)
