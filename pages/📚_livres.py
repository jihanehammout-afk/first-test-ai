from collections.abc import Callable
from typing import Any, Optional

from huggingfacehub import main
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="livres",
    page_icon="📚",
)

st.markdown("# Proposition de livres")
st.sidebar.header("Proposition de livres")

objectif_options = ["Découvrir de nouveaux genres", "Trouver des livres pour se détendre", "Trouver des livres pour apprendre quelque chose de nouveau"]    

def required(field_name: str) -> Callable[[Any], Optional[str]]:
    def inner(value: Any) -> Optional[str]:
        return None if value else f"{field_name} est requis."
    return inner

def basic_ui(args):
    with st.form("my_form"):
        style = st.text_input("Quel est votre style de lecture?")
        mood = st.text_input("Quel est votre humeur?")       
        age = st.text_input("Quel est votre âge?")
        goal = st.pills("Quel est votre objectif?", objectif_options)
        submitted = st.form_submit_button("Proposer des livres")

    if submitted:
        errors = [error for error in [required("Style")(style), required("Humeur")(mood), required("Âge")(age)] if error]
        if errors:
            for msg in errors:
                st.error(msg)
        else:
            st.write("En se basant sur vos préférences, voici un livre recommandé pour aujourd'hui:")
            result = main.basic_question(f"Quel est le livre recommandé pour aujourd'hui pour une personne de {age} ans avec un style de lecture {style}, une humeur {mood} et l'objectif de {goal}?")
            st.write(result)


with st.container(horizontal_alignment="center"):
    basic_ui([])

