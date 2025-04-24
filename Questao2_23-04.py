import pandas as pd

"""
Questão 2 – Estoque de uma loja de eletrônicos Você recebeu uma planilha com a quantidade de vendas de 12 produtos em um mês. Os dados são os seguintes:

Tarefa:
1. Calcule e imprima:
 Média, Mediana e Moda das vendas
 Quartis: Q1 (25%), Q2 (50%) e Q3 (75%)
 Valor mínimo, valor máximo e amplitude
 Desvio padrão
"""

vendas = pd.Series([25, 32, 29, 41, 36, 20, 19, 45, 32, 30, 33, 28])

# Média
media = vendas.mean()
print(f"Média: {media}")

# Mediana
mediana = vendas.median()
print(f"Mediana: {mediana}")

# Moda
moda = vendas.mode()
print(f"Moda: {moda}")

# Medidas de Posição
#  Quartis: Q1 (25%), Q2 (50% = 0.5) e Q3 (75% = 0.75)
Q1 = vendas.quantile(0.25) # Primeiro quartil
print(f"\nPrimeiro quartil (Q1): {Q1}")

Q2 = vendas.quantile(0.5) # Segundo quartil
print(f"Segundo quartil (Q2): {Q2}")

Q3 = vendas.quantile(0.75) # Terceiro quartil
print(f"Terceiro quartil (Q3): {Q3}")

# Desvio padrão
desvio_padrao = vendas.std()
print(f"Desvio padrão: {desvio_padrao}")

# Valor mínimo, valor máximo e amplitude
print(f"\nMínimo: {vendas.min()}")
print(f"Máximo: {vendas.max()}")
print(f"Amplitude: {vendas.max() - vendas.min()}")

"""
RESULTADO

Média: 30.833333333333332
Mediana: 31.0
Moda: 0    32
dtype: int64

Primeiro quartil (Q1): 27.25
Segundo quartil (Q2): 31.0
Terceiro quartil (Q3): 33.75

Desvio padrão: 7.637626158259734

Mínimo: 19
Máximo: 45
Amplitude: 26
"""
#### 2. Faça uma análise:

    ### a) Os dados estão distribuídos de forma equilibrada ou há indícios de produtos com vendas fora do padrão?
        ## Mediana (31.0) ≈ Média (30.83) → Sugere que a distribuição é relativamente equilibrada em torno do centro.
        # Desvio Padrão (7.64) relativamente alto → Indica que os dados têm dispersão significativa, ou seja, algumas vendas estão bem acima ou abaixo da média.
        # Amplitude grande (26) → A diferença entre o mínimo (19) e o máximo (45) é grande, reforçando que o 45 é um valor atípico.

    ### b)  O gerente acredita que o produto mais vendido está muito acima da média. Com base nos seus cálculos, você concorda?
        # Não, pois o produto mais vendido não está muito acima da média (a moda 32 está praticamente na média (30.83))




"""
O IQR (Interquartile Range, ou "Intervalo Interquartil") é uma medida estatística que representa a dispersão dos 50% centrais de um conjunto 
de dados. Ele é calculado como a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1): IQR = Q3 - Q1

            Q1 = 27.25, Q3 = 33.75 → IQR = 6.5
            Limite inferior: 27.25 - 1.5×6.5 = 17.5
            Limite superior: 33.75 + 1.5×6.5 = 43.5
"""