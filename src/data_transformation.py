# Importa as bibliotecas necessárias
import os
import pandas as pd
import joblib as jl
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Função para aplicar padronização nos dados
def aplicar_padronizacao(x_train, x_test, caminho_salvar_scaler):
    # Aplica o StandardScaler nos dados, garantindo que não haja Data Leakage.
    # Salva o transformador em formato .pkl para uso em produção.
    
    # Inicializa o padronizador
    scaler = StandardScaler()
    
    # O modelo aprende a média/variância e transforma o Treino
    x_train_scaled = scaler.fit_transform(x_train)
    
    # O modelo aplica as regras aprendidas no Teste
    x_test_scaled = scaler.transform(x_test)
    
    # Converte as matrizes do numpy de volta para DataFrame do pandas
    x_train_scaled = pd.DataFrame(x_train_scaled, columns=x_train.columns)
    x_test_scaled = pd.DataFrame(x_test_scaled, columns=x_test.columns)
    
    # Garante que a pasta de destino existe e salva o scaler
    os.makedirs(os.path.dirname(caminho_salvar_scaler), exist_ok=True)
    jl.dump(scaler, caminho_salvar_scaler)
    
    return x_train_scaled, x_test_scaled

# Função para separar o DataFrame em variáveis preditoras (x) e variável alvo (y),
# e dividir os dados em treino e teste
def dividir_dados_treino_teste(df, colunas_para_excluir=None, col_alvo='target', test_size=0.20, random_state=42):
   
    if colunas_para_excluir is None:
        colunas_para_excluir = []
        
    # Separa variáveis preditoras (x) da variável alvo (y)
    x = df.drop(colunas_para_excluir, axis=1, errors='ignore')
    y = df[col_alvo]
    
    # Separação estratificada (mantém a proporção das classes do target)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, 
        test_size=test_size, 
        random_state=random_state, 
        stratify=y
    )
    
    return x_train, x_test, y_train, y_test

