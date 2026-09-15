"""Bar plot of company registration by year."""

import csv
from collections import Counter

from bar_plots import bar_plot


COMPANY_FILE = "data/company_master_data_2026-09-12.csv"


def registration_by_year():
    """Count company registrations by year."""
    year_count = Counter()

    with open(
        COMPANY_FILE,
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Company Registration Date"].strip()

            if not date:
                continue

            year = date[:4]
            year_count[year] += 1

    return year_count


def execute():
    """Run the registration analysis."""
    year_count = registration_by_year()

    print("\nCompany Registration by Year\n")

    for year in sorted(year_count):
        print(f"{year}: {year_count[year]}")

    years = sorted(year_count)
    registrations = [
        year_count[year]
        for year in years
    ]

    bar_plot(
        x_bar=years,
        y_bar=registrations,
        x_label="Years",
        y_label="Number of Registrations",
        title="Company Registration by Year",
    )


if __name__ == "__main__":
    execute()
