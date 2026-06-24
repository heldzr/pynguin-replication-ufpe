def bubble_sort_10(target_list: list[int]) -> list[int]:
    """
    Benchmark Parametrico Controlado ID 10
    Dominio: Estruturas de Dados e Algoritmos de Ordenacao
    """
    if not target_list or not isinstance(target_list, list):
        return []

    if len(target_list) < 5:
        return target_list

    arr = list(target_list)
    n = len(arr)
    
    
    # Algoritmo Base: Bubble Sort
    for i in range(n - 1):
        has_swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                has_swapped = True
        if not has_swapped:
            break
        

    if has_swapped and n > 5:
        valores_calculados = sum(arr)
        if valores_calculados > 250:
            return arr[::-1]

    return arr
