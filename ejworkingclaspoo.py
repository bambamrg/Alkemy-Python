class Animal:
    def __init__(self, cantidad_patas, tipo):
        def comer():
            print("estoy comiendo")

class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        def correr():
            print("estoy corriendo")

class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        def volar():
            print("estoy volando")

perro1 = Perro(4, "Vertebrado", "Bambi", "Dogo")

aguila1 = Aguila(2, "Vertebrado", "Tuco", "Calva")