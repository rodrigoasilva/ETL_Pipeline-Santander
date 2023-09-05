import pandas as pd
import numpy as np

Mugiwaras_list = ['Monkey D. Luffy', 'Roronoa Zoro','Vinsmoke Sanji','Nico Robin','Jinbe',
             'Franky', 'Brook', 'Nami', 'Usopp', 'Tony Tony Chopper'
             ]


########################    EXTRACT    ########################



df = pd.read_csv('OnePiece-Bounty - Sheet1.csv')

# Filtrar o DataFrame para incluir apenas os membros da tripulação dos Chapéus de Palha
filtered_df = df[df['Name'].isin(Mugiwaras_list)]

# Função para converter valores com símbolo de moeda e vírgula para números
def convert_bounty(value):
    try:
        return float(value.replace('฿', '').replace(',', ''))
    except ValueError:
        return np.nan


# Aplicar a função de conversão à coluna 'Bounty'
filtered_df['Bounty'] = filtered_df['Bounty'].apply(convert_bounty)



########################    TRANSFORM    ########################



# Calcular a média das recompensas
media_recompensas = filtered_df['Bounty'].mean()

# Calcular o desvio (valor atual - média) para cada membro da tripulação e criar um novo DataFrame
desvios_df = filtered_df.copy()
desvios_df['Desvio'] = desvios_df['Bounty'] - media_recompensas

# Adicionar coluna 'Média da Tripulação' com a média das recompensas da tripulação
desvios_df['Média da Tripulação'] = media_recompensas


########################    LOAD    ########################


# Reorganizar o DataFrame para ter as colunas na ordem desejada
desvios_df = desvios_df[['Name', 'Desvio', 'Bounty', 'Média da Tripulação']]

# Exibir o novo DataFrame com os desvios
print(desvios_df)