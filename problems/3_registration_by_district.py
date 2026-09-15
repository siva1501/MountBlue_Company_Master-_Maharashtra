"""Company registration in 2015 by district."""

import csv
import re
from datetime import datetime

from bar_plots import bar_plot


ZIP_CODE_FILE = "data/zip_code_MH.csv"
COMPANY_FILE = "data/company_master_data_2026-09-12.csv"


def load_zip_code_data():
    """Create a mapping of pin code to district."""
    pin_to_district = {}

    with open(
        ZIP_CODE_FILE,
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            pin_code = row["Pin Code"].strip()
            district = row["District"].strip()

            if pin_code and district:
                pin_to_district[pin_code] = district

    return pin_to_district


def find_pin_code(address):
    """Find six-digit PIN code from address."""
    pin_codes = re.findall(r"\b\d{6}\b", address)

    if pin_codes:
        return pin_codes[-1]

    return ""


def registration_by_district(pin_to_district):
    """Count company registrations in 2015 by district."""
    district_count = {}

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

            try:
                year = datetime.strptime(
                    date,
                    "%Y-%m-%d",
                ).year
            except ValueError:
                continue

            if year != 2015:
                continue

            address = row["Company Address"].strip()
            pin_code = find_pin_code(address)

            district = pin_to_district.get(pin_code)

            if district:
                district_count[district] = (
                    district_count.get(district, 0) + 1
                )

    return district_count


def execute():
    """Run the company registration analysis."""
    pin_to_district = load_zip_code_data()

    district_count = registration_by_district(
        pin_to_district
    )

    sorted_data = sorted(
        district_count.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    print(
        "\nCompany Registration in 2015 by District\n"
    )

    for district, count in sorted_data:
        print(f"{district}: {count}")

    districts = [
        item[0]
        for item in sorted_data
    ]

    registrations = [
        item[1]
        for item in sorted_data
    ]

    bar_plot(
        x_bar=districts,
        y_bar=registrations,
        x_label="District",
        y_label="Number of Registrations",
        title="Company Registration in 2015 by District",
    )


if __name__ == "__main__":
    execute()
