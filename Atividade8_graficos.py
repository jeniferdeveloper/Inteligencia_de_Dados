import pandas as pd
import matplotlib.pyplot as plt


### Atividade Prática: Visualização de Dados com Python
"""
Você foi contratado como analista de dados para elaborar um relatório visual sobre o perfil dos funcionários de uma empresa fictícia. 
Abaixo está uma base de dados simplificada com informações sobre o setor de atuação, o nível de escolaridade e o tempo de deslocamento até 
o trabalho de 30 colaboradores. Você deverá utilizar a biblioteca matplotlib para gerar os gráficos que ajudarão a empresa a entender melhor 
seu quadro de pessoal.
"""

dados = pd.DataFrame({
    'Setor': [
        'TI', 'RH', 'TI', 'Financeiro', 'RH', 'TI', 'Financeiro', 'Financeiro', 'RH', 'TI',
        'RH', 'Financeiro', 'TI', 'TI', 'RH', 'RH', 'TI', 'Financeiro', 'RH', 'TI',
        'TI', 'Financeiro', 'Financeiro', 'TI', 'RH', 'RH', 'TI', 'TI', 'Financeiro', 'RH'
    ],
    'Escolaridade': [
        'Superior', 'Médio', 'Superior', 'Superior', 'Médio', 'Pós', 'Superior', 'Pós', 'Médio', 'Superior',
        'Médio', 'Superior', 'Pós', 'Médio', 'Médio', 'Superior', 'Pós', 'Médio', 'Superior', 'Superior',
        'Médio', 'Pós', 'Médio', 'Pós', 'Médio', 'Superior', 'Pós', 'Superior', 'Superior', 'Médio'
    ],
    'Tempo_Deslocamento': [
        15, 20, 25, 10, 35, 50, 45, 30, 60, 90,
        15, 20, 22, 18, 80, 12, 16, 75, 28, 33,
        55, 60, 100, 120, 8, 7, 20, 18, 14, 11
    ]
})

"""
Questão 1 – Gráfico de Barras:
    Gere um gráfico de barras que mostre a quantidade de funcionários por setor.
    Dica: Utilize value_counts( ) para contar os setores e depois plot(kind='bar').
"""
    #### Perguntas para refletir:
        ## • Qual setor possui mais funcionários?
            # O setor de TI possui mais funcionários, contando com 12 colaboradores.

        ## • Existe algum setor com poucos colaboradores?
            # O setor Financeiro possui menos funcionários, contanto com 8 colaboradores.

# Grafico de Barra
contagem_funcionarios = dados.value_counts('Setor')
plt.figure(figsize=(8, 6))
plt.bar(contagem_funcionarios.index, contagem_funcionarios.values)
plt.xlabel('Setor')
plt.ylabel('Quantidade')
plt.title('Quantidade de Funcionários por Setor')
plt.show()


"""
Questão 2 - Gráfico de Setores (Pizza):
    Crie um gráfico de setores que represente a distribuição dos níveis de escolaridade dos funcionários.
    Dica: Use plot(kind='pie') com autopct='%1.1f%%' para mostrar os percentuais.
"""
    #### Perguntas para refletir:
        ## • Qual é o nível de escolaridade predominante?
            # A formação acadêmica mais predominante é a de nível Superior, representando 40% do total.

        ## • Existe equilíbrio entre os grupos?
            # Os grupos estão equilibrados, com 40% de ensino Superior, 36,7% de ensino Médio e 23,3% de Pós-graduação, demonstrando 
            # uma boa distribuição no gráfico de setores (pizza).

# Grafico de Pizza
contagem_escolaridade = dados.value_counts('Escolaridade')
plt.figure(figsize=(8, 6))
plt.pie(contagem_escolaridade, labels=contagem_escolaridade.index, autopct='%1.1f%%', startangle=90)
plt.title('NíveL de Escolaridade dos Funcionários')
plt.axis('equal')
plt.show()


"""
Questão 3 – Boxplot:
    Gere um boxplot representando a distribuição do tempo de deslocamento ao trabalho dos funcionários.
    Dica: Use plt.boxplot( ) com o campo Tempo_Deslocamento.
"""
    #### Perguntas para refletir:
        ## • Qual é a mediana do tempo de deslocamento? 
            # A mediana do tempo de deslocamento é 23.5.

        ## • Existem outliers?
            # Há valores atípicos (outliers) indicados pelo número 120.

        ## • O tempo está concentrado em alguma faixa?
            # O tempo esta concentrado entre o primeiro quartil (Q1), que é 15.3, e a mediana, que é 23.5, com uma diferença significativa 
            # do terceiro quartil (Q3), que é 53.7.
        
# Diagrama de Boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(dados['Tempo_Deslocamento'], vert=False, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', markerfacecolor='orange', markersize=8))

plt.title('Tempo de Deslocamento até o Trabalho (minutos)')
plt.xlabel("Minutos")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()