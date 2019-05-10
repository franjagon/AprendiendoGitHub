# Modulo 1 - Programa 8 de Ramón Maldonado
#
fEntradas = open("M1_P07_Prof_transacciones.txt", 'r')

todas = fEntradas.read()
transacciones = todas.split('\n')
print(transacciones)

fEntradas.close()

fEntradas = open("M1_P07_Prof_transacciones.txt", 'r')

todas = fEntradas.readlines()
for transaccion in todas:
    print(transaccion[:-1], "-- ", end = "")

fEntradas.close()

print("\nLo anterior eran ejemplos de como leer un fichero\n")

preciosE = {'bebe': 0.0, 'niño': 14.0, 'adulto': 23.0, 'jubilado': 18.0}

numEntBebe = 0
numEntNiño = 0
numEntAdulto = 0
numEntJubilado = 0

numTot = 0
preTot = 0

fEntradas = open("M1_P07_Prof_transacciones.txt", 'r')

salir = False
while not salir:
    fila = fEntradas.readline()
    if fila != '':
        listaFila = fila.split(',')
        numEntBebe += int(listaFila[0])
        numTot += int(listaFila[0])
        preTot += int(listaFila[0]) * preciosE['bebe']
        numEntNiño += int(listaFila[1])
        numTot += int(listaFila[1])
        preTot += int(listaFila[1]) * preciosE['niño']
        numEntAdulto += int(listaFila[2])
        numTot += int(listaFila[2])
        preTot += int(listaFila[2]) * preciosE['adulto']
        numEntJubilado += int(listaFila[3])
        numTot += int(listaFila[3])
        preTot += int(listaFila[3]) * preciosE['jubilado']
    else:
        salir = True

fEntradas.close()

print("Entradas de Bebe:     {:3d}  -  {:7.2f}€".format(numEntBebe, numEntBebe * preciosE['bebe']))
print("Entradas de Niño:     {:3d}  -  {:7.2f}€".format(numEntNiño, numEntNiño * preciosE['niño']))
print("Entradas de Adulto:   {:3d}  -  {:7.2f}€".format(numEntAdulto, numEntAdulto * preciosE['adulto']))
print("Entradas de Jubilado: {:3d}  -  {:7.2f}€".format(numEntJubilado, numEntJubilado * preciosE['jubilado']))
print("\nTotal:                {:3d}  -  {:7.2f}€".format(numTot, preTot))
