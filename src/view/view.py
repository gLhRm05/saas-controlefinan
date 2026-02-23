import src.model.model as md
import streamlit as st
import pandas as pd
import src.controller.controller as ct
def main():
    st.title('FinanPy',text_alignment='center')
    st.markdown('Organize suas finanças de forma fácil',text_alignment='center')
    arquivo = ct.uploaderArq()
    if arquivo is not None:
        df = md.uploaded_file(arquivo)
        categoria = ct.inputPesquisa()
        md.pesquisar_categoria(df,categoria)