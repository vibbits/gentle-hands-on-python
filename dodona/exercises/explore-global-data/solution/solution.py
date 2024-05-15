def parse_csv(filename: str) -> dict[str, str]:
    "Parse the first data row of a csv file."
    with open(filename) as resource:
        headers = resource.readline().split(",")
        data = resource.readline().split(",")

    result = {}
    for index in range(len(headers)):
        result[headers[index]] = data[index]

    return result
