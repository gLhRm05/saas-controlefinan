import streamlit as st
import matplotlib.pyplot as mplb
import src.controller.controller as ct
def main():
    st.title('FinanPy',text_alignment='center')
    st.markdown('Organize suas finanças de forma fácil',text_alignment='center')
    arquivo = st.file_uploader("Insira um arquivo CSV", type=["csv"])
    dfpositivo = ct.filtrarPositivos(arquivo)
    st.divider()
    if arquivo is not None:
        st.markdown('**Escolha o gasto que procura**', text_alignment='center')
        categoria = st.text_input('Pesquise a sua categoria:').strip().upper()
        if categoria:
            resultado = ct.pesquisaCategoria(dfpositivo,categoria)
            st.dataframe(resultado)
            soma = ct.requestSomarDf(resultado)
            st.text(f'O seu gasto total com {categoria} é de R${soma:.2f}')
        st.divider()
        st.markdown('**Adicione mais categorias ao filtro geral**',text_alignment='center')
        with st.form("gasto_form"):
            nome = st.text_input("Categoria")
            titulo = st.text_input("Título do gasto")
            enviar = st.form_submit_button("Salvar")
        if enviar:
            showadd = ct.adicionarCategoria(nome,titulo)
            st.dataframe(showadd)
        st.divider()
    
#==============================