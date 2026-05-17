import streamlit as st
import plotly.graph_objects as go

from core.monte_carlo import monte_carlo_paths

st.title("Monte Carlo Simulation")

S0 = st.number_input("Initial Price", value=100.0)
mu = st.slider("Expected Return", -0.2, 0.2, 0.05)
sigma = st.slider("Volatility", 0.01, 1.0, 0.2)

paths = monte_carlo_paths(
    S0,
    mu,
    sigma,
    1,
    252,
    100
)

fig = go.Figure()

for i in range(20):

    fig.add_trace(
        go.Scatter(
            y=paths[:, i],
            mode='lines',
            showlegend=False
        )
    )

fig.update_layout(
    template="plotly_dark",
    title="Monte Carlo Price Paths"
)

st.plotly_chart(fig, use_container_width=True)
