import pandas as pd
import streamlit as st
import src.view.view as v
import src.model.model as md

def uploaderArq():
    input_file = st.file_uploader('Faça o upload do arquivo CSV do seu banco:', type="csv")
    return input_file
    

def inputPesquisa():
    categoria = st.text_input('Digite a categoria desejada: ').strip().upper()
    return categoria

def inputCentroCustoAd():
    nome = st.text_input('Digite o nome do centro de custo desejado')
    titulo = st.text_input('Digite a palavra chave que identifica o titulo do gasto')
    return nome, titulo