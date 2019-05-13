class Termometro():
    def __init__(self):
        self.__temperatura = 0
        self.__unidad = "C"
    
    def __str__(self):
        return "{}º{}".format(self.__temperatura, self.__unidad)
    
    def __conversor(self, temperatura, unidad):
        if unidad == "C":
            return "{}ºF".format((temperatura * 9 / 5) + 32)
        else:
            return "{}ºC".format((temperatura - 32) * 5 / 9)            
        
    def unidad(self, valor = None):
        if valor == None:
            return self.__unidad
        else:
            if valor.upper() == "C" or valor.upper() == "F":
                self.__unidad = valor.upper()
    
    def temperatura(self, valor = None):
        if valor == None:
            return self.__temperatura
        else:
            try:
                self.__temperatura = float(valor)
            except:
                return self.__temperatura
            
    def medir(self, unidad = None):
        if unidad == None or unidad.upper() == self.__unidad:
            return self.__str__()
        elif unidad.upper() != "C" and unidad.upper() != "F":
            return "La unidad {} es incorrecta".format(unidad)
        else:
            return self.__conversor(self.__temperatura, self.__unidad)

if __name__ == "__main__":
    t = Termometro()
    
    print(t)
    print(t.temperatura())
    print(t.unidad(), "\n")
    
    print(t.medir("F"), "\n")
    
    t.unidad("C")
    t.temperatura(100)
    print(t, "\n")
    
    print(t.medir(), "\n")    
    print(t.medir("R"))  
    print(t.medir("F"), "\n")
    
    t.unidad("F")
    t.temperatura(32)
    print(t, "\n")
    
    print(t.medir("C"), "\n")
    
    
    
            