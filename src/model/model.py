import pandas as pd
import regex as re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
FIN_CSV = DATA_DIR / "categorias_financeiras_organizado.csv"
MAXVAL_CSV = DATA_DIR / "maxvalue.csv"

#==========CARREGA E SALVA CSV===========
def carregar_categoriasdflt():
    return pd.read_csv(FIN_CSV)
def salvar_categoriasdflt(df):
    df.to_csv(FIN_CSV, index=False)

def carregar_maxval():
    return pd.read_csv(MAXVAL_CSV)
def salvar_maxval(df):
    df.to_csv(MAXVAL_CSV, index=False)
#=========================================


def only_posi(arquivo):
    arquivo['title'].dtype == 'object'
    arquivo['title'] = arquivo['title'].str.upper()
    arquivo = arquivo[arquivo['amount'] > 0]
    return arquivo

def pesquisar_categoria(df,categoria):
    cfo = carregar_categoriasdflt()
    if categoria not in cfo['CATEGORIA'].values:
        if categoria == 'TODOS':
            pd.DataFrame(df)
        else:
            return pd.DataFrame()
    
    regra = pd.concat([cfo[cfo['CATEGORIA'] == categoria],])
    
    regex = '|'.join(regra['TITULO'].dropna().astype(str).map(re.escape))
    
    resultado = df[df['title'].str.contains(regex, case=False, na=False)]

    return resultado

def adicionar_categoria_gastos(nome,titulo):
    cfo = carregar_categoriasdflt()
    nome_padrao = nome.upper().strip()
    titulo_padrao = titulo.upper().strip()

    if (titulo_padrao == cfo['TITULO']).any():
        return cfo
    
    nova_linha = {"CATEGORIA": nome_padrao,"TITULO": titulo_padrao}
    cfo = pd.concat([cfo, pd.DataFrame([nova_linha])], ignore_index=True)
    salvar_categoriasdflt(cfo)
    return cfo

def somarDf(arquivo):
    soma = arquivo['amount'].sum()
    return soma

def categorias_grafico(df,categoria):
    cfo = carregar_categoriasdflt()
    if categoria not in cfo['CATEGORIA'].values:
        if categoria == 'TODOS':
            pd.DataFrame(df)
        else:
            return pd.DataFrame()
    
    regra = pd.concat([cfo[cfo['CATEGORIA'] == categoria],])
    
    regex = '|'.join(regra['TITULO'].dropna().astype(str).map(re.escape))
    
    resultado = df[df['title'].str.contains(regex, case=False, na=False)]

    return resultado