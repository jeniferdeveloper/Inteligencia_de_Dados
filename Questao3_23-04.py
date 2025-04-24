import pandas as pd

"""Questão 3 – Pesquisando o tempo de estudo diário. Em uma pesquisa com 10 alunos sobre o tempo diário de estudo para
programação (em horas), os seguintes dados foram registrados:

Tarefa:
1. Calcule:
 Média, Moda, Mediana
 Desvio padrão
 Percentis 25, 50, 75 e 90
 Crie uma análise descritiva completa com describe()
"""

estudo = pd.Series([2, 3, 4, 5, 1, 3, 4, 6, 2, 3])

# Média
media = estudo.mean()
print(f"Média: {media}")

# Mediana
mediana = estudo.median()
print(f"Mediana: {mediana}")

# Moda
moda = estudo.mode()
print(f"Moda: {moda}")

# Medidas de Posição
#  Percentis 25, 50, 75 e 90
P25 = estudo.quantile(0.25) # 25% percentil
print(f"Percentil 25 (P25): {P25}")

P50 = estudo.quantile(0.5) # 50% percentil
print(f"Percentil 50 (P50): {P50}")

P75 = estudo.quantile(0.75) # 75% percentil
print(f"Percentil 75 (P75): {P75}")

P90 = estudo.quantile(0.90) # 90% percentil
print(f"Percentil 90 (P90): {P90}")

# Desvio padrão
desvio_padrao = estudo.std()
print(f"Desvio padrão: {desvio_padrao}")

# Valor mínimo, valor máximo e amplitude
print(f"Mínimo: {estudo.min()}")
print(f"Máximo: {estudo.max()}")
print(f"Amplitude: {estudo.max() - estudo.min()}")

# describe()
print("\nDescribe") # pular linha
print(estudo.describe(percentiles=[.25, .5, .75, .9]))

"""
RESULTADO

Média: 3.3
Mediana: 3.0
Moda: 0    3
dtype: int64
Percentil 25 (P25): 2.25
Percentil 50 (P50): 3.0
Percentil 75 (P75): 4.0
Percentil 90 (P90): 5.1
Desvio padrão: 1.4944341180973262
Mínimo: 1
Máximo: 6
Amplitude: 5

Describe
count    10.000000
mean      3.300000
std       1.494434
min       1.000000
25%       2.250000
50%       3.000000
75%       4.000000
90%       5.100000
max       6.000000
dtype: float64
"""

#### 2. Responda:

    ### a)  A distribuição dos dados é simétrica ou assimétrica? Baseie-se na omparação entre média, mediana e moda.
        ## A distribuição dos dados é assimétrica, porque o resultado  da média, da mediana e da moda são muito próximas ou iguais. 

    ### b) A maioria dos alunos estuda mais ou menos do que a média?
        ## A maioria dos alunos estuda MENOS que a média, porque na conta tem 6 valores abaixo da média e 4 valores acima: 
            # Menores que 3.3: 2, 3, 1, 3, 2, 3 (6 valores)
            # Maiores que 3.3: 4, 5, 4, 6 (4 valores)
        # Portanto, a maioria dos alunos (6 em 10) estuda menos do que a média.