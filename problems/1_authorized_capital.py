"""Plot companies by authorized capital."""

import csv

from bar_plots import bar_plot


DATA_CSV = "data/company_master_data_2026-09-12.csv"


def authorized_capital():
    """Count companies in authorized capital ranges."""

    ranges = {
        "<= 1L": 0,
        "1L to 10L": 0,
        "10L to 1Cr": 0,
        "1Cr to 10Cr": 0,
        "> 10Cr": 0,
    }

    with open(
        DATA_CSV,
        "r",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                capital = float(row["Authorized Capital"])
            except (ValueError, TypeError):
                continue

            if capital <= 100000:
                ranges["<= 1L"] += 1
            elif capital <= 1000000:
                ranges["1L to 10L"] += 1
            elif capital <= 10000000:
                ranges["10L to 1Cr"] += 1
            elif capital <= 100000000:
                ranges["1Cr to 10Cr"] += 1
            else:
                ranges["> 10Cr"] += 1

    print("\nAuthorized Capital:\n")

    for category, count in ranges.items():
        print(f"{category}: {count}")

    bar_plot(
        x_bar=ranges.keys(),
        y_bar=ranges.values(),
        x_label="Authorized Capital",
        y_label="Number of Companies",
        title="Companies by Authorized Capital",
    )


if __name__ == "__main__":
    authorized_capital()

