from logging import info

import pandas as pd
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from markdown_pdf import MarkdownPdf, Section

from prompts import main_prompt

MODEL = "gpt-4o-mini"
# Load video data
video_data = pd.read_csv("video.csv")


# Define the business_plan function
def business_plan(form: str) -> str:
    """Take a business idea and returns a business plan.

    Identify in the business idea concepts that are present in the database and return a
    business plan that highlights the formation available in the database.
    """
    # Initialize the language model with the OpenAI API key parsed from secrets.toml
    llm = ChatOpenAI(model=MODEL, api_key=st.secrets.OPENAI_API_KEY)

    # Define the prompt template
    prompt_template = PromptTemplate(
        input_variables=["form", "video_data"],
        template=main_prompt,
    )

    # Set output parser to return only the response
    output_parser = StrOutputParser()

    # Create the chain
    chain = prompt_template | llm | output_parser

    # Run the chain
    result = chain.invoke({"form": form, "video_data": video_data.to_dict()})

    # TODO: implement streaming
    return result


# Convert string to pdf
def exit_strategy_to_pdf(exit_strategy: str) -> MarkdownPdf | None:
    """Take the exit strategy and convert it to a pdf."""
    try:
        pdf = MarkdownPdf()
        pdf.add_section(Section(exit_strategy))
        pdf.save("exit_strategy.pdf")
        info("PDF successfully created")
        return pdf
        # TODO(): give the pdf a different name each time like exit_strategy + UUID/name
    except Exception as e:
        info(f"An error occurred while creating the PDF: {e}")
