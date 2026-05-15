import streamlit as st
import numpy as np

st.title("Options Risk Analysis")

st.markdown("""
# Greeks Analysis

Greeks measure sensitivity of option prices to market factors.

---

## Delta
Sensitivity to underlying price movement.

## Gamma
Sensitivity of delta.

## Vega
Sensitivity to volatility.

## Theta
Time decay of options.
""")

delta = st.slider("Delta", 0.0, 1.0, 0.5)
gamma = st.slider("Gamma", 0.0, 1.0, 0.1)
vega = st.slider("Vega", 0.0, 1.0, 0.3)
theta = st.slider("Theta", -1.0, 0.0, -0.1)

col1, col2 = st.columns(2)

col1.metric("Delta Exposure", delta)
col1.metric("Gamma Exposure", gamma)

col2.metric("Vega Exposure", vega)
col2.metric("Theta Decay", theta)

st.warning("""
High Vega exposure implies strong sensitivity to implied volatility changes.
""")
