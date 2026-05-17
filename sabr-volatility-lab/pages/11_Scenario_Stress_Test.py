import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Stress Testing Engine")

market_shock = st.slider(
    "Market Shock (%)",
    -50,
    50,
    -10
)

vol_shock = st.slider(
    "Volatility Shock (%)",
    -50,
    100,
    25
)

prices = np.linspace(80, 120, 100)

stressed_prices = (
    prices
    * (1 + market_shock / 100)
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=prices,
        y=stressed_prices,
        mode='lines',
        name='Stress Scenario'
    )
)

fig.update_layout(
    template="plotly_dark",
    title="Market Stress Impact"
)

st.plotly_chart(fig, use_container_width=True)
