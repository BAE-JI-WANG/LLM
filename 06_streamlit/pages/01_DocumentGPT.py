import streamlit as st

st.title("DocumnetGPT")

st.markdown("""
Welcome!

Use this chatbot to ask questions to an AI about your files!
""")

file = st.file_uploader("Upload a .txt .pdf or .docx file", type=["pdf", "txt", "docx"])

