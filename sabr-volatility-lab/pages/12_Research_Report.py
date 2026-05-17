import streamlit as st

from utils.report_generator import create_report

st.title("Research Report Generator")

if st.button("Generate PDF Report"):

    create_report(
        "reports/sabr_report.pdf"
    )

    with open(
        "reports/sabr_report.pdf",
        "rb"
    ) as file:

        st.download_button(
            label="Download Report",
            data=file,
            file_name="sabr_report.pdf",
            mime="application/pdf"
        )
