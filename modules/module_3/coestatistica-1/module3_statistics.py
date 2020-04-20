# Load libraries
import json
import pandas as pd

df = pd.read_csv('desafio1.csv')

df_stats = df.groupby('estado_residencia')['pontuacao_credito'].\
    agg({pd.Series.mode, 'median', 'mean', 'std'})

df_stats.rename(columns={'mode': 'moda', 'median': 'mediana',
                         'mean': 'media', 'std': 'desvio_padrao'}, 
                inplace=True)

# df_stats.sort_values(by='estado_residencia', ascending=False, inplace=True)

# orientar o JSON pelo indíce para ficar no formato correto de sub
df_stats.to_json('submission.json', orient='index') 