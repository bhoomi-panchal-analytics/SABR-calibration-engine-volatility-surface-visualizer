import numpy as np


def percentage_change(
    old,
    new
):

    return (
        (new - old)
        / old
    ) * 100


def normalize_array(arr):

    arr = np.array(arr)

    return (
        arr - np.min(arr)
    ) / (
        np.max(arr)
        - np.min(arr)
    )


def format_large_number(num):

    if num >= 1_000_000_000:
        return f"{num/1_000_000_000:.2f}B"

    if num >= 1_000_000:
        return f"{num/1_000_000:.2f}M"

    if num >= 1_000:
        return f"{num/1_000:.2f}K"

    return str(num)


def annualize_volatility(vol):

    return vol * np.sqrt(252)
