import pandas as pd

df = pd.read_csv('data.csv')

print(df)

def filtros():
    print(f"="*100)
    print(f'\nGASTOS COM DELIVERY') 
    delivery = df[df['title'].str.startswith('Ifood') | df['title'].str.startswith('Ifd*') | df['title'].str.startswith('99food') ] #FILTRA AS PLATAFORMAS DE DELIVERY
    print(delivery)

    print(f'\nGASTOS COM CORRIDAS')
    corridas = df[df['title'].str.startswith('Uber') | df['title'].str.startswith('Dl*99 Ride')] #FILTRA AS PLATAFORMAS DE CORRIDAS POR APLICATIVO
    print(corridas)

    print(f'\nGASTOS COM VAREGISTAS')
    varegistas = df[df['title'].str.startswith('Kabum',) | df['title'].str.startswith('Mercadolivre') | df['title'].str.startswith('Amazonmktplc')] #FILTRA AS GRANDES VAREGISTAS
    print(varegistas)
    print(f"="*100) 

def soma_dos_filtrados():
    print(f"="*100) 
    delivery_sum = df[df['title'].str.startswith('Ifd*') | df['title'].str.startswith('99food') ]['amount'].sum() #SOMA PLAT DELIVERY
    print(f"O TOTAL GASTO EM DELIVERY {delivery_sum}")

    corridas_sum = df[df['title'].str.startswith('Uber') | df['title'].str.startswith('Dl*99 Ride')]['amount'].sum() #SOMA PLAT CORRIDAS
    print(corridas_sum)

    varegistas_sum = df[df['title'].str.startswith('Kabum',) | df['title'].str.startswith('Mercadolivre') | df['title'].str.startswith('Amazonmktplc')]['amount'].sum() #SOMA GRANDES VAREGISTAS
    print(varegistas_sum)
    print(f"="*100) 

def lista_filtros():
    print(f"="*100)
    print(f'\nTABELA DE FILTROS')
    filtro_geral = [varegistas,delivery,corridas] #MOSTRA TODOS OS GASTOS COM OS FILTROS ATIVOS
    print(filtro_geral)

    print(f'\nTABELA COM OS GASTOS GERAIS')
    lista_sem_filtro = df[~(df['title'].str.startswith('Dl*99') | df['title'].str.startswith('Pagamento recebido')| df['title'].str.startswith('Ifood') |df['title'].str.startswith('Ifd*') | df['title'].str.startswith('99food') | df['title'].str.startswith('Uber') | df['title'].str.startswith('Kabum',) | df['title'].str.startswith('Mercadolivre') | df['title'].str.startswith('Amazon'))]
    print(lista_sem_filtro) #'RETIRA' O FILTRO DA LISTA, DEIXANDO OS GASTOS GERAIS
    print(f"="*100)

def total():
    print(f"="*100) 
    print(f'\nTOTAL DE GASTOS')
    total = df[df['amount'] > 0]['amount'].sum() #SOMA O TOTAL RETIRANDO OS PAGAMENTOS
    print(f'R$ {total:.2f}')

    print(f'\nTOTAL DE GASTOS GERAIS')
    print(f'R$ {lista_sem_filtros['amount'].sum():.2f}') #SOMA OS GASTOS SEM OS FILTROS

    print(f'\nTOTAL DE GASTOS COM FILTROS')
    print(f'R$ {corridas_sum + delivery_sum + varegistas_sum:.2f}') #SOMA OS GASTIS COM OS FILTROS
    print(f"="*100)

filtros()
total()