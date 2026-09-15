"""Company Master - Maharashtra analysis."""

import csv
import re
from collections import Counter, defaultdict
from datetime import datetime

import matplotlib.pyplot as plt


COMPANY_FILE = "data/company_master_data_2026-09-12.csv"
ZIP_CODE_FILE = "data/zip_code_MH.csv"


def bar_plot(x_bar, y_bar, x_label, y_label, title):
    """Create and display a bar plot."""
    plt.figure(figsize=(12, 6))
    plt.bar(x_bar, y_bar)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grouped_bar_plot(
    counts,
    years,
    categories,
    x_label,
    y_label,
    title,
):
    """Create and display a grouped bar plot."""
    plt.figure(figsize=(14, 7))

    width = 0.15
    positions = list(range(len(years)))

    for index, category in enumerate(categories):
        values = [
            counts[year][category]
            for year in years
        ]

        plot_positions = [
            position + index * width
            for position in positions
        ]

        plt.bar(
            plot_positions,
            values,
            width=width,
            label=category,
        )

    center = (len(categories) - 1) * width / 2

    plt.xticks(
        [
            position + center
            for position in positions
        ],
        years,
    )

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.tight_layout()

    plt.show()


# Problem 1
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
        COMPANY_FILE,
        "r",
        encoding="utf-8",
        newline="",
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


# Problem 2
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


# Problem 3
def load_zip_code_data():
    """Create a mapping of PIN code to district."""
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


def registration_by_district():
    """Count company registrations in 2015 by district."""
    pin_to_district = load_zip_code_data()
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


# Problem 4
def load_data():
    """Load company registration data."""
    registrations = []

    with open(
        COMPANY_FILE,
        "r",
        encoding="utf-8",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Company Registration Date"].strip()
            activity = row[
                "Company Industrial Classification"
            ].strip()

            if not date or not activity:
                continue

            try:
                year = datetime.strptime(
                    date,
                    "%Y-%m-%d",
                ).year
            except ValueError:
                continue

            registrations.append((year, activity))

    return registrations


def find_top_activities(registrations, years):
    """Find the top five business activities."""
    activity_count = Counter()

    for year, activity in registrations:
        if year in years:
            activity_count[activity] += 1

    return [
        activity
        for activity, _ in activity_count.most_common(5)
    ]


def count_registrations(
    registrations,
    years,
    activities,
):
    """Count registrations by year and activity."""
    counts = defaultdict(lambda: defaultdict(int))

    for year, activity in registrations:
        if year in years and activity in activities:
            counts[year][activity] += 1

    return counts


def grouped_activity_analysis():
    """Run the grouped business activity analysis."""
    registrations = load_data()

    all_years = sorted(
        {year for year, _ in registrations}
    )

    years = all_years[-10:]

    activities = find_top_activities(
        registrations,
        years,
    )

    counts = count_registrations(
        registrations,
        years,
        activities,
    )

    print(
        "\nTop 5 Business Activities - Last 10 Years\n"
    )

    for year in years:
        print(f"\n{year}")

        for activity in activities:
            print(
                f"{activity}: "
                f"{counts[year][activity]}"
            )

    grouped_bar_plot(
        counts=counts,
        years=years,
        categories=activities,
        x_label="Year",
        y_label="Number of Registrations",
        title="Top 5 Business Activities - Last 10 Years",
    )


def main():
    """Display the main menu."""
    while True:
        print("\nCompany Master - Maharashtra")
        print("1. Companies by Authorized Capital")
        print("2. Company Registration by Year")
        print("3. Company Registration in 2015 by District")
        print("4. Top 5 Business Activities - Last 10 Years")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            authorized_capital()
        elif choice == "2":
            registration_by_year()
        elif choice == "3":
            registration_by_district()
        elif choice == "4":
            grouped_activity_analysis()
        elif choice == "0":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

