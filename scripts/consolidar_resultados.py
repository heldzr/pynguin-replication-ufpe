import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def consolidar_e_gerar_insights():
    pasta_resultados = "./resultados"
    dados_mestres = []
    
    print("=== 1. INICIANDO MINERAÇÃO DOS DADOS (900 ARQUIVOS) ===")
    
    if not os.path.exists(pasta_resultados):
        print(f"❌ Erro: A pasta {pasta_resultados} não foi encontrada.")
        return

    pastas = [f for f in os.listdir(pasta_resultados) if os.path.isdir(os.path.join(pasta_resultados, f))]
    print(f"Localizadas {len(pastas)} pastas de execução para análise.")

    for subpasta in pastas:
        caminho_csv = os.path.join(pasta_resultados, subpasta, "statistics.csv")
        
        if os.path.exists(caminho_csv):
            try:
                # Lê o CSV estático ("TargetModule", "Coverage")
                df = pd.read_csv(caminho_csv)
                if df.empty:
                    continue
                
                # Mapeamento de metadados contornando o nome composto de "WHOLE_SUITE"
                partes = subpasta.split("_")
                
                if "WHOLE_SUITE" in subpasta:
                    algoritmo = "WHOLE_SUITE"
                    repeticao = partes[3].replace("rep", "")  # run_WHOLE_SUITE_rep1... (posição muda)
                else:
                    algoritmo = partes[1]                     # run_DYNAMOSA_rep1...
                    repeticao = partes[2].replace("rep", "")
                
                # Identifica se pertence à família matemática ou de strings
                if "math" in subpasta:
                    familia = "TheAlgorithms"
                    modulo_id = partes[-1]
                else:
                    familia = "Validators"
                    modulo_id = partes[-1]
                
                # Injeta os metadados acadêmicos estruturados
                df["Algoritmo"] = algoritmo
                df["Repeticao"] = int(repeticao)
                df["Familia"] = familia
                df["Modulo_ID"] = int(modulo_id)
                df["Nome_Cenario"] = subpasta
                
                dados_mestres.append(df)
            except Exception as e:
                print(f"⚠️ Erro ao processar a pasta {subpasta}: {e}")

    if not dados_mestres:
        print("❌ Nenhum dado pôde ser extraído. Verifique se os arquivos existem.")
        return

    # Unifica tudo em um único DataFrame Mestre
    df_final = pd.concat(dados_mestres, ignore_index=True)
    
    # Organiza as colunas
    colunas_ordenadas = ["Familia", "Modulo_ID", "Algoritmo", "Repeticao", "TargetModule", "Coverage"]
    df_final = df_final[colunas_ordenadas]
    
    # Salva o CSV mestre na raiz
    caminho_csv_saida = "./resultados_experimento_consolidado.csv"
    df_final.to_csv(caminho_csv_saida, index=False)
    print(f"📊 Base mestre consolidada salva com sucesso em: {caminho_csv_saida}")

    print("\n=== 2. GERANDO GRÁFICOS ESTATÍSTOS PARA OS SLIDES ===")
    sns.set_theme(style="whitegrid")

    # --- GRÁFICO 1: BOXPLOT COMPARATIVO DE COBERTURA FINAL ---
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_final, x="Algoritmo", y="Coverage", hue="Familia", palette="Set2")
    plt.title("Distribuição Estatística da Cobertura de Ramos Final (Branch Coverage)", fontsize=14, fontweight='bold')
    plt.xlabel("Algoritmo de Busca", fontsize=12)
    plt.ylabel("Taxa de Cobertura (0.0 a 1.0)", fontsize=12)
    plt.ylim(-0.05, 1.05)
    plt.legend(title="Domínio do Problema")
    plt.tight_layout()
    plt.savefig("./boxplot_cobertura_final.png", dpi=300)
    plt.close()
    print("📈 Gráfico [boxplot_cobertura_final.png] gerado com sucesso!")

    # --- GRÁFICO 2: CURVA DE DEGRADAÇÃO POR ID (CRESCIMENTO DA COMPLEXIDADE) ---
    plt.figure(figsize=(12, 6))
    df_agrupado = df_final.groupby(["Familia", "Algoritmo", "Modulo_ID"])["Coverage"].mean().reset_index()
    
    sns.lineplot(data=df_agrupado, x="Modulo_ID", y="Coverage", hue="Algoritmo", style="Familia", markers=True, dashes=False)
    plt.title("Impacto do Aumento de Restrições na Performance (ID 1 a 30)", fontsize=14, fontweight='bold')
    plt.xlabel("Identificador do Cenário (ID Crescente = Maior Restrição)", fontsize=12)
    plt.ylabel("Média de Cobertura de Ramos", fontsize=12)
    plt.xticks(range(1, 31, 2))
    plt.ylim(-0.05, 1.05)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("./curva_degradacao_complexidade.png", dpi=300)
    plt.close()
    print("📉 Gráfico [curva_degradacao_complexidade.png] gerado com sucesso!")

    # --- 3. EXIBE INSIGHTS RÁPIDOS NO TERMINAL ---
    print("\n=== 3. INSIGHTS BRUTOS PARA COPIAR PARA OS SLIDES ===")
    resumo_geral = df_final.groupby(["Familia", "Algoritmo"])["Coverage"].mean().reset_index()
    print(resumo_geral.to_string(index=False))

if __name__ == "__main__":
    consolidar_e_gerar_insights()