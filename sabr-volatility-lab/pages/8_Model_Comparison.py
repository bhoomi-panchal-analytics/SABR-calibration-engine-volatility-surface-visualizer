import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Black-Scholes vs SABR")

st.markdown("""
# Why Black-Scholes Fails

Black-Scholes assumes:

- Constant volatility
- Lognormal returns
- No smile dynamics

Real markets violate these assumptions.

SABR introduces stochastic volatility dynamics.
""")

strike = np.linspace(80, 120, 100)

bs_vol = np.ones_like(strike) * 0.2

sabr_vol = (
    0.2
    + 0.0005 * (strike - 100) ** 2
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=strike,
        y=bs_vol,
        mode='lines',
        name='Black-Scholes'
    )
)

fig.add_trace(
    go.Scatter(
        x=strike,
        y=sabr_vol,
        mode='lines',
        name='SABR Smile'
    )
)

fig.update_layout(
    template="plotly_dark",
    title="Model Comparison",
    xaxis_title="Strike",
    yaxis_title="Implied Volatility"
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
SABR captures smile structures that Black-Scholes cannot model effectively.
""")
