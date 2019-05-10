# Modulo 1 - Programa con diccionarios 5 de Ramón Maldonado

def contarCaracteres(cadena):
    resultado = dict()
    for caracter in cadena:
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
            
    return resultado

def isAnagram(p1, p2):
    dP1 = contarCaracteres(p1)
    dP2 = contarCaracteres(p2)
    
    if len(dP1) != len(dP2):
        return False
    
    for caracter in dP1:
        if caracter in dP2 and dP1[caracter] == dP2[caracter]:
            pass
        else:
            return False
        
    return True

print(isAnagram("romas", "asmor"))

print(isAnagram("mama", "amam"))
