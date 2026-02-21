# Credit Scoring com Regressão Logística 💳

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-4479A1?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Contato:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nayarasudariodiniz/)

# Credit Scoring com Regressão Logística 💳

Este repositório contém um projeto completo de **Credit Scoring**, focado em prever a probabilidade de inadimplência superior a 90 dias. O projeto abrange desde o saneamento de dados reais até a implementação de um modelo preditivo escalonado e balanceado, disponível via interface interativa.



## 🎯 Objetivo
Desenvolver um modelo estatístico capaz de classificar o risco de crédito de clientes, lidando com bases de dados desbalanceadas e variáveis de diferentes escalas, priorizando o **Recall** para mitigação de prejuízos financeiros.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Bibliotecas:** Pandas, NumPy, Scikit-Learn, Joblib
* **Visualização:** Matplotlib, Seaborn
* **Interface:** Streamlit
* **Ambiente:** Virtualenv (venv)

## 📈 Resultados do Modelo Final
Após o ajuste de hiperparâmetros e balanceamento de classes, o modelo atingiu:
* **Recall (Inadimplentes):** 0.76 (Capacidade de detectar 76% dos devedores reais).
* **AUC-ROC:** 0.85 (Excelente capacidade de discriminação entre classes).
* **Acurácia Global:** 0.80.

## 📁 Estrutura do Repositório
* `app.py`: Script do Streamlit para a interface de usuário.
* `modelo_credit_scoring.pkl`: Modelo treinado e serializado.
* `GiveMeSomeCredit.ipynb`: Jupyter com o passo a passo da análise e treinamento.
* `requirements.txt`: Lista de dependências do projeto.

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```
   git clone [https://github.com/nayarasudariodiniz/credit-scoring-logistic-regression.git](https://github.com/nayarasudariodiniz/credit-scoring-logistic-regression.git)
   cd credit-scoring-logistic-regression

2. **Crie e ative seu ambiente virtural:**
    ```
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
3. **Instale as dependências:**
    ```
    pip install -r requirements.txt
4. **Execute a aplicação Streamlit**:
    ```
    streamlit run app.py

___
<<<<<<< HEAD
Nota sobre os dados: Para rodar o treinamento no notebook, é necessário baixar os arquivos originais do Kaggle (cs-training.csv) e garantir a execução dos scripts de pré-processamento.
=======
Nota sobre os dados: Para rodar o treinamento no notebook, é necessário baixar os arquivos originais do Kaggle (cs-training.csv) e garantir a execução dos scripts de pré-processamento.
>>>>>>> 61211c0 (feat: add final model and streamlit app)
