import numpy as np


def calculate_rmse(
    market_vols,
    model_vols
):

    rmse = np.sqrt(
        np.mean(
            (market_vols - model_vols) ** 2
        )
    )

    return rmse


def calculate_skew(
    vols
):

    skew = np.mean(vols[:3]) - np.mean(vols[-3:])

    return skew


def calculate_smile_curvature(
    strikes,
    vols
):

    coefficients = np.polyfit(
        strikes,
        vols,
        2
    )

    curvature = coefficients[0]

    return curvature


def volatility_statistics(vols):

    return {
        "Mean Volatility": np.mean(vols),
        "Max Volatility": np.max(vols),
        "Min Volatility": np.min(vols),
        "Std Dev": np.std(vols)
    }
