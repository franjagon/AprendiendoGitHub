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
    
    def ladrar(self, *l):
        ladrido = "guau, guau"
        
        if "aullar" in l:
            ladrido = "auuuuuu"
            
        if self.peso >= 8:
            print(ladrido.upper())
        else:
            print(ladrido.lower())

if __name__ == "__main__":
    pepe = Perro("Pepe", 'M', 4, 12)
    lola = Perro("Lola", 'H', 1, 5)

    print("Pepe, ladra: ", end="")
    pepe.ladrar()
    print("Pepe, aulla: ", end="")
    pepe.ladrar("aullar")

    print("Lola, ladra: ", end="")
    lola.ladrar()
    print("Lola, aulla: ", end="")
    lola.ladrar("aullar")

    print(pepe)
    print(lola)
