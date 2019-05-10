# Modulo 1 - Programa 2 con listas de Ramón Maldonado

cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)
CadenaPrecio = input("Precio unitario (€): ")
precio = float(CadenaPrecio)

totalItems = 0
precioTotal = 0
lineasDeImpresion = ""

listaUnidades = []
listaPrecios = []

while unidades > 0 and precio > 0:
    listaUnidades.append(unidades)
    listaPrecios.append(precio)
    
    totalItems += unidades
    precioTotal += unidades * precio
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    CadenaPrecio = input("Precio unitario (€): ")
    precio = float(CadenaPrecio)    

print("")

for unidades, precio in zip(listaUnidades, listaPrecios):
    print("{:8.2f}€  - {:5.2f} unidades  - {:8.2f}€".format(precio, unidades, precio * unidades))

#print("\033[3;33;41m")
print("-----------------------------------------\n Total:\t\t{:8.2f}€\n Unidades:\t\t{:8.2f}".format(precioTotal,totalItems))
