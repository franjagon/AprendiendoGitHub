class Perro():
    def __init__(self, nombre, sexo, edad, peso):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.peso = peso
        
    def __str__(self):
        s = "s"        
        if self.edad == 1:
            s = ""
            
        if self.sexo == "M":
            return "Soy el perrito {}, tengo {} año{} y peso {} kg.".format(self.nombre, self.edad, s, self.peso)
        if self.sexo == "H":
            return "Soy la perrita {}, tengo {} año{} y peso {} kg.".format(self.nombre, self.edad, s, self.peso)
        
        return
    
    def ladrar(self, *l):
        ladrido = "guau, guau"
        
        if "aullar" in l:
            ladrido = "auuuuuu"
            
        if self.peso >= 8:
            print(ladrido.upper())
        else:
            print(ladrido.lower())

'''Esta sera una clase hija que heredará atributos y métodos de su clase padre. Y tambien podrá tener atributos y métodos propios.'''
class PerroAsistencia(Perro):
    def __init__(self, nombre, sexo, edad, peso, amo):
        Perro.__init__(self, nombre, sexo, edad, peso)
        self.amo = amo
        
        '''Las clases pueden tener métodos y atributos privados. Que se marcan anteponiendo a su nombre un par de guiones bajos.
           Estos atributos serán accesibles dentro de la propia clase pero no fuera de ella.'''
        self.__paseando = False

    '''La clase hija puede sobreescribir los métodos de su clase padre.'''
    def __str__(self):
        Perro.__str__(self)
        return "Soy {}, el perro de asistencia de {}.".format(self.nombre, self.amo)
    
    def ladrar(self, *l):
        if self.__paseando:
            print("Estoy ocupado en mi tarea. No puedo hacer ruido. Pídemelo más tarde.")       
        else:
            Perro.ladrar(self, *l)

    def pasear(self):
        self.__paseando = True
        print("{} acompaña y protege a {} caminando a su lado.".format(self.nombre, self.amo))

    '''Este es un método getter/setter.
       Estos métodos se utilizan para conocer/fijar el valor de un atributo privado de una clase sin acceder directamente a él.'''
    def paseando(self, valor = None):
        if valor == None:
            sn = "no "
            if self.__paseando:
                sn = ""
            
            print("{} {}está paseando".format(self.nombre, sn))
        else:
            self.__paseando = valor
        
        
if __name__ == "__main__":
    pepe = Perro("Pepe", 'M', 4, 12)
    lola = Perro("Lola", 'H', 1, 5)

    print(pepe)
    print("Pepe, ladra: ", end="")
    pepe.ladrar()
    print("Pepe, aulla: ", end="")
    pepe.ladrar("aullar")

    print(lola)
    print("Lola, ladra: ", end="")
    lola.ladrar()
    print("Lola, aulla: ", end="")
    lola.ladrar("aullar")

    print()
    
    rantamplan = PerroAsistencia("Ran Tam Plan", 'M', 4, 8, "Lucky Luke")
    
    print(rantamplan)
    print("Ran Tam Plan, ladra: ", end="")
    rantamplan.ladrar()
    print("Ran Tam Plan, aulla: ", end="")
    rantamplan.ladrar("aullar")

    print()
        
    rantamplan.pasear()
    print("Ran Tam Plan, ladra: ", end="")
    rantamplan.ladrar()

    print()
        
    rantamplan.paseando()
    print("Ran Tam Plan, ladra: ", end="")
    rantamplan.ladrar()
    rantamplan.paseando(False)
    rantamplan.paseando()
    print("Ran Tam Plan, ladra: ", end="")
    rantamplan.ladrar()

    print()
    
    '''Para poder acceder a un parametro privado se antepone de un guión bajo y su clase'''
    print(rantamplan._PerroAsistencia__paseando)
    
