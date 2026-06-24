Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "=== INICIANDO EXPERIMENTO EXPANDIDO: SORTING     ===" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

if (!(Test-Path ".\resultados")) { New-Item -ItemType Directory -Path ".\resultados" | Out-Null }

$ALGORITHMS = @("DYNAMOSA", "MOSA", "MIO", "WHOLE_SUITE", "RANDOM")
$INPUT_DIR = "./dataset/sorting_algorithms"

$modules = Get-ChildItem -Path $INPUT_DIR -Filter *.py | Select-Object -ExpandProperty BaseName

foreach ($mod in $modules) {
    foreach ($alg in $ALGORITHMS) {
        foreach ($rep in 1..3) {
            $output_folder = "run_${alg}_rep${rep}_${mod}"
            
            Write-Host "=== [EXECUÇÃO] [Sorting] ${mod} | Alg: ${alg} | Rep: ${rep} (300s) ===" -ForegroundColor Yellow
            
            # Adicionado --statistics-backend CONSOLE para forçar a geração das tabelas temporais detalhadas
            docker run --rm -v "${pwd}/resultados:/app/resultados" -v "${pwd}/dataset:/app/dataset" -e PYNGUIN_DANGER_AWARE=true pynguin-rec --project-path /app/dataset/sorting_algorithms --module-name $mod --output-path /app/resultados/$output_folder --algorithm $alg --maximum-search-time 300 --create-coverage-report True --timeline-interval 1 --report-dir /app/resultados/$output_folder --statistics-backend CONSOLE
        }
    }
}
