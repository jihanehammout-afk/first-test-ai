from huggingfacehub import main
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Greeting",
    page_icon="👋",
)

st.sidebar.success("Select a page for your specific needs.")

def basic_ui(args):
    question = st.text_input("How can I assist you today?")
    if question:
        result = main.basic_question(question)
        st.write(result)

with st.container(horizontal_alignment="center"):
    st.title(
        'Welcome to HL, your dream assistant with a heart of gold! 🌟',
        width="content",
        anchor=False,
    )       
    basic_ui([])
