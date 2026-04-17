from huggingfacehub.main import basic_question
import streamlit as st
import pandas as pd
import numpy as np

def basic_ui(args):
    st.set_page_config(page_title="HL.AI", page_icon=" ")
    st.header(' Welcome to HL, your dream assistant with Internet access.?')
    st.write("How can I assist you today?" )
    question = st.text_input("Enter your question:")
    if question:
        result = basic_question([question])
        st.write(result)

def main():
    basic_ui([])

if __name__ == "__main__":
    main()
