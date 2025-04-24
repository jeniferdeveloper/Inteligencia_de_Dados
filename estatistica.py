import pandas as pd
dados = pd.Series([5,6,7,2,3,9,10,8,6,9])
media = dados.mean()
print(f"Média: {media}")

mediana = dados.median()
print(f"Mediana: {mediana}")

moda = dados.mode() # repetição
print(f"Moda: {moda}")

# Medidas de Posição
Q1 = dados.quantile(0.25) # Primeiro quartil
print(f"\nPrimeiro quartil (Q1): {Q1}")

P90 = dados.quantile(0.90) # 90% percentil
print(f"Percentil 90 (P90): {P90}")

desvio_padrao = dados.std()
print(f"Desvio padrão: {desvio_padrao}")

print(f"\nMínimo: {dados.min()}")
print(f"Máximo: {dados.max()}")
print(f"Amplitude: {dados.max() - dados.min()}")

print(dados.describe(percentiles=[.25, .5, .9]))