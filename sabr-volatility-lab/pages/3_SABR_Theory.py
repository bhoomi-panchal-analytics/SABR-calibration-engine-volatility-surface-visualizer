import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("SABR Model Theory")

st.markdown("""
# What is the SABR Model?

The SABR (Stochastic Alpha Beta Rho) model is a stochastic volatility model
used for modeling implied volatility smiles in derivatives markets.

---

# Core Equation

The SABR model dynamics are:

""")

st.latex(r"""
dF_t = \alpha_t F_t^\beta dW_t
""")

st.latex(r"""
d\alpha_t = \nu \alpha_t dZ_t
""")

st.latex(r"""
corr(dW_t, dZ_t) = \rho
""")

st.markdown("""
---

# Parameter Interpretation

### Alpha (α)
Controls the overall volatility level.

### Beta (β)
Controls elasticity of variance.

- β = 1 → Lognormal model
- β = 0 → Normal model

### Rho (ρ)
Correlation between spot and volatility.

### Nu (ν)
Volatility of volatility.

Higher ν creates steeper smiles.

---

# Why SABR Matters

Traditional Black-Scholes assumes constant volatility.

Real markets exhibit:
- Volatility smile
- Volatility skew
- Fat tails
- Dynamic uncertainty

SABR captures these market realities.
""")

beta = st.slider("Beta", 0.0, 1.0, 0.5)

x = np.linspace(80, 120, 100)

y = (x / 100) ** beta

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='Elasticity Curve'
    )
)

fig.update_layout(
    template="plotly_dark",
    title="Effect of Beta on Elasticity"
)

st.plotly_chart(fig, use_container_width=True)
