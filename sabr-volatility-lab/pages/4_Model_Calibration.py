import streamlit as st
import pandas as pd
import numpy as np

from core.calibration import calibrate_sabr
from core.sabr_model import sabr_vol
from utils.plotting import calibration_chart

st.title("SABR Calibration Engine")

df = pd.read_csv("data/sample_option_chain.csv")

st.markdown("""
# Objective

The calibration engine minimizes the error between:

- Market implied volatility
- SABR model implied volatility

using nonlinear optimization.
""")

F = st.number_input("Forward Price", value=100.0)
T = st.slider("Expiry (Years)", 0.1, 5.0, 1.0)

K = df["strike"].values
market_vols = df["implied_vol"].values

if st.button("Run Calibration"):

    alpha, beta, rho, nu = calibrate_sabr(
        F,
        K,
        T,
        market_vols
    )

    st.success("Calibration Complete")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Alpha", round(alpha, 4))
    col2.metric("Beta", round(beta, 4))
    col3.metric("Rho", round(rho, 4))
    col4.metric("Nu", round(nu, 4))

    model_vols = np.array([
        sabr_vol(F, k, T, alpha, beta, rho, nu)
        for k in K
    ])

    fig = calibration_chart(
        K,
        market_vols,
        model_vols
    )

    st.plotly_chart(fig, use_container_width=True)
