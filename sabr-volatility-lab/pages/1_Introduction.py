import streamlit as st

st.set_page_config(layout="wide")

st.title("SABR Volatility Surface Research Lab")

st.markdown("""
## Overview

This platform is designed to study and calibrate the SABR (Stochastic Alpha Beta Rho) volatility model
used extensively in quantitative finance and derivatives trading.

The project demonstrates:

- Volatility smile analysis
- Implied volatility surface construction
- SABR parameter calibration
- Market skew dynamics
- Risk visualization
- Derivatives analytics

---

## Why This Matters

Traditional Black-Scholes assumes constant volatility.

Real markets do NOT behave like this.

Option markets exhibit:

- Volatility smiles
- Volatility skews
- Fat tails
- Dynamic risk regimes

The SABR model addresses these issues using stochastic volatility dynamics.

---

## Core Objectives

### 1. Calibrate SABR Model
Estimate:
- Alpha
- Beta
- Rho
- Nu

from market implied volatility data.

### 2. Build Volatility Surface
Generate:
- Strike vs Volatility
- Expiry vs Volatility
- 3D volatility surfaces

### 3. Analyze Risk Dynamics
Study:
- Smile curvature
- Skew steepness
- Sensitivity shifts
- Volatility clustering

---

## Applications

This framework is relevant for:

- Volatility Trading
- Exotic Derivatives Pricing
- Risk Management
- Quantitative Research
- Market Making
- Options Structuring

---

## Institutional Relevance

SABR is widely used across:

- Investment Banks
- Hedge Funds
- Structured Products Desks
- Commodities Trading
- FX Derivatives

---

## Technical Stack

- Python
- Streamlit
- NumPy
- SciPy
- Plotly
- Quantitative Finance Models

""")
