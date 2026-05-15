import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Market Option Chain Analysis")

df = pd.read_csv("data/sample_option_chain.csv")

st.subheader("Sample Option Chain")

st.dataframe(df)

st.markdown("""
## Understanding the Data

### Strike Price
The predetermined price at which an option can be exercised.

### Implied Volatility
Represents market expectations of future volatility.

### Volatility Smile
Markets assign different implied volatilities to different strikes,
creating a smile-like structure.
""")

fig = px.line(
    df,
    x="strike",
    y="implied_vol",
    markers=True,
    title="Volatility Smile"
)

st.plotly_chart(fig, use_container_width=True)
