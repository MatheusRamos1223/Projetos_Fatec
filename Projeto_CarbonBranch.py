import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import streamlit as st

st.set_page_config(page_title="Previsão CO₂", layout="centered")

# 🎨 Cores do tema
CORES = {
    "roxo": "#6A0DAD",
    "verde": "#2E8B57",
    "roxo_claro": "#9F7FDF",
    "cinza": "#808080"
}

# 📥 Entrada
st.sidebar.header("Entrada de Dados")
num_dias = st.sidebar.slider("Número de dias", 3, 30, 9)

emissoes = []
for i in range(1, num_dias + 1):
    emissoes.append(st.sidebar.number_input(
        f"Dia {i}",
        min_value=0.0,
        value=float(35 + np.random.randint(-5, 10))
    ))

dias = np.arange(1, num_dias + 1)
emissoes = np.array(emissoes)

# 🔍 Interpolação e previsões
spline = CubicSpline(dias, emissoes, bc_type='natural')
velocidade = spline.derivative(1)
aceleracao = spline.derivative(2)

dias_futuros = np.arange(dias[-1] + 1, dias[-1] + 8)
incl_final = velocidade(dias[-1])
emissao_final = spline(dias[-1])
previsao = [emissao_final + incl_final * (i - dias[-1]) for i in dias_futuros]

# 📊 Gráfico
fig, ax = plt.subplots(figsize=(10, 5))
x_interp = np.linspace(dias[0], dias[-1], 300)

ax.plot(dias, emissoes, 'o', label="Dados reais", color=CORES["roxo"])
ax.plot(x_interp, spline(x_interp), '-', label="Spline cúbica", color=CORES["roxo"])
ax.plot(dias_futuros, previsao, 'x--', label="Previsão (7 dias)", color=CORES["roxo_claro"])
ax.plot(x_interp, velocidade(x_interp), '--', label="Velocidade", color=CORES["verde"])
ax.plot(x_interp, aceleracao(x_interp), ':', label="Aceleração", color=CORES["cinza"])
ax.axvline(x=dias[-1], color='gray', linestyle='--', alpha=0.5)

ax.set_title("Análise de Emissões de CO₂", fontweight='bold')
ax.set_xlabel("Dia")
ax.set_ylabel("kg de CO₂/dia")
ax.grid(True, linestyle='--', alpha=0.3)
ax.legend()

st.pyplot(fig)

# 📢 Resultados
st.subheader("Resultados Numéricos")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"**Última medição:** {emissoes[-1]:.1f} kg")
    st.markdown(f"**Velocidade atual:** {velocidade(dias[-1]):.1f} kg/dia")
with col2:
    st.markdown(f"**Aceleração atual:** {aceleracao(dias[-1]):.1f} kg/dia²")

st.markdown("**Previsão para os próximos 7 dias:**")
for dia, valor in zip(dias_futuros, previsao):
    tendencia = '↑' if valor > emissoes[-1] else '↓'
    st.markdown(f"Dia {dia}: {valor:.1f} kg {tendencia}")
