

class Alumno:
    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print (f"Hola mi nombre es {self.nombre} que tengas un buen dia")

    def adios(self):
        print(f"me despido soy {self.nombre}")

    def __str__ (self):
        return self.nombre + " " +self.apellido

