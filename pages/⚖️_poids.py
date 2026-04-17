from collections.abc import Callable
from typing import Any, Optional

from huggingfacehub import main
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="poids",
    page_icon="⚖️",
)

st.markdown("# Gestion du poids")
st.sidebar.header("Gestion du poids")

def required(field_name: str) -> Callable[[Any], Optional[str]]:
    def inner(value: Any) -> Optional[str]:
        return None if value else f"{field_name} est requis."
    return inner

def basic_ui(args):
    with st.form("my_form"):
        weight = st.text_input("Quel est votre poids?")
        height = st.text_input("Quelle est votre taille?")
        age = st.text_input("Quel est votre âge?")
        goal = st.selectbox("Quel est votre objectif?", ["Maintien du poids", "Perte de poids", "Prise de poids"])
        submitted = st.form_submit_button("Calculer BMR")

    if submitted:
        errors = [error for error in [required("Poids")(weight), required("Taille")(height), required("Âge")(age)] if error]
        if errors:
            for msg in errors:
                st.error(msg)
        else:
            bmr = (9.99 * float(weight)) + (6.25 * float(height)) - (4.92 * float(age)) - 161
            st.write(f"Ton metabolisme de base (BMR) est approximativement: {bmr} calories/jour")
            st.write("En se basant sur votre BMR, voici un programme recommandé pour aujourd'hui:")
            result = main.basic_question(f"Quel est le programme recommandé pour aujourd'hui pour une personne de métabolisme de base {bmr} calories/jour avec l'objectif de {goal}?")
            st.write(result)


with st.container(horizontal_alignment="center"):
    basic_ui([])

