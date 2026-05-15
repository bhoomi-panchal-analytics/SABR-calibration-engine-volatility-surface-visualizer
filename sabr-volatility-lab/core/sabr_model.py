import numpy as np

def sabr_vol(F, K, T, alpha, beta, rho, nu):

    if F == K:
        return alpha / (F ** (1 - beta))

    z = (nu / alpha) * ((F * K) ** ((1 - beta) / 2)) * np.log(F / K)

    x_z = np.log(
        (np.sqrt(1 - 2 * rho * z + z**2) + z - rho)
        / (1 - rho)
    )

    numerator = alpha * (z / x_z)

    denominator = ((F * K) ** ((1 - beta) / 2))

    return numerator / denominator
