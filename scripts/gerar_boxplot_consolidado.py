import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar a base de dados mestre com as 3 bibliotecas (90 módulos)
path_final_unificado = r"C:\pynguin-sbst-replication\resultados_experimento_total.csv"
df = pd.read_csv(path_final_unificado)

# 2. Calcular a média das 3 repetições para cada um dos 90 módulos por algoritmo
# Isso gera exatamente os pontos de distribuição que o boxplot precisa
df_boxplot = df.groupby(["Familia", "Modulo_ID", "Algoritmo"], as_index=False)["Coverage"].mean()

# 3. Configurações de Identidade Visual (Idêntico ao seu padrão anterior)
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Definir a ordem exata dos algoritmos no eixo X
ordem_algoritmos = ["DYNAMOSA", "MOSA", "MIO", "WHOLE_SUITE", "RANDOM"]

paleta_cores = {
    "DYNAMOSA": "#1f77b4",     # Azul
    "MOSA": "#ff7f0e",         # Laranja
    "MIO": "#2ca02c",          # Verde
    "WHOLE_SUITE": "#9467bd",  # Roxo
    "RANDOM": "#d62728"        # Vermelho
}

# 4. Plotar o Boxplot Consolidado
# Adicionamos o 'showmeans=True' caso queira exibir um triângulo com a média exata
sns.boxplot(
    data=df_boxplot,
    x="Algoritmo",
    y="Coverage",
    order=ordem_algoritmos,
    palette=paleta_cores,
    width=0.5,
    linewidth=1.5,
    showmeans=True,
    meanprops={"marker":"^", "markerfacecolor":"white", "markeredgecolor":"black", "markersize": 7}
)

# 5. Customização de Eixos e Títulos
plt.title("Distribuição Geral de Cobertura de Ramos (Consolidado - 90 Módulos)", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Algoritmos de Busca", fontsize=11, labelpad=10)
plt.ylabel("Branch Coverage Média (0.0 a 1.0)", fontsize=11, labelpad=10)

# Ajustar a escala do eixo Y para destacar o topo e as quedas
plt.ylim(0.0, 1.05)

plt.tight_layout()

# 6. Salvar o gráfico final em alta definição
output_boxplot_path = r"C:\pynguin-sbst-replication\boxplot_consolidado_90_modulos.png"
plt.savefig(output_boxplot_path, dpi=300)
plt.close()

print(f"📊 [SUCESSO] O boxplot consolidado dos 90 módulos foi salvo em: {output_boxplot_path}")