import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .main {
            background-color: #0E1117;
        }

        h1, h2, h3 {
            color: #00FFAA;
        }

        .stMetric {
            background-color: #161A23;
            padding: 10px;
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
