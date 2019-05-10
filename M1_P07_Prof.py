# Modulo 1 - Programa 7 de Ramón Maldonado
#
import M1_P07_Prof_Screen

def tipoEntrada(e):
    if e > 0 and e <= 2:
        tipo = 'bebe'
    elif e <= 12:
        tipo = 'niño'
    elif e < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    
    return tipo

def validaEdad(cadena):
    try:
        n = int(cadena)
        
        if n >= 0:
            return True
        
        return False
    except:
        return False

def pedirEdad():
    edad = M1_P07_Prof_Screen.Input("¿Qué edad tienes? ", line=1, column=1)
    
    while not validaEdad(edad):
        M1_P07_Prof_Screen.Print("Edad inválida", line=25, column=1, color="yellow", back='red', style='bold')
        edad = M1_P07_Prof_Screen.Input("¿Qué edad tienes? ", line=1, column=1)
    
    M1_P07_Prof_Screen.clearLine(25)
        
    return int(edad)

def printScreen():
    M1_P07_Prof_Screen.clear()
    M1_P07_Prof_Screen.Print("Bebé....:   -", line=4, column=5)
    M1_P07_Prof_Screen.Print("Niño....:   -", line=5, column=5)
    M1_P07_Prof_Screen.Print("Adulto..:   -", line=6, column=5)
    M1_P07_Prof_Screen.Print("Jubilado:   -", line=7, column=5)
    M1_P07_Prof_Screen.Print("Total....:", line=9, column=8, style='bold')
    
def main():
    preciosE = {'bebe': 0.0, 'niño': 14.0, 'adulto': 23.0, 'jubilado': 18.0}
    numEntradas = {'bebe': 0, 'niño': 0, 'adulto': 0, 'jubilado': 0}
    entradasQ = {'bebe': {'cantidad': (4, 15), 'precioA': (4, 19)},
                 'niño': {'cantidad': (5, 15), 'precioA': (5, 19)},
                 'adulto': {'cantidad': (6, 15), 'precioA': (6, 19)},
                 'jubilado': {'cantidad': (7, 15), 'precioA': (7, 19)}}

    printScreen()

    precioTotal = 0

    edad = pedirEdad()

    while edad != 0:
        tipoE = tipoEntrada(edad)
        precioE = preciosE[tipoE]
        numEntradas[tipoE] += 1
        precioTotal += precioE
        
        M1_P07_Prof_Screen.Print(numEntradas[tipoE], line=entradasQ[tipoE]['cantidad'][0], column=entradasQ[tipoE]['cantidad'][1])
        M1_P07_Prof_Screen.Print("{:7.2f}€".format(numEntradas[tipoE] * precioE), \
                                 line=entradasQ[tipoE]['precioA'][0], column=entradasQ[tipoE]['precioA'][1])
        M1_P07_Prof_Screen.Print("{:7.2f}€".format(precioTotal), line=9, column=19, style='bold')
        
        edad = pedirEdad()
        
    fEntradas = open('M1_P07_Prof_transacciones.txt', 'a+')
    transaccion = "{},{},{},{}\n".format(numEntradas['bebe'], numEntradas['niño'], numEntradas['adulto'], numEntradas['jubilado'])
    fEntradas.write(transaccion)
    fEntradas.close()
        
    M1_P07_Prof_Screen.locate(11, 1)

main()

