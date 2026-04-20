from collections.abc import Callable
import os
from typing import Any, Optional

from huggingfacehub import main
import streamlit as st
import numpy as np
import json

st.set_page_config(
    page_title="Création de pages dynamiques",
    page_icon="🛠️",
)


st.markdown("# Création de pages dynamiques")
st.sidebar.header("Création de pages dynamiques")



if "pages" not in st.session_state:
    st.session_state.pages = {}




    
new_page_name = st.text_input("Nom de la page")
new_page_content = st.text_area("Contenu", value="Contenu de la nouvelle page", height=200, width=700)


if st.button("Créer"):
    if new_page_name:
        st.session_state.pages[new_page_name] = f"pages/documentations/{new_page_name}.txt"
        with open(f"pages/documentations/{new_page_name}.txt", "w") as f:
            f.write(new_page_content)
        # Sauvegarde
        with open("pages.json", "w") as f:
            json.dump(st.session_state.pages, f)


  
