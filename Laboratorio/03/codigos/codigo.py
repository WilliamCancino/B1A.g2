class Gato(object):
    def __init__(self, energia, hambre):
        self.energia = energia
        self.hambre = hambre

    def tomar_leche(self, leche_en_litros):
        self.hambre -= leche_en_litros
        print("El gato tomó su leche :)")
        print("Hambre ... "+str(self.hambre))

    def acariciar(self):
        print("prrrr...")

    def jugar(self):
        if self.energia <=0 or self.hambre>2:
            print("El gato no quiere jugar ... :(")
        else:
            self.energia -= 1
            self.hambre += 2
            print("Jugando ... :)")

    def dormir(self, horas):
        self.energia += horas
        print("El gato tomó una siesta de "+str(horas)+" horas")        

    def hablar(self):
        print("Hola soy un gato :)")

class Gatico(Gato):
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripción(self):
        return '{} es un gato tipo: {}'. format(self.nombre,self.tipo)

garfield = Gato(10,-6)
garfield.dormir(2)
for i in range(6):
    garfield.jugar()
garfield.tomar_leche(10)
garfield.hablar()