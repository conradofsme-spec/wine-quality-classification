# Tech Challenge: Classificação da Qualidade de Vinhos

Este projeto foi desenvolvido para prever a qualidade de vinhos com base em suas propriedades físico-químicas. O objetivo principal é construir um modelo de **Machine Learning** capaz de identificar vinhos de **Alta Qualidade**, lidando com os desafios reais de dados desbalanceados.

## 1. Contexto e Objetivos

No mercado vitivinícola, classificar vinhos de excelência é um processo caro e subjetivo, dependente de especialistas. Este projeto visa automatizar uma triagem inicial por meio da análise química de atributos como acidez, teor de álcool, pH e açúcar residual, utilizando um modelo de Machine Learning. Como vinhos excelentes podem ser raros, o desafio principal do projeto foi evitar que o modelo de Machine Learning selecionado ignorasse tal classe, por ser minoritária.

## 2. Estrutura do Repositório

O repositório do projeto foi organizado da seguinte forma:
* `data/`: Contém o dataset original (`WineQT.csv`).
* Em `notebooks/`, foi adotada a seguinte estrutura:
  * `01_eda.ipynb`: Análise exploratória dos dados.
  * `02_pre_processing.ipynb`: Feature Engineering, estratificação e padronização dos dados.
  * `03_modeling.ipynb`: Desenvolvimento e avaliação de dois modelos de Machine Learning - Regressão Logística e Random Forest.
* `src/`: Contém os scripts modulares em Python - `load.py`, `plots.py`, `data_transformation.py` e `metrics.py`.
* `results/`: Contém o objeto `scaler_vinho.pkl`.
* `requirements.txt`: Relação de dependências e bibliotecas necessárias.

## 3. Tecnologias e Configuração

O projeto foi desenvolvido utilizando um ambiente virtual isolado para garantir a estabilidade das versões:
* Linguagem: Python 3.13.13
* Bibliotecas principais: Scikit-Learn, Matplotlib e Seaborn.
* IDE: VS Code.

## 4. Autor
* **Conrado Filippo Silva** - Grupo 194
* Pós-graduação em Data Analytics - FIAP - 2026

