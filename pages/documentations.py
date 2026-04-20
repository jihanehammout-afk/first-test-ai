

from huggingfacehub import main
import streamlit as st
import json


st.set_page_config(
    page_title="Documentations",
    page_icon="📚",
)

# Chargement
with open("pages.json") as f:
    st.session_state.pages = json.load(f)

st.sidebar.header("Documentations")



def edit_page(page: str):
    with open(st.session_state.pages[page], "r") as f:
        content = f.read()

    new_content = st.text_area("Contenu", value=content, key=f"editor_{page}", width=700)

    if st.button("Enregistrer", key=f"save_{page}"):
        with open(st.session_state.pages[page], "w") as f:
            f.write(new_content)
        st.success("Page mise à jour !")
        st.session_state.editing = False  # exit edit mode


def show_page(page: str):
    st.title(page)

    with open(st.session_state.pages[page], "r") as f:
        st.write(f.read())

    if st.button("Modifier", key=f"edit_{page}"):
        st.session_state.editing = True


# --- INIT STATE ---
if "current_page" not in st.session_state:
    st.session_state.current_page = next(iter(st.session_state.pages))

if "editing" not in st.session_state:
    st.session_state.editing = False


# --- MAIN DISPLAY ---
if st.session_state.editing:
    edit_page(st.session_state.current_page)
else:
    show_page(st.session_state.current_page)


# --- SIDEBAR NAV ---
with st.sidebar:
    for page in st.session_state.pages:
        if st.button(page):
            st.session_state.current_page = page
            st.session_state.editing = False  # reset edit mode
