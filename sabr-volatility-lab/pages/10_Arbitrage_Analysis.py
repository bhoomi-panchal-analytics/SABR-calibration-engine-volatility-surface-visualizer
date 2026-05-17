import streamlit as st
import pandas as pd

from core.arbitrage import (
    butterfly_arbitrage,
    calendar_arbitrage
)

st.title("Arbitrage Diagnostics")

vols = [0.32, 0.28, 0.24, 0.21, 0.20, 0.22, 0.25]

butterfly = butterfly_arbitrage(vols)

calendar = calendar_arbitrage(
    0.30,
    0.25
)

if butterfly:
    st.error("Butterfly Arbitrage Detected")
else:
    st.success("No Butterfly Arbitrage")

if calendar:
    st.error("Calendar Arbitrage Detected")
else:
    st.success("No Calendar Arbitrage")
