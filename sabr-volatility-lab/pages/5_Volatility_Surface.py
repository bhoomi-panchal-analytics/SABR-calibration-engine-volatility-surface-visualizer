import streamlit as st
import numpy as np

from core.sabr_model import sabr_vol
from utils.plotting import surface_plot

st.title("3D Volatility Surface")

alpha = st.slider("Alpha", 0.1, 1.0, 0.3)
beta = st.slider("Beta", 0.0, 1.0, 0.5)
rho = st.slider("Rho", -1.0, 1.0, -0.2)
nu = st.slider("Nu", 0.1, 2.0, 0.5)

F = 100

strike_range = np.linspace(70, 130, 40)
expiry_range = np.linspace(0.1, 2.0, 40)

X, Y = np.meshgrid(
    strike_range,
    expiry_range
)

Z = np.zeros_like(X)

for i in range(len(expiry_range)):
    for j in range(len(strike_range)):

        Z[i, j] = sabr_vol(
            F,
            X[i, j],
            Y[i, j],
            alpha,
            beta,
            rho,
            nu
        )

fig = surface_plot(X, Y, Z)

st.plotly_chart(fig, use_container_width=True)
