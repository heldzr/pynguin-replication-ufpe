# Replicação Pynguin 

Este repositório contém o arcabouço metodológico e todos os dados resultantes da replicação empírica do framework Pynguin, avaliando a eficácia dos algoritmos DynaMOSA, MOSA, MIO, Whole Suite e Random sob pressão paramétrica escalável.

## Estrutura de Artefatos Entregues

* **Base Consolidada:** O arquivo mestre unificado [resultados_experimento_consolidado.csv](./resultados_experimento_consolidado.csv) está disponível na raiz para auditoria rápida das médias estatísticas.
* **Gráficos de Análise:** Os arquivos `curva_artigo_1_global.png`, `curva_artigo_2_math.png` e `curva_artigo_3_string.png` trazem a evidência visual do comportamento dos algoritmos.
* **Dados Brutos (900 Rodadas):** Devido ao volume massivo de diretórios lógicos gerados pelo framework, o histórico completo com as suítes de teste e relatórios XML está compactado no arquivo `resultados.zip` na raiz.
* **Módulos e Scripts:** As pastas `/dataset` e `/scripts` contêm as 60 funções de alta complexidade criadas e os códigos de automação/mineração.

## Resumo Estatístico do Experimento (Resultados Globais)

* **Domínio Numérico (TheAlgorithms):** DynaMOSA (98.1%) e MOSA (97.0%) lideraram com folga através do cálculo de distância de ramos. O MIO (83.9%) sofreu com dispersão estrutural.
* **Domínio Textual (Validators):** Colapso generalizado das meta-heurísticas (DynaMOSA 26.3% vs Random 21.7%), comprovando empiricamente a barreira teórica do **Platô de Aptidão (Fitness Plateau)** em validações booleanas de strings.
