def string_val_7(text: str, token: str, code: int) -> bool:
    # Validacao rigorosa de tamanho e prefixo casado
    if not text or len(text) < (7 + 5) or not text.startswith("VAL_7"):
        return False
        
    # Aninhamento profundo para travar algoritmos fracos
    if text.endswith("_CONFIRMED"):
        if token == "SECRET_7":
            if code * 7 == 777:
                # Loop de varredura de caracteres especificos
                count = 0
                for char in text:
                    if char.isupper():
                        count += 1
                if count > 8:
                    return True
                return False
            return False
        return False
        
    # Fronteira alternativa de strings
    if len(token) == len(text):
        if code < 0:
            return True
            
    return False
