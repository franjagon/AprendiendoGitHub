# Modulo 1 - Programa 2 con diccionarios de Ramón Maldonado

cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)
CadenaPrecio = input("Precio unitario (€): ")
precio = float(CadenaPrecio)

totalItems = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    item = dict()
    item['unidades'] = unidades
    item['precio'] = precio
    listaLineasFact.append(item)
    
    totalItems += unidades
    precioTotal += unidades * precio
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    CadenaPrecio = input("Precio unitario (€): ")
    precio = float(CadenaPrecio)    

for item in listaLineasFact:
    print(item['precio'], "€ - ", item['unidades'], " unidades - ", round(item['precio'] * item['unidades'], 2), "€")

print("--------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
