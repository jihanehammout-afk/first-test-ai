from huggingfacehub import main
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Accueil",
    page_icon="👋",
)

st.sidebar.success("Selectionnez une page pour vos besoins spécifiques.")

def basic_ui(args):
    question = st.text_input("Comment puis-je vous aider?")
    if question:
        result = main.basic_question(question)
        st.write(result)

with st.container(horizontal_alignment="center"):
    st.title(
        "Bienvenue sur HL, votre assistant de rêves avec un cœur d'or! 🌟",
        width="content",
        anchor=False,
    )       
    basic_ui([])
