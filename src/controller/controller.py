import src.model.model as md
import pandas as pd
#=============================================
#filtra apenas transacoes positivas do CSV
def filtrarPositivos(arquivo):
    if arquivo is not None:
        df = pd.read_csv(arquivo)
        dfpos = md.only_posi(df)
        return dfpos
#=============================================
def pesquisaCategoria(arquivo,categoria):
    resultado = md.pesquisar_categoria(arquivo, categoria)
    return resultado
#=============================================
def requestSomarDf(arquivo):
    soma = md.somarDf(arquivo)
    return soma
#=============================================
def adicionarCategoria(nome,titulo):
    addcat = md.adicionar_categoria_gastos(nome,titulo)
    return addcat
#=============================================
