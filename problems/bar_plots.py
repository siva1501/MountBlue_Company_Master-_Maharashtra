"""Common plotting functions."""

import matplotlib.pyplot as plt


def bar_plot(
    x_bar,
    y_bar,
    x_label,
    y_label,
    title,
):
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