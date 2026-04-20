from huggingfacehub import main
import streamlit as st
import pandas as pd
import numpy as np
import json



st.set_page_config(
    page_title="Accueil",
    page_icon="👋",
)

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





    