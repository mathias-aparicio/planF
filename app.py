"""Power the streamit app with the business_plan and exit_strategy_to_pdf functions."""

from pathlib import Path
from time import sleep

import streamlit as st

from api import business_plan, exit_strategy_to_pdf

# Set up the Streamlit app
st.title("PlanF")
st.header("Bienvenue à l'IA PlanF")

# Create an expandable form for user input
with st.expander(label="IA - plan F", expanded=True), st.form(
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

    # Create PDF
    pdf = exit_strategy_to_pdf(plan)

    if Path("exit_strategy.pdf").exists():
        st.write("Vous pouvez télécharger le plan de fuite en PDF.")
    # Add a button to get PDF
    sleep(
        3,
    )  # TODO: remove this and find a proper way to wait for the complete creation of the pdf
    with Path.open("exit_strategy.pdf", "rb") as f:
        st.download_button("Download pdf", f, mime="application/pdf")

    # TODO: After download, re paste the business idea on the website
