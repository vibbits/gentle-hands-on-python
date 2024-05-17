import csv


def parse_csv(csv_source) -> list[dict[str, str]]:
    "Parse all rows of data from csv_source emitting CSV formatted data."
    result = []
    source = csv_source
    if type(csv_source) != str:
        # It's a resource then
        source = csv_source.read()

    if type(source) == bytes:
        source = csv_source.decode()

    for row in csv.DictReader(source.splitlines()):
        result = result + [row]

    return result
