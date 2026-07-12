# Importa as bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

# Função para avaliar o modelo de classificação
# Gera o relatório de métricas de classificação
# E plota a Matriz de Confusão visual.
def avaliar_modelo(y_true, y_pred, titulo='Avaliação do Modelo', labels=None):

    print(f'\n{'='*42}')
    print(f'Relatório de Métricas: {titulo}')
    print(f'{'='*42}')
    print(classification_report(y_true, y_pred))
    
    # Gera a matriz de confusão
    cm = confusion_matrix(y_true, y_pred)
    
    # Configuração visual da matriz
    plt.figure(figsize=(6, 4))

    if labels is None:
        labels = y_pred.unique()  # Usa as classes previstas como rótulos se não forem fornecidos

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=labels,
                yticklabels=labels)
    plt.ylabel('Classe Real', fontweight='bold')
    plt.xlabel('Classe Prevista', fontweight='bold')
    plt.title(f'Matriz de Confusão: {titulo}', fontsize=12)
    plt.tight_layout()
    plt.show()