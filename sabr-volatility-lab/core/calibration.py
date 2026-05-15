import numpy as np

from scipy.optimize import minimize

from core.sabr_model import sabr_vol


def objective_function(
    params,
    F,
    strikes,
    T,
    market_vols
):

    alpha, beta, rho, nu = params

    model_vols = np.array([
        sabr_vol(
            F,
            k,
            T,
            alpha,
            beta,
            rho,
            nu
        )
        for k in strikes
    ])

    error = np.mean(
        (model_vols - market_vols) ** 2
    )

    return error


def calibrate_sabr(
    F,
    strikes,
    T,
    market_vols
):

    initial_guess = [
        0.2,    # alpha
        0.5,    # beta
        0.0,    # rho
        0.5     # nu
    ]

    bounds = [
        (0.0001, 5.0),
        (0.0, 1.0),
        (-0.999, 0.999),
        (0.0001, 5.0)
    ]

    result = minimize(
        objective_function,
        initial_guess,
        args=(
            F,
            strikes,
            T,
            market_vols
        ),
        method="L-BFGS-B",
        bounds=bounds
    )

    return result.x
