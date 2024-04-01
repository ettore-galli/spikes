import csv


def main():
    filename = "./input/input.csv"
    NITEMS = 10
    with open(filename, "w", encoding="utf-8") as csvfile:
        csvwriter = csv.DictWriter(
            csvfile,
            ["INDEX", "VALUE"],
            delimiter="|",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )

        csvwriter.writeheader()

        for index in range(NITEMS):
            record = {
                "INDEX": index,
                "VALUE": int((NITEMS + index) ** 31 % (NITEMS)),
            }
            csvwriter.writerow(record)


if __name__ == "__main__":
    main()
