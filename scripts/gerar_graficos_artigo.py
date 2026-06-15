import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carrega a base consolidada
df = pd.read_csv("./resultados_experimento_consolidado.csv")

# Calcula as médias agrupando as 3 repetições de cada cenário
df_g = df.groupby(["Familia", "Algoritmo", "Modulo_ID"])["Coverage"].mean().reset_index()

# Configuração do estilo científico igual ao da imagem anexada
sns.set_theme(style="ticks")
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11

# Paleta de cores e marcadores customizados para diferenciar bem os algoritmos
cores = {"DYNAMOSA": "#00cbd6", "MOSA": "#ff3344", "WHOLE_SUITE": "#7a22ed", "MIO": "#ff9900", "RANDOM": "#a1d914"}
marcadores = {"DYNAMOSA": "+", "MOSA": "x", "WHOLE_SUITE": "d", "MIO": "o", "RANDOM": ""}

def plotar_curva_estilo_artigo(data, titulo, nome_arquivo):
    plt.figure(figsize=(7, 5))
    
    # Plota a linha de cada algoritmo individualmente para aplicar os marcadores do artigo
    for alg in data["Algoritmo"].unique():
        sub_df = data[data["Algoritmo"] == alg].sort_values("Modulo_ID")
        plt.plot(
            sub_df["Modulo_ID"], 
            sub_df["Coverage"], 
            label=alg,
            color=cores.get(alg, "#333333"),
            marker=marcadores.get(alg, ""),
            markersize=6,
            linestyle="--" if alg in ["MIO", "WHOLE_SUITE"] else "-",
            linewidth=1.5
        )
        
    plt.title(titulo, fontsize=12, fontweight='bold', pad=15)
    plt.xlabel("Complexidade do Cenário (Identificador ID 1 a 30)")
    plt.ylabel("Cobertura de Ramos Média (Branch Coverage)")
    plt.xlim(0, 31)
    plt.ylim(-0.05, 1.05)
    plt.xticks(range(1, 31, 2))
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="lower left" if "Validators" in titulo else "upper right", frameon=True)
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=300)
    plt.close()

# --- 1. GRÁFICO GLOBAL (AGRUPADO) ---
# Tira a média geral sem separar por família de código
df_global = df.groupby(["Algoritmo", "Modulo_ID"])["Coverage"].mean().reset_index()
plotar_curva_estilo_artigo(df_global, "Pynguin: Geração de Testes (Média Combinada Global)", "./curva_artigo_1_global.png")
print("-> Gráfico 1: Global Gerado!")

# --- 2. GRÁFICO SEGMENTADO: MATEMÁTICA (TheAlgorithms) ---
df_math = df_g[df_g["Familia"] == "TheAlgorithms"]
plotar_curva_estilo_artigo(df_math, "Pynguin: Domínio de Restrições Matemáticas (TheAlgorithms)", "./curva_artigo_2_math.png")
print("-> Gráfico 2: Segmentado Matemática Gerado!")

# --- 3. GRÁFICO SEGMENTADO: STRINGS (Validators) ---
df_string = df_g[df_g["Familia"] == "Validators"]
plotar_curva_estilo_artigo(df_string, "Pynguin: Domínio de Restrições de Strings (Validators)", "./curva_artigo_3_string.png")
print("-> Gráfico 3: Segmentado Strings Gerado!")

print("\n🎉 Todos os 3 gráficos estilo artigo foram salvos na raiz do projeto!")