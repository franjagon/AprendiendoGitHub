# Modulo 0 -  Programa 1 de Ramón Maldonado

# Definición de funciones
def validacion(mensaje):
    strNumero = input(mensaje)

    isvalid = False
    while not isvalid:
        if strNumero.isdigit():
            isvalid = True
        elif strNumero != '' and strNumero[0] == '-' and strNumero[1:].isdigit():
            isvalid = True
        else:
            print(strNumero, "debe ser un entero")
            strNumero = input(mensaje)
            
    return strNumero    
    
# Entrada y validación de datos
strNumero01 = validacion("Introduzca un número: ")      
strNumero02 = validacion("Introduzca otro número: ")
        
# Transformacion y procesamiento de datos
numero01 = int(strNumero01) / 10
numero02 = int(strNumero02) / 10

suma = round(numero01 + numero02, 2)
resta = numero01 - numero02
resta = round(resta, 2)
producto = round(numero01 * numero02, 2)
division = round(numero01 / numero02, 2)

# Salida de resultados
print(numero01, "+", numero02, "=", suma)
print(numero01, "-", numero02, "=", resta)
print(numero01, "·", numero02, "=", producto)
print(numero01, "/", numero02, "=", division)
