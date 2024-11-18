"""Power the streamit app with the business_plan and exit_strategy_to_pdf functions."""

from pathlib import Path

import streamlit as st

from api import business_plan

# Set up the Streamlit app
st.title("PlanF")
st.header("Bienvenue à l'IA PlanF")

# Create an expandable form for user input
with st.expander("Racontez nous votre idée de Business", expanded=True), st.form(
    key="business_idea_form",
):
    business_idea = st.text_area(
        "Racontez nous votre idée de Business:",
        height=300,
    )
    submit_button = st.form_submit_button(label="Envoyer")

# Display the inputted business idea after submission
if submit_button:
    plan = business_plan(business_idea)
    st.write(plan)

    # Add a button to get PDF
    with Path.open("exit_strategy.pdf", "rb") as f:
        st.download_button("Download pdf", f, mime="application/pdf")
