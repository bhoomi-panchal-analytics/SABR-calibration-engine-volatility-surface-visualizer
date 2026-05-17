import numpy as np


def butterfly_arbitrage(vols):

    second_derivative = np.diff(vols, n=2)

    return np.any(second_derivative < 0)



def calendar_arbitrage(short_vol, long_vol):

    return long_vol < short_vol
