from huggingfacehub import main
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Weight",
    page_icon="⚖️",
)

st.markdown("# Weight Management")
st.sidebar.header("Weight Management")

def basic_ui(args):
    weight = st.text_input("What is your weight?")
    height = st.text_input("What is your height?")
    age = st.text_input("What is your age?")
    if st.button("Calculate BMR"):
        bmr = (9.99 * float(weight)) + (6.25 * float(height)) - (4.92 * float(age)) - 161
        st.write(f"Your Basal Metabolic Rate (BMR) is: {bmr} calories/day")
        result = main.basic_question(f"What is the ideal weight for a person with weight {weight}, height {height}, and age {age}? and what is the recommded program for today?")
        st.write(result)

with st.container(horizontal_alignment="center"):
    basic_ui([])

