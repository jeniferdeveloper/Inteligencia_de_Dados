import pandas as pd

"""Questão 1 – Análise de avaliações de um curso online Uma plataforma de cursos online registrou as notas de avaliação de um de seus
cursos por 15 estudantes. As notas vão de 0 a 10.

Tarefa:
1. Calcule e imprima:
 Média
 Mediana
 Moda
 Primeiro Quartil (Q1)
 Percentil 90 (P90)
 Desvio Padrão
 Amplitude
"""

avaliacoes = pd.Series([8, 7, 9, 6, 10, 8, 7, 9, 10, 9, 5, 6, 7, 8, 10])

# Média
media = avaliacoes.mean()
print(f"Média: {media}")
# Mediana
mediana = avaliacoes.median()
print(f"Mediana: {mediana}")
# Moda
moda = avaliacoes.mode()
print(f"Moda: {moda}")

# Medidas de Posição
Q1 = avaliacoes.quantile(0.25) # Primeiro quartil
print(f"\nPrimeiro quartil (Q1): {Q1}")

P90 = avaliacoes.quantile(0.90) # 90% percentil
print(f"Percentil 90 (P90): {P90}")

#  Desvio Padrão
desvio_padrao = avaliacoes.std()
print(f"Desvio padrão: {desvio_padrao}")

# Amplitude
print(f"\nMínimo: {avaliacoes.min()}")
print(f"Máximo: {avaliacoes.max()}")
print(f"Amplitude: {avaliacoes.max() - avaliacoes.min()}")

"""
RESULTADOS

Média: 7.933333333333334
Mediana: 8.0
Moda: 0     7
1     8
2     9
3    10
dtype: int64

Primeiro quartil (Q1): 7.0
Percentil 90 (P90): 10.0
Desvio padrão: 1.579632265825846

Mínimo: 5
Máximo: 10
Amplitude: 5
"""

#### 2. Com base nos resultados, responda:

### a) As notas estão concentradas próximas da média? Justifique com base na mediana, moda e desvio padrão
    ## Sim, as notas estão concentradas próximas da média. Observando que:
        # A mediana (8.0) é próxima da média (Média: 7.93), indicando uma distribuição aproximadamente simétrica, sem grande distorção para valores muito altos ou baixos.
        # O desvio padrão (~1.58) é relativamente baixo em comparação com a amplitude total (5), sugerindo que a maioria das notas está dentro de 1-2 desvios padrão da média.
        # As notas mais frequentes (moda = 7, 8, 9, 10) estão um pouco acima da média, mas ainda dentro de uma faixa razoável.

### b) A nota mais comum foi alta ou baixa?
    ## A nota mais comum foi alta. De acordo com a moda as notas 7, 8, 9, 10 aparecem 3 vezes cada. Ambas estão acima da média (7.8) e da mediana
    # (8.0), indicando que as notas mais frequentes estão na parte superior da distribuição.