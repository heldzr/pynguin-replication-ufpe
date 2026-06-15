def math_logic_29(x: int, y: int, z: int) -> int:
    # Restricao de entrada complexa (Dificulta a busca cega do Random)
    if (x * 3) + (y - 29) == 42:
        if z > x and z < y:
            # Loop dependente do estado das variaveis
            for i in range(1, 10):
                if i * z == 29 * 2:
                    return x + y + z + i
            return (x * y) // z
        else:
            if x % 2 == 0:
                return z - x
            return z - y
    
    # Caminho alternativo com multiplos desvios estruturais
    if z == 0:
        if x == y:
            raise ValueError("Divisao por zero disfarçada")
        return (x + y) // (29 * 2)
        
    return x - y + z
