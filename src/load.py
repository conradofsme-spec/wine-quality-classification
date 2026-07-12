# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np

# Função para carregar o dataset, com a criação da coluna 'target' a partir da coluna col_alvo
def carregar_dataset(path_data, col_alvo):
    
    # Carregar o dataset
    df = pd.read_csv(path_data)

    # Criar a nova coluna 'target' com base na coluna col_alvo
    # Alta qualidade (nota >= 7) será rotulada como 1
    # Baixa ou média qualidade (nota < 7) será rotulada como 0
    df['target'] = np.where(df[col_alvo] >= 7, 1, 0)

    return df

