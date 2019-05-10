# Modulo 1 - Programa 6 de Ramón Maldonado

from sys import argv

def areaT(b, h):
    return b * h / 2

if __name__ == "__main__":
    print(argv[0])
    
    if len(argv) > 2:
        base = float(argv[1])
        altura = float(argv[2])
    else:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
    
    print("Superficie: {}".format(areaT(base, altura)))