import pandas as pd
import src.view.view as v
import streamlit as st
import src.controller.controller as ct
import regex as re
cfo = pd.read_csv('E:\PROJPY FINAN\saas-controlefinan\data\categorias_financeiras_organizado.csv')
cfu = pd.read_csv('E:\PROJPY FINAN\saas-controlefinan\data\categorias_financeiras_user.csv')
mvx = pd.read_csv('E:\PROJPY FINAN\saas-controlefinan\data\maxvalue.csv')

def uploaded_file(arquivo):
    arquivo = pd.read_csv(arquivo)
    arquivo['title'].dtype == 'object'
    arquivo['title'] = arquivo['title'].str.upper()
    arquivo = arquivo[arquivo['amount'] > 0]
    st.dataframe(arquivo)
    st.text(f'Valor total gasto: R$ {arquivo['amount'].sum():.2f}')
    return arquivo

def pesquisar_categoria(df,categoria):
    regra = cfo[cfo['CATEGORIA'] == categoria]
    regra_usr = cfu[cfu['CATEGORIA'] == categoria]
    if regra.empty and regra_usr.empty:
        st.text('CATEGORIA NAO ENCONTRADA')
        return
    regex = '|'.join(regra['TITULO'].dropna().astype(str).map(re.escape))
    regex_usr = '|'.join(regra_usr['TITULO'].dropna().astype(str).map(re.escape))
    if regra_usr.empty:
        resultado = df[df['title'].str.contains(regex,case=False,na=False)]
    if regra.empty:
        resultado = df[df['title'].str.contains(regex_usr,case=False,na=False)]
    if resultado.empty:
        st.text('Digite uma categoria válida')
        return
    st.dataframe(resultado)
    soma = resultado['amount'].sum()
    st.text(f'Total gasto em {categoria}: R$ {soma}')