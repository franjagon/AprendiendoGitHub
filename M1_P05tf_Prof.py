# Modulo 1 - Programa con lista de True/False 5 de Ramón Maldonado (que no funciona... ver 'arara' y 'arrar')

def isAnagramEle(p1, p2):
    ListaComparacionLetras = []
    
    if len(p1) == len(p2):
        for caracter1 in p1:
            noPongasFalse = False
            for caracter2 in p2:
                if caracter1 == caracter2:
                    noPongasFalse = True
                    ListaComparacionLetras.append(True)
                
            if not noPongasFalse:
                ListaComparacionLetras.append(False)
    else:
        ListaComparacionLetras.append(False)

                
    if False in ListaComparacionLetras:
        return False
    else:
        return True

def isAnagram(p1, p2):
    sn = "no"
    if isAnagramEle(p1, p2) and isAnagramEle(p2, p1):
        sn = "sí"

    print("{} y {}, {} son anagramas".format(p1, p2, sn))

isAnagram("arara", "rarra")