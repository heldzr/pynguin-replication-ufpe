import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados minerados
csv_path = r"C:\pynguin-sbst-replication\tabela_resultados_sorting.csv"
df = pd.read_csv(csv_path)

# 2. Calcular a média das 3 repetições para cada Módulo e Algoritmo
# Isso garante uma linha contínua e estável no gráfico
df_agrupado = df.groupby(["Modulo", "Algoritmo"], as_index=False)["Cobertura"].mean()

# Opcional: Se quiser ordenar os módulos no eixo X caso eles apareçam fora de ordem física
# df_agrupado['sort_key'] = df_agrupado['Modulo'].str.extract('(\d+)').astype(float)
# df_agrupado = df_agrupado.sort_values(by=['sort_key', 'Algoritmo'])

# 3. Configurar a identidade visual do gráfico
plt.figure(figsize=(14, 7))
sns.set_theme(style="whitegrid")

# Definir paleta de cores marcantes para diferenciar bem os algoritmos
paleta_cores = {
    "DYNAMOSA": "#1f77b4",     # Azul escuro
    "MOSA": "#ff7f0e",         # Laranja
    "MIO": "#2ca02c",          # Verde
    "WHOLE_SUITE": "#9467bd",  # Roxo
    "RANDOM": "#d62728"        # Vermelho (Destaque para a queda de performance)
}

# 4. Plotar o gráfico de linhas com marcadores em cada ponto de dado
plot = sns.lineplot(
    data=df_agrupado,
    x="Modulo",
    y="Cobertura",
    hue="Algoritmo",
    style="Algoritmo",
    markers=True,
    markersize=8,
    linewidth=2.5,
    palette=paleta_cores
)

# 5. Ajustar títulos e rótulos dos eixos
plt.title("Análise Comparativa de Cobertura de Ramos por Complexidade Paramétrica (Sorting)", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Módulos de Ordenação (Complexidade Paramétrica Crescente)", fontsize=12, labelpad=10)
plt.ylabel("Branch Coverage Média (0.0 a 1.0)", fontsize=12, labelpad=10)

# Garantir que o eixo Y represente fielmente a escala de cobertura (0% a 100%)
plt.ylim(-0.05, 1.05)

# Rotacionar os nomes dos módulos no eixo X para não sobrepor o texto
plt.xticks(rotation=45, ha='right')

# Customizar a legenda
plt.legend(title="Algoritmos SBST", title_fontsize='11', loc="lower left", frameon=True, shadow=True)

plt.tight_layout()

# 6. Salvar o gráfico em alta definição (pronto para incluir na dissertação/relatório)
output_graph_path = r"C:\pynguin-sbst-replication\grafico_comparativo_sorting.png"
plt.savefig(output_graph_path, dpi=300)
plt.close()

print(f"📊 [SUCESSO] Gráfico gerado e salvo em alta definição em: {output_graph_path}")