from functools import reduce

lista = [1, 3, -2, 15, 9]

print("Tomamos esta lista", list(lista))
print("La lista cuyos elementos son el doble (dobles):", list(map(lambda x : x * 2, list(lista))))
print("Los elementos pares de la lista:", list(filter(lambda x : x % 2 == 0, list(lista))))
print("Los elementos pares de la lista de dobles:", list(filter(lambda x : x % 2 == 0, list(map(lambda x : x * 2, list(lista))))))

sumatorio = reduce(lambda x, y : x + y, list(lista))
sumadoble = reduce(lambda x, y : x + (y * 2), list(lista))
sumadobles = reduce(lambda x, y : x + y, list(map(lambda x : x * 2, list(lista))))
suma100 = reduce(lambda x, y : x + y, range(101))

print("La suma de los elementos de la lista es: ", sumatorio)
print("La suma de los elementos dobles de la lista (el primero sin doblar) es: ", sumadoble)
print("La suma de los elementos dobles de la lista es: ", sumadobles)
print("La suma de los 100 primeros números positivos es: ", suma100)

