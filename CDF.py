import streamlit as st
from scipy.stats import norm

st.set_page_config(page_title="Distribuição Normal", layout="centered")
st.title("📊 Distribuição Normal Contínua")

# Entradas do usuário
media = st.number_input("Média (μ)", value=0.0)
desvio_padrao = st.number_input("Desvio padrão (σ)", value=1.0, min_value=0.0001)

# Seleção do tipo de cálculo
tipo_calculo = st.radio(
    "Selecione o tipo de cálculo:",
    ("Valor único (P(X ≤ x))", "Intervalo (P(n1 ≤ X ≤ n2))")
)

if tipo_calculo == "Valor único (P(X ≤ x))":
    valor_x = st.number_input("Valor desejado (x)", value=0.0)
    prob = norm.cdf(valor_x, loc=media, scale=desvio_padrao)
    porcentagem = prob * 100
    
    st.write("---")
    st.subheader("📌 Resultado:")
    st.write(f"Probabilidade de P(X ≤ {valor_x}) com média {media} e desvio padrão {desvio_padrao} é:")
    st.metric(label="Valor acumulado (em %)", value=f"{porcentagem:.2f}%")
    
    with st.expander("🔍 O que isso significa?"):
        st.markdown(f"""
        - Isso representa a área sob a curva da distribuição normal à esquerda de **{valor_x}**.
        - A porcentagem corresponde à chance de um valor ser **menor ou igual a {valor_x}**.
        """)

else:  # Intervalo
    col1, col2 = st.columns(2)
    with col1:
        n1 = st.number_input("Limite inferior (n1)", value=-1.0)
    with col2:
        n2 = st.number_input("Limite superior (n2)", value=1.0)
    
    if n2 < n1:
        st.error("O limite superior deve ser maior que o limite inferior!")
    else:
        prob_n1 = norm.cdf(n1, loc=media, scale=desvio_padrao)
        prob_n2 = norm.cdf(n2, loc=media, scale=desvio_padrao)
        prob_intervalo = prob_n2 - prob_n1
        porcentagem_intervalo = prob_intervalo * 100
        
        st.write("---")
        st.subheader("📌 Resultado:")
        st.write(f"Probabilidade de P({n1} ≤ X ≤ {n2}) com média {media} e desvio padrão {desvio_padrao} é:")
        st.metric(label="Probabilidade do intervalo (em %)", value=f"{porcentagem_intervalo:.2f}%")
        
        with st.expander("🔍 O que isso significa?"):
            st.markdown(f"""
            - Isso representa a área sob a curva da distribuição normal entre **{n1}** e **{n2}**.
            - A porcentagem corresponde à chance de um valor estar **entre {n1} e {n2}**.
            """)