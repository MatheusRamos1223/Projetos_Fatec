# Projetos_Fatec
Esses projetos fazem parte de uma coletânea de atividades da FATEC Americana das disciplinas Engenharia de Sotware, Calculo 1 e Estatistca 

# CDF 
A Função de Distribuição Acumulada (CDF - Cumulative Distribution Function) calcula a probabilidade de uma variável aleatória 𝑋
ser menor ou igual a um valor 𝑥 específico: 
𝐹(𝑥) = 𝑃(𝑋 ≤ x). Ela é uma função não decrescente que varia de 0 a 1, essencial na estatística para definir distribuições de probabilidade acumuladas.
 

# Análise e Previsão de Emissões de CO₂

Este projeto utiliza conceitos de cálculo diferencial para analisar dados históricos de emissão e projetar tendências futuras de forma automatizada.

## Metodologia Matemática

A aplicação de derivadas neste sistema ocorre em quatro etapas fundamentais para garantir precisão e suavidade na análise:

### 1. Interpolação por Spline Cúbica
Para transformar dados discretos (pontos isolados) em uma curva contínua, utilizamos o método `CubicSpline`.
* **Papel da Derivada:** O algoritmo garante que a **primeira e a segunda derivadas** sejam contínuas em todos os pontos de conexão. Isso evita mudanças bruscas ("quinas") no gráfico, simulando um fenômeno físico real e fluido.

### 2. Primeira Derivada ($f'(x)$): Velocidade
A primeira derivada é extraída da função spline para representar a **taxa de variação instantânea**.
* **Significado:** No contexto de CO₂, ela representa a **Velocidade de Emissão** (kg/dia).
* **Aplicação:** Indica a direção da tendência. Se $f'(x) > 0$, as emissões estão em rota de subida; se $f'(x) < 0$, há uma tendência de queda.

### 3. Segunda Derivada ($f''(x)$): Aceleração
Calculamos a segunda derivada para entender a **concavidade** da curva.
* **Significado:** Representa a **Aceleração das Emissões** (kg/dia²).
* **Aplicação:** Identifica se o crescimento está ganhando força (aceleração positiva) ou se o ritmo está diminuindo e prestes a estabilizar (aceleração negativa).

### 4. Modelo de Previsão (Extrapolação Linear)
A previsão para os próximos 7 dias é baseada na **Reta Tangente** ao último ponto conhecido, utilizando a expansão da Série de Taylor de primeira ordem:

$$V_{previsto} = V_{atual} + f'(t) \cdot \Delta t$$

Onde:
* **$V_{atual}$**: Último valor de CO₂ registrado.
* **$f'(t)$**: Inclinação (derivada) calculada no último ponto.
* **$\Delta t$**: Intervalo de dias no futuro.

