import streamlit as st
import pandas as pd
import joblib

# 1. Carregar o modelo
modelo = joblib.load('modelo_credit_scoring.pkl')

st.title("Sistema de Análise de Risco de Crédito")

# 2. Entradas do Usuário
idade = st.number_input("Idade", 18, 100, 30)
utilizacao = st.slider("Utilização de Limite (0 a 1)", 0.0, 1.0, 0.5)
atraso_30_59 = st.number_input("Vezes que atrasou 30-59 dias", 0, 10, 0)
razao_debito = st.number_input("Razão de Débito", 0.0, 1.0, 0.1)
renda = st.number_input("Renda Mensal", 0.0, 50000.0, 5000.0)
# Ajustado para o nome que o erro apontou:
linhas_abertas = st.number_input("Qtd de Linhas de Crédito e Empréstimos Abertos", 0, 50, 5)
atraso_90 = st.number_input("Vezes que atrasou 90+ dias", 0, 10, 0)
imobiliarios = st.number_input("Empréstimos Imobiliários", 0, 10, 0)
atraso_60_89 = st.number_input("Vezes que atrasou 60-89 dias", 0, 10, 0)
dependentes = st.number_input("Número de Dependentes", 0, 10, 0)

if st.button("Analisar Risco"):
    # Lógica de faixas (conforme Aula 5.4)
    faixa_adulto = 1 if 25 < idade <= 45 else 0
    faixa_senior = 1 if 45 < idade <= 65 else 0
    faixa_idoso = 1 if idade > 65 else 0

    # 3. Dicionário com nomes EXATOS conforme o erro do Scikit-Learn
    dados_entrada = {
        'Utilizacao_Limite': utilizacao,
        'Idade': idade,
        'Atrasos_30_59_Dias': atraso_30_59,
        'Razao_Debito': razao_debito,
        'Renda_Mensal': renda,
        'Linhas_Credito_Emprestimos_Abertos': linhas_abertas, # Nome corrigido aqui
        'Atrasos_90_Dias_Ou_Mais': atraso_90,
        'Emprestimos_Imobiliarios': imobiliarios,
        'Atrasos_60_89_Dias': atraso_60_89,
        'Numero_Dependentes': dependentes,
        'Faixa_Idade_Adulto': faixa_adulto,
        'Faixa_Idade_Senior': faixa_senior,
        'Faixa_Idade_Idoso': faixa_idoso
    }
    
    df_usuario = pd.DataFrame([dados_entrada])
    
    # 4. Predição
    prob = modelo.predict_proba(df_usuario)[0][1]
    
    if prob > 0.5:
        st.error(f"Risco de Inadimplência Elevado: {prob:.2%}")
    else:
        st.success(f"Crédito Pré-Aprovado! Probabilidade de risco: {prob:.2%}")