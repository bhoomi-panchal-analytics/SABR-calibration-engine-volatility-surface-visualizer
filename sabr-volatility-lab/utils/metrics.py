import numpy as np


def rmse(
    market_vols,
    model_vols
):

    return np.sqrt(
        np.mean(
            (market_vols - model_vols) ** 2
        )
    )


def mae(
    market_vols,
    model_vols
):

    return np.mean(
        np.abs(
            market_vols - model_vols
        )
    )


def skew_measure(vols):

    return np.mean(vols[:3]) - np.mean(vols[-3:])


def kurtosis_measure(vols):

    mean = np.mean(vols)

    std = np.std(vols)

    kurtosis = np.mean(
        ((vols - mean) / std) ** 4
    )

    return kurtosis
