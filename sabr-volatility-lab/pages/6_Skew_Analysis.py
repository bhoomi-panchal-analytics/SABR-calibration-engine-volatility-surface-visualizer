import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Volatility Skew Analysis")

st.markdown("""
# Volatility Skew

Equity markets typically exhibit downside skew.

This means:
- OTM puts have higher implied volatility
- Investors pay more for downside protection
- Tail risk becomes expensive
""")

strike = np.linspace(80, 120, 100)

base_vol = 0.2

skew = st.slider(
    "Skew Strength",
    -0.02,
    0.02,
    -0.01
)

vol_curve = base_vol + skew * (strike - 100)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=strike,
        y=vol_curve,
        mode='lines',
        name='Skew Curve'
    )
)

fig.update_layout(
    template="plotly_dark",
    title="Volatility Skew Structure",
    xaxis_title="Strike",
    yaxis_title="Implied Volatility"
)

st.plotly_chart(fig, use_container_width=True)
