# Importa as bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Gera histogramas com curva de densidade para cada variável numérica do DataFrame
# Permite excluir colunas específicas, como as variáveis alvo
def plot_distribuicoes(df, colunas_para_excluir=None):
    
    sns.set_theme(style="whitegrid")

    if colunas_para_excluir is None:
        colunas_para_excluir = [] # Se nenhuma coluna for especificada, cria uma lista vazia
    
    # Remove as colunas indicadas e mantém apenas as que sobraram
    features = df.drop(colunas_para_excluir, axis=1, errors='ignore').columns

    # Define o número de linhas necessárias
    n_colunas = 3
    n_linhas = math.ceil(len(features) / n_colunas)

    # Cria o quadro em branco com base na quantidade de linhas e colunas
    fig, axes = plt.subplots(n_linhas, n_colunas, figsize=(16, 4 * n_linhas))

    # Achata a matriz de eixos para facilitar a iteração
    axes = axes.flatten()

    # Plota o histograma e a curva de densidade para cada variável
    for i, col in enumerate(features):
        sns.histplot(df[col], kde=True, ax=axes[i], color='teal', bins=30)
        axes[i].set_title(f'Distribuição de {col}', fontsize=12)
        axes[i].set_xlabel('')
        axes[i].set_ylabel('Frequência')
    
    # Remove os quadrados vazios que sobrarem no final
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    # Exibe o gráfico
    plt.tight_layout()
    plt.show()

# Gera um Heatmap referente à correlação das variáveis com o alvo
def plot_correlacao_alvo(df, col_alvo, colunas_para_excluir=None, titulo=None):

    sns.set_theme(style="whitegrid")

    if colunas_para_excluir is None:
        colunas_para_excluir = [] # Se nenhuma coluna for especificada, cria uma lista vazia
    
    # Calcula a correlação, ignorando a coluna excluída
    corr = df.drop(colunas_para_excluir, axis=1, errors='ignore').corr()
    corr_alvo = corr[[col_alvo]].sort_values(by=col_alvo, ascending=False)
    
    #Remove a correlação da variável alvo com ela mesma
    corr_alvo = corr_alvo.drop(index=col_alvo, errors='ignore')

    # Configurações do gráfico
    plt.figure(figsize=(8, 10))
    sns.heatmap(corr_alvo, annot=True, fmt=".2f", cmap="coolwarm", center=0, vmin=-1, vmax=1)
    plt.title(titulo, fontsize=16)
    plt.tight_layout()
    
    # Exibe o gráfico
    plt.show()

# Gera um gráfico de barras mostrando a contagem e o percentual de cada classe na variável alvo.
def plot_balanceamento_classes(df, col_alvo, rotulo_x=None):
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 6))

    # Cria o gráfico de contagem baseado na coluna dinâmica
    ax = sns.countplot(x=col_alvo, hue=col_alvo, data=df, palette="Set2", legend=False)

    # Título dinâmico que recebe o nome da coluna
    plt.title(f"Distribuição das Classes ({col_alvo})", fontsize=14)

    # Rótulo X dinâmico que recebe o nome da coluna
    if rotulo_x is None:
        plt.xlabel(col_alvo.capitalize(), fontsize=12)
    else:
        plt.xlabel(rotulo_x, fontsize=12)
    
    # Adiciona os percentuais e quantidades acima de cada barra
    total = len(df)
    for p in ax.patches:
        altura = p.get_height()
        if altura > 0: # Evita barras vazias
            percentual = (altura / total) * 100
            ax.text(p.get_x() + p.get_width() / 2.,
                    altura + (total * 0.01),
                    f'{int(altura)} ({percentual:.1f}%)',
                    ha="center", fontsize=12, fontweight='bold')
    
    # Exibe o gráfico
    plt.tight_layout()
    plt.show()