# pip install pandas matplotlib    --> instalar pacotes

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.Series([5,6,7,2,3,9,10,8,6,9])

# Grafico de Pizza
contagem_valores = dados.value_counts()
plt.figure(figsize=(8, 6))
plt.pie(contagem_valores, labels=contagem_valores.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Frequencia de Dados')
plt.axis('equal')
plt.show()

# Grafico de Barra
plt.figure(figsize=(8, 6))
plt.bar(contagem_valores.index, contagem_valores.values)
plt.xlabel('Valores')
plt.ylabel('Frequencia')
plt.title('Frequencia de cada Valor')
plt.show()

# Diagrama de Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(dados, vert=False)
plt.title('Boxplot de Dados')
plt.xlabel('Valores')
plt.show()


# Base de dados simulada: tempo de deslocamento ao trabalho (minutos)
tempo_deslocamento = pd.Series([
    10, 12, 15, 13, 14, 16, 20, 22, 25, 30,
    35, 36, 38, 40, 42, 43, 45, 50, 55, 60,
    65, 70, 75, 80, 90, 100, 120, 150, 180, 200
])

# Diagrama de Boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(tempo_deslocamento, vert=False, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', markerfacecolor='orange', markersize=8))

plt.title('Tempo de Deslocamento até o Trabalho (minutos)')
plt.xlabel("Minutos")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()